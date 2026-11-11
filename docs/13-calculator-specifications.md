# 共病、事件風險與心理量表：Calculator 規格

查核日期：2026-11-11。本文為公式與適用規格，**不是已實作或已做臨床驗證的 calculator 軟體**。原始係數、當代地區校準與臨床決策效益是不同查核層次。下列模型不能全部加總成新的「全人風險分數」。

## 1. 先決定要回答什麼

| 類型 | 工具 | 輸出意義 |
| --- | --- | --- |
| 目前疾病負擔 | DCSI/aDCSI、CCI | 已存在的併發症/共病程度，可作研究分層與調整 |
| 目前功能或疾病分層 | CKD-EPI、CKD G/A、FIB-4、IWGDF | 估計腎功能、纖維化篩檢或照護需求分層 |
| 未來事件風險 | KFRE、SCORE2-Diabetes、RECODe、PREVENT、WATCH-DM | 指定族群、指定時間窗內的指定事件機率 |
| 當前心理狀態 | PHQ-9、GAD-7、DDS17、PAID20、WHO-5 | 症狀、困擾或幸福感；通常不是個人未來器官事件機率 |

## 2. DCSI／aDCSI 與一般共病

DCSI 將七領域各取最高嚴重度後加總，範圍 **0–13**；不能把每個診斷碼逐項累加。Neuropathy最高1，其餘六領域最高2。原始DCSI包含臨床/實驗室資料；aDCSI是診斷碼版本，需鎖定ICD版本、查核期間與演算法，不是把缺少實驗室值當作正常。[DCSI PMID18197741](https://pubmed.ncbi.nlm.nih.gov/18197741/)、[aDCSI PMID23198714](https://pubmed.ncbi.nlm.nih.gov/23198714/)。

| 領域 | 最高分 |
| --- | ---: |
| Retinopathy | 2 |
| Nephropathy | 2 |
| Neuropathy | 1 |
| Cerebrovascular | 2 |
| Cardiovascular | 2 |
| Peripheral vascular | 2 |
| Acute metabolic complications | 2 |

具體0/1/2判定要依原始rubric或aDCSI診斷碼表，不能由LLM憑病名選嚴重度。DCSI不完整涵蓋depression、MASLD、frailty及生活負擔，宜與其餘領域並列。[原始rubric Table1](https://pmc.ncbi.nlm.nih.gov/articles/PMC3810070/)、[臺灣DCSI/CCI比較 PMID36977521](https://pubmed.ncbi.nlm.nih.gov/36977521/)。

**CCI** 用指定版本權重加總一般共病，可補 cancer、COPD、dementia 等；需區分原始CCI、age-adjusted、Deyo/Quan ICD映射。Diabetes without complications與with chronic complications不能重複計分。CCI不是本地當代死亡風險百分比，不應把歷史存活率直接套到現在病人。[Charlson1987 PMID3558716](https://pubmed.ncbi.nlm.nih.gov/3558716/)。

## 3. CKD-EPI 2021 creatinine

```text
eGFR = 142 × min(Scr/κ,1)^α × max(Scr/κ,1)^(-1.200)
       × 0.9938^age × 1.012(if female)

Scr: mg/dL；age: years；eGFR: mL/min/1.73 m²
female: κ=0.7, α=−0.241
male:   κ=0.9, α=−0.302
```

來源：[NIDDK adult equations](https://www.niddk.nih.gov/research-funding/research-programs/kidney-clinical-research-epidemiology/laboratory/glomerular-filtration-rate-equations/adults)。Scr若µmol/L先除88.4。公式為成人race-free版本；AKI、極端肌肉量、截肢、懷孕等情境須個別判斷，必要時採creatinine-cystatin C或measured GFR。**eGFR不是未來腎衰竭機率**；CKD診斷仍須慢性、albuminuria或其他腎損傷證據，不能由單次eGFR自動確診。

> 2026-11-11 全文查核補充：KFRE 原始係數以 CKD-EPI 2009 的 eGFR 開發；搭配 2021 版時 eGFR 45–59 低估、65 歲以上 5 年風險高估（Grams 2023），多重共病者可能低估（Walker 2026）。JAMA 2016 補充附錄 p9 本輪無法開啟，Original 與非北美 5 年 S0 已在開放全文核對（0.9240、0.9365），2 年與北美版維持暫定或只有規格。已實作的程式與測試見 [整合報告](14-integrated-synthesis.md) 第 8 節與 `calculators/`。

## 4. 四變項 KFRE：完整公式與校準版本

輸入age、sex、eGFR及UACR，估計CKD G3–G5病人2/5年接受dialysis或transplantation的kidney failure風險。不是用於所有糖尿病、G1–G2、AKI或已接受KRT者的通用分數。

```text
LP = −0.2201×(age/10 − 7.036)
     +0.2467×(male − 0.5642)
     −0.5567×(eGFR/5 − 7.222)
     +0.4510×(ln[UACR mg/g] − 5.137)

risk(t) = 1 − S0(t)^exp(LP)
```

male=1、female=0；ln為自然對數。風險輸出0–1，乘100顯示百分比。**UACR為mg/g**；mg/mmol需乘約8.84。缺值、零/負UACR或超出適用族群應回報無法計算，不能以極小正數或族群平均值靜默代替。

| 明確版本名稱 | S0(2 years) | S0(5 years) |
| --- | ---: | ---: |
| Original 4-variable equation | 0.9750 | 0.9240 |
| 2016 regionally recalibrated original — North America | 0.9751 | 0.8996 |
| 2016 regionally recalibrated original — non-North America | 0.9832 | 0.9365 |

係數與baseline survival由 **Tangri2016 JAMA supplement，eAppendix2，第9頁** 核對。[正文及supplement入口](https://jamanetwork.com/journals/jama/fullarticle/2481005)、[PMID26757465](https://pubmed.ncbi.nlm.nih.gov/26757465/)。這三組不能混稱「原始北美校準版」；選non-North America也不等於已完成臺灣驗證。

KDIGO2024在CKD G3–G5建議經外部驗證的風險方程；5年風險3–5%可輔助nephrology referral、2年>10%可輔助multidisciplinary care、2年>40%可輔助KRT教育與準備，需與eGFR、病程、臨床判斷及病人偏好併用。[KDIGO2024](https://doi.org/10.1016/j.kint.2023.10.016)。當代器官保護藥物、競爭死亡及KRT選擇都可能影響校準，不能把預測機率當必然病程。

## 5. FIB-4

```text
FIB-4 = age(years) × AST(U/L)
        / [platelets(10^9/L) × sqrt(ALT(U/L))]
```

原始模型來自HIV/HCV族群，後用於MASLD纖維化分流。[PMID16729309](https://pubmed.ncbi.nlm.nih.gov/16729309/)。現代T2D照護常以<1.3較低風險、≥1.3接VCTE/ELF，>2.67高風險可評估hepatology；較高齡門檻須固定版本：ADA2026對diabetes年齡≥65歲採1.9–2.0，AASLD2023文字為>65歲且cutoff>2.0。<35歲及急性疾病準確性有限；低值亦不能保證排除T2D病人的advanced fibrosis。[ADA2026 Section4](https://doi.org/10.2337/dc26-S004)。

ADA2026另提醒：T2D合併多個cardiometabolic risk factors，即使FIB-4為1.0–1.3仍可能需進一步評估；不能用單一低值排除所有高風險者。來源與界線詳見[獨立查核](../research/VERIFICATION_CALCULATORS_20261111.md)。

Platelets若標示10³/µL，數值與10⁹/L一致；若是每µL的原始count必須換算。FIB-4不是MASH確診、fibrosis stage或未來肝硬化的百分比。不能只根據ALT正常跳過評估。

## 6. 其他事件模型：有來源才實作

| 工具 | 端點／族群 | 實作狀態與限制 |
| --- | --- | --- |
| SCORE2-Diabetes | 歐洲T2D初級預防，常用40–69歲、無ASCVD或severe target-organ damage；10年fatal/nonfatal MI或stroke | 本次未逐項轉錄所有sex-specific係數與地區recalibration，**spec_only**。不得替臺灣任選歐洲區域。[PMID37247330](https://pubmed.ncbi.nlm.nih.gov/37247330/)、[ESC2023](https://doi.org/10.1093/eurheartj/ehad192) |
| RECODe | 不同方程各估nephropathy、retinopathy、neuropathy、MI、stroke、HF、死亡 | 原始ACCORD及外部驗證；**每種outcome一條方程**，不是總分。完整coefficients/transforms/baseline survival未逐項實作。[PMID28803840](https://pubmed.ncbi.nlm.nih.gov/28803840/)、[validation PMID29269511](https://pubmed.ncbi.nlm.nih.gov/29269511/) |
| PREVENT | 適用無已知CVD者，10年30–79歲、30年30–59歲；CVD/ASCVD/HF不同端點 | 需用當前AHA公式；2026-10-14官方HbA1c修正已確認，影響HbA1c add-on與full模型；base與僅UACR/SDI版本不受影響。完整修正係數與測試向量仍待驗證，保持spec_only。[官方FAQ](https://professional.heart.org/-/media/PHD-Files/Guidelines-and-Statements/PREVENT/PREVENT-Update-FAQ-101426.pdf)。[AHA官方](https://professional.heart.org/en/guidelines-and-statements/prevent-calculator) |
| WATCH-DM | 無既往HF的T2D，5年HF hospitalization | 使用發表的確切point或continuous版本，勿混用。[PMID31519694](https://pubmed.ncbi.nlm.nih.gov/31519694/) |
| UKPDS Risk Engine | 與UKPDS相近者的CHD/stroke初級預防 | 與UKPDS Outcomes Model不同；依Oxford官方FAQ、下載及授權，現代臺灣校準待驗。[Oxford FAQ](https://www.rdm.ox.ac.uk/about/our-facilities-and-units/DTU/software/risk-engine/faq) |
| Karter hypoglycemia tool | T2D未來12個月因低血糖急診/住院 | 不是所有CGM低值或輕度低血糖；需核對原始風險分類、藥物與既往事件輸入。[原文](https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2649265) |
| IWGDF risk classification | 足部LOPS/PAD/變形/潰瘍或截肢史/ESRD；0–3級 | 追蹤約12、6–12、3–6、1–3個月；不是單一未來截肢百分比。未做足部檢查不能預設0級。[IWGDF2023](https://iwgdfguidelines.org/wp-content/uploads/2023/07/IWGDF-Guidelines-2023.pdf) |

上表spec_only模型的完整公式應由原文、官方套件及測試向量取得後，另建版本並驗證；此報告沒有產生看似可執行的替代係數。

## 7. 心理量表的計分與處理

以下只提供計分規格，不重製完整問卷；臨床需使用有來源、適用族群與翻譯驗證的繁中正式版本。

| 量表 | 計分公式與常用分界 | 代表什麼／後續行動 |
| --- | --- | --- |
| PHQ-9 | 9題各0–3，sum0–27；5/10/15/20為常用症狀嚴重度界線；≥10進一步評估 | Depression screening與追蹤，不能單靠總分確診。第9題任何陽性接即時人工評估。[PMID11556941](https://pubmed.ncbi.nlm.nih.gov/11556941/) |
| GAD-7 | 7題各0–3，sum0–21；5/10/15為常用界線；≥10進一步評估 | Anxiety症狀；不是CVD風險模型。[PMID16717171](https://pubmed.ncbi.nlm.nih.gov/16717171/) |
| DDS17 legacy | 17題各1–6，mean=sum/17；<2 low、2–2.9 moderate、≥3 high distress | 四分量表可定位emotional、regimen、interpersonal、physician distress。不可與DDS2或新T2-DDAS29題互換。[development](https://pubmed.ncbi.nlm.nih.gov/15735199/)、[cutoffs](https://pubmed.ncbi.nlm.nih.gov/22228744/) |
| PAID20現行常用版 | 20題各0–4，sum×1.25→0–100；≥40常用high distress | 原始1995研究為六點選項，不能只引原始摘要驗證現行計分。PAID5不可套本公式。[原始](https://pubmed.ncbi.nlm.nih.gov/7555499/)、[現行NDSS說明](https://www.ndss.com.au/health-professionals/supporting-emotional-health/mental-health-questionnaires/paid-scale/) |
| WHO-5 | 5題各0–5，raw0–25×4→0–100，越高越好；raw<13常用進一步評估門檻 | 正向well-being。WHO官方採percentage<50或raw<13；完整答題的合法分數為4的倍數，實際raw≤12對應≤48。[WHO2024](https://www.who.int/publications/m/item/WHO-UCN-MSD-MHE-2024.01) |

DDS17的「2–2.9」在程式規格需明確處理連續平均值，例如2.94；建議保存原始平均，以<2／2≤x<3／≥3分類並由量表負責人核定，不先四捨五入造成分類改變。這是實作邊界澄清，不是新增臨床cutoff。

PHQ-9/GAD-7的重製一般不需額外許可，但翻譯驗證仍須查核；WHO2024採CC BY-NC-SA3.0IGO，不能說所有工具皆可無限制商用。DDS/PAID各版本及翻譯條件需與權利人確認。缺答不可靜默補零或依病歷推答案；若特定正式版允許缺答處理，需明列規則與有效題數。

## 8. 統一資料規格與驗證要求

每筆結果保留：`instrument, version, formula_source, endpoint, horizon, eligibility, units, input_dates, missingness, calibration_region, result, interpretation, action_owner, clinician_review`。

Calculator驗證至少包含：原文向量核對、mg/g與mg/mmol換算一致、邊界年齡/分期、非正值拒算、缺值拒算、超出族群不輸出、跨地區版本差異；心理量表另驗證方向、題數、上限及警示不被總分覆蓋。通過公式測試仍不代表本地校準或臨床效益驗證。

