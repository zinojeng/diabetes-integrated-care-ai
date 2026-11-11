# complications session 報告：成人 T2D 的整合照護困難點、整合內容、共病評估與介入證據

日期：2026-11-11｜角色：complications｜範圍：成人 T2D 為主（ACCESS 為青少年試驗，已明標）
標記：📄 = 本地全文（PMC E-utilities JATS→md）已用 grep 驗證，驗證紀錄見 `literature/notes/complications/grep_verification.md`（236 項比對，0 FAIL）；📌 = 僅 PubMed abstract／metadata，不做超出 abstract 的數字斷言。`UNRESOLVED` = 本 session 無法確認，不以推論補洞。
證據表：`evidence_table.csv`（40 筆；29 筆開放全文、11 筆 abstract-only）。

> 本報告不是 systematic review（無雙人獨立篩選、無正式 ROB 評分）；是以研究名稱＋主題檢索的目的式綜整，檢索式與失敗紀錄見 `search_log.md`。內容不是已部署的臨床診療系統，介入「改善達標」不等於「改善病人結局」。

---

## 0. 先給結論（10 點）

1. **整合照護對「過程指標與代理指標」的效果一致，對「硬終點」的效果少、小、且條件依賴。** 代理指標：CARRS 多重目標達成 18.2% vs 8.1%（RR 2.24, 1.71–2.92）[PMID 27398874] 📄；JADE-DKD team-based care RR 1.20（1.03–1.40）[PMID 35333363] 📄；Cochrane 553 RCT 網絡後設回歸顯示效果「modest」，證據確定性多為 low／very low，平均追蹤僅 12.5 個月 [PMID 37254718] 📄。
2. **硬終點證據分歧：** Steno-2 正向（CVD HR 0.47；21 年死亡 HR 0.55）[PMID 12556541 📌；27531506 📄]，但 n=160 且為高強度專科介入；ADDITION-Europe 5 年 HR 0.83（0.65–1.05）、10 年 HR 0.87（0.73–1.04）皆未達顯著 [PMID 21705063 📄；31748169 📌]；J-DOIT3 主要複合終點 HR 0.81（0.63–1.04）p=0.094，且非嚴重低血糖 41% vs 22% [PMID 29079252 📌]；JADE 12 個月臨床事件 OR 0.94（0.74–1.21）／1.02（0.83–1.25）[PMID 33929522 📄]。
3. **「持續投入」是效果的條件：** CARRS 6.5 年，微血管首發事件 HR 0.68（0.56–0.83），但**只出現在繼續實施介入的站點**，大血管終點無組間差異 [PMID 38829880 📄]。這是目前最直接支持「整合照護要有常設人力與流程，而非一次性專案」的隨機資料（但為 post hoc、74.5% 有 6.5 年資料）。
4. **哪些元件有效？** Cochrane 排序中 case management、team changes、patient education、promotion of self-management 在多數結局屬 "Top" [37254718 📄]；JADE-DKD 中「個人報告＋護理電話」(empowered care) 相對 usual care RR 0.95（0.80–1.12）無益，加上固定醫師-護理團隊 ≥6 次接觸才有效 [35333363 📄]。→ 「產生報告」不等於「有人解讀並行動」。
5. **困難點最硬的量化是「流程斷點」而非「不知道指引」：** CKD 病人 59% 未做 albuminuria 測試 [36434513 📄]；新偵測 albuminuria 後 1 年內 retest 46%、轉介腎臟科 28%、RASi／SGLT2i 起始 10%／12%／37%（依嚴重度）[41360255 📄]；SGLT2i 在 NICE 適用者僅 17.5%（CKD-only 3.8%）[42723263 📄]；US DR care cascade 中位數：篩檢 59.4%、確診者首次連結治療 52.0%、追蹤中斷 70.3% [42270111 📄]。
6. **篩檢完成率會被誤讀：** ACCESS（青少年，T1D+T2D，n=164）AI 組完成眼底檢查 100% vs 22%，但 AI 判陽性者只有 16/25（64%）完成眼科追蹤；對照組「22% follow-through」是 18/83 的一般檢查完成、且無人有 DED，兩個分母不可直接相減 [38212308 📄]。**即使完全自動化篩檢，下游追蹤仍有 36% 流失。**
7. **共病量測有顯著缺口：** aDCSI／CCI 為診斷碼型、以死亡為校準目標（Taiwan 1,002,589 人，aDCSI C-index 0.760/0.794/0.781）[36977521 📄]；它們不含 eGFR／UACR 數值、心理、功能／frailty、治療負擔、SDOH；且「病歷沒有碼」≠「沒有病」。T2D 共病盛行率 83.17%（I² 97.0%）高度依定義而異 [41382017 📄]。
8. **Taiwan P4P 觀察研究的效果量（2020 aHR 0.58；2016 HR 0.76）遠大於 ADDITION／J-DOIT3／JADE 等 RCT（與高強度小樣本 Steno-2 相當），且有依從度梯度（≥1 年良好依從 aHR 0.48、≥2 年 0.36）→ 強烈提示 healthy-adherer／選擇偏誤，不可當成整合照護的因果效益** [32049836 📄；27399144 📄]。
9. **既有 `docs/03` 數字沒有發現硬性錯誤，但有 8 處重要省略／不精確**（第 7 節），最重要：漏掉 ADDITION／J-DOIT3 中性結果與 CARRS 長期追蹤、INDEPENDENT 的次要結局多數無顯著差異、JADE 的兩階段設計與追蹤流失。
10. **無法處理／UNRESOLVED：** ADA Standards of Care 2026 Section 4 全文（PMC 僅 abstract）；Steno-2 2003/2008、ADDITION 10 年、J-DOIT3、INDEPENDENT 全文（無開放全文，僅 PubMed abstract）；HF／PAD／認知／frailty 的整合照護隨機證據（本輪未找到可核對的糖尿病專屬 RCT）；「門診時間限制」的量化研究（未檢出）。

---

## 1. 證據可得性與方法限制（影響信心度）

- 全文取得：`fulltext_tools.py pmc <PMCID>`。**發現工具缺陷：** 以 PMID 呼叫時，`elink` 的 `linksetdbs[0]` 可能是「引用該文的 PMC 文章」而非該文本身——Steno-2 2003／2008、ADDITION 2019、J-DOIT3 四個 PMID 取回的是 2026 年無關文章（PMC13738796 等），我已刪除這些檔案與對應 receipt 行，並只使用「PMCID 與 esummary 標題比對一致」的檔案。修正建議見 handoff。
- `download_with_fallback`（`use_scihub=false`）對 5 篇無開放全文者全部失敗：PubMed 來源不提供 PDF；Unpaywall 回報 "no OA URL found (or …UNPAYWALL_EMAIL missing)"（未能分辨是無 OA 版本或未設定 email 環境變數；我未自行填入使用者 email）。**未使用 Sci-Hub**：這 5 篇雖皆為 2021 年以前（協議允許作最後備援），但屬繞過出版商付費牆，本 session 不自行決定；以 abstract-only 如實標示，是否補抓留給 lead／使用者明示。
- 本報告沒有 pooled 分析、沒有自己計算的 effect size（引用皆為原文數字）。

---

## 2. 困難點（研究問題 1）

### 2.1 Guideline-concordant care gap（流程斷點）

| 斷點 | 量化證據 | 解讀界線 |
| --- | --- | --- |
| UACR 測試不足 | 30 項研究、>2,900 萬人；固定效應約 22%，隨機效應 49%（95% CI 7–93%），I² ≈100%；範圍 <5% 到近 100% [41345917 📄] | **單一數字不可解讀**；差異主要來自制度（protocol 化方案近 100%）。美國商保／MA CKD 病人 59% 無 albuminuria 測試 [36434513 📄] |
| 新發現 albuminuria 後處理 | 215,035 人（Stockholm）：1 年內 retest 46%；符合適應症者轉腎臟科 28%；RASi／SGLT2i 1 年起始 10%／12%／37%（中度／重度／極重度）[41360255 📄] | 單一區域、含非糖尿病者；為描述性 |
| SGLT2i 使用不足 | UK 初級照護 980 萬成人：NICE 適用者 17.5% 在用，CKD-only 3.8%，三適應症皆符 32.9% [42723263 📄]；US VA T2D+CKD+ASCVD 174,443 人：2020 年 11.5% 處方，女性 OR 0.59（0.52–0.67），院所間 MRR 1.58 [36702340 📄]；VA T2D+CAD：2023 年 trial-concordant 處方 SGLT2i 42%、GLP-1RA 15% [40275941 📄]；腎臟科單一診所 587 人：SGLT2i 12.9%、GLP-1RA 10.4% [41031090 📄] | 「適用」以演算法或試驗條件界定，禁忌／不耐受未必可從資料看出；2020 與 2023–2024 資料不可混比 |
| 眼底 cascade | US 46 項研究：兩年內篩檢中位 59.4%（15.5–78.7%）；有 DR 者 70.1% 不知診斷；確診後首次連結治療 52.0%；追蹤中斷 70.3% [42270111 📄]。全球篩檢依從：高收入 66.9%、中低收入 39.3%（77 項研究，11,383,715 人）[39094991 📌] | cascade 研究限美國；異質性大 |
| Clinical inertia | 25 項研究、575,067 人，多數研究 >50% 有 inertia，各國範圍極寬（US 35.4–85.8%）[36676805 📄]；UK CPRD 105,477 人：HbA1c ≥7% 且延遲 1 年強化，composite CVE HR 1.62（1.46–1.80）[26249018 📄] | inertia 定義不一；CPRD 為觀察性，存在 confounding by indication |

### 2.2 Fragmentation、失聯與可近性

- 連續性照護（continuity of care）SR（42 項研究，無法 meta-analysis）：高 CoC 與住院減少（16/18 項研究）、死亡（6/7）、併發症（7/7）相關，但血壓（2/13）、血脂（1/6）幾乎無關；研究多為 vote-counting，混雜與選擇偏誤明顯 [34217212 📄]。→ 連續性與硬終點「相關」，與代理指標關聯弱，因果未確定。
- 門診失約（34 項研究）：年輕、吸菸、經濟壓力與較高 HbA1c 相關；質性研究顯示失約只有部分是物流問題，心理社會因素重要；僅 1 項 RCT [31968127 📌]。
- SES／種族與品質（MA）：黑人病人 HbA1c／BP 達標 OR 0.67–0.68，但眼／足檢查 OR 1.22–1.47；教育程度與眼底檢查完成相關 [32720345 📌]——**不同品質指標方向不同，不能用單一「品質」概念概括 SDOH 影響。**
- **UNRESOLVED：** 「門診時間限制」與 health literacy 對上述斷點的量化貢獻；本輪檢索未得到可核對的直接研究。

### 2.3 Multimorbidity 與治療負擔

- T2D 的 multimorbidity 盛行率 83.17%（79.72–86.63%），concordant 50.21%、discordant 47.24%，但 I² 97.0%，且「共病」定義納入高血壓等常見併存，故不宜把 83% 當作「有第二個需要獨立處置的疾病」的比例 [41382017 📄]。
- 治療負擔量測：混合方法 SR（26 篇）整理出 7 個核心負擔面向（經濟、藥物、行政、生活型態、醫療、時間／交通、醫療資訊）；PETS、TBQ、MTBQ 在 COSMIN 評價最佳；10 個 PROM 中 8 個 responsiveness 評為 negative，研究多為橫斷與資源充足場域 [38858619 📄]。→ 可作為整合照護的「負擔輸入」，但無證據顯示以此調整治療能改善結局（**UNRESOLVED**）。

---

## 3. 整合照護需要整合什麼（研究問題 2）

下表為**依本輪證據的整理框架**；「證據強度」指糖尿病專屬的整合介入證據，不是疾病本身的重要性。

| 整合層 | 具體內容 | 有直接支持的證據 | 證據邊界 |
| --- | --- | --- | --- |
| 資料 | 結構化評估（HbA1c、BP、LDL、eGFR、UACR、眼、足）、registry、風險分層 | JADE portal 結構化評估＋分層 [33929522 📄]；Cochrane 中 electronic patient registry 為組合效果元件 [37254718 📄] | JADE 對照組本身也做結構化評估 → 「評估」的獨立效果未分離 |
| 人員 | 非醫師照護協調員／護理個管、固定醫師-護理團隊、專科 case review、足部 MDT | CARRS 協調員＋DS-EHR [27398874 📄]；JADE-DKD 固定團隊≥6 次接觸 [35333363 📄]；TEAMcare 護理個管＋每週精神科／PCP 督導 [21190455 📄]；足部 MDT 含 podiatry：總截肢 RR 0.69（0.54–0.89, I² 64%）、重大截肢 RR 0.45（0.23–0.90, I² 67%）[32192509 📄]（多為觀察研究，作者自述證據不足） | 協調員與軟體綑綁，無法單獨歸因（CARRS 全文自述 “unable to examine the relative effectiveness of individual intervention components” 📄） |
| 決策 | treat-to-target、decision-support EHR、處方調整提示、專科回饋 | TEAMcare 調整胰島素／降壓／抗憂鬱藥機會較高 [21190455 📄]；CARRS DS-EHR | J-DOIT3 顯示「更強化的目標」≠更好（低血糖增加、主要終點未顯著）[29079252 📌] |
| 追蹤迴圈 | 異常結果的確認、轉介、治療起始、轉介完成與失聯追蹤 | ACCESS 流程 [38212308 📄]；SCREAM 顯示現況斷點 [41360255 📄] | **沒有成人 T2D 隨機試驗以「轉介完成／治療起始」為主要結局的整合介入被本輪確認（UNRESOLVED）** |

### 器官／面向別（以證據層級誠實標示）

- **Cardio-kidney-metabolic（CKM）：** Taiwan 健檢世代 515,602 人，CKM（含 stage 1–4）占 71.5%；CKM 與 all-cause 死亡 HR 1.33（1.28–1.39）、CVD 死亡 HR 2.81、incident ESKD HR 10.15；每多一個 CKM 組成，all-cause 死亡 HR 1.22 [40570007 📄]。為預後關聯，不是整合介入證據。
- **CKD／DKD：** JADE-DKD [35333363 📄]、SCREAM 斷點 [41360255 📄]、Steno-2 ESRD 1 vs 6（2008，abstract）[18256393 📌]。
- **Retinopathy：** Steno-2 光凝需求 RR 0.45（0.23–0.86）[18256393 📌]；篩檢 cascade [42270111 📄]；Cochrane 中 case management 對 retinopathy screening OR 1.09（0.66–1.78），確定性 very low [37254718 📄]；估計三元件組合（PE+PR+TC）在基準 50% 下可增加 33 個百分點篩檢率（模型估計）。
- **Neuropathy／foot：** Steno-2 21 年追蹤中，peripheral neuropathy HR 1.12，與其他微血管結局方向不同 [27531506 📄]；足部 MDT [32192509 📄；38461443 📌（數字未驗證）]。IWGDF 指引本輪**未檢索** → UNRESOLVED。
- **MASLD：** FIB-4→elastography 路徑預估會把約 40% 的 T2D 導向 transient elastography、約 20% 導向三級照護，false discovery 最高 80%（作者估計）[38334817 📄]。→ 「全面篩檢」若無分流容量，會把問題轉成轉介過載。無整合介入試驗證據。
- **HF／PAD／認知／frailty：** 本輪未找到糖尿病專屬的整合介入隨機證據 → UNRESOLVED。老年／frail 指引 SR（23 份 CPG）：多數建議健康老人 HbA1c <7.0–7.5%、frail 或醫療複雜者 <8.0–8.5%，但藥物建議差異大 [39572394 📄，僅 abstract 段]。
- **心理：** TEAMcare 與 INDEPENDENT 見第 5 節；細節留給 psychosocial session。

---

## 4. 如何更完整評估共病（研究問題 3）

1. **ADA Standards of Care 2026, Section 4（Comprehensive Medical Evaluation and Assessment of Comorbidities）[41358897]：📌 僅標題與前言（PMC 開放子集無本文）。** 我不複述其建議內容；→ UNRESOLVED，建議 lead 或 Codex 在可存取全文處核對。
2. **DCSI／aDCSI／CCI：**
   - aDCSI 為 13 點量表（七類並發症，嚴重度各 0–2，neuropathy 0–1）[36977521 📄，本文 L49；Young 2008 原始 DCSI 的 Table 1 因 PMC 僅 abstract 無法在本地核對 [18197741 📌]]。
   - Taiwan NHI 1,002,589 人：aDCSI HR 1.21（1.20–1.21）優於 CCI 1.18（1.17–1.18）預測 all-cause 死亡；cause-specific：aDCSI 對癌症死亡 HR 僅 1.04；兩者合併時 aDCSI 對癌症 HR 轉為 0.98、CCI 對 CVD／糖尿病死亡轉為近中性 [36977521 📄]。→ **兩者捕捉不同面向**，單一分數不能取代分項。
   - 缺口：僅用診斷碼（無 BMI、吸菸、生活型態、檢驗值）；以死亡為標的；「無碼」被當成 0 分。這與專案原則「病歷空白不得推斷為陰性」衝突，需在 calculators 實作中明確處理缺資料（見 handoff）。
3. **建議的「評估完整度」做法（設計建議，非已驗證）：** 對每個必查項目分別記錄 `completed / not_done / unknown / refused`，把「未完成」當成一個可追蹤的狀態，而不是 0 分；不合成全人風險總分。這是依據第 2 節斷點資料的設計結論，**目前沒有研究驗證這種「完整度指標」能改善結局**。
4. **治療負擔與 multimorbidity：** 見 2.3。

---

## 5. 整合照護介入的實證（研究問題 4）

### 5.1 逐項核對（必查清單）

| 研究 | 設計／族群／n | 時間 | 主要結果（含 CI） | 終點層級 | 需保留的陰性／限制 |
| --- | --- | --- | --- | --- | --- |
| **Steno-2 2003** [12556541 📌] | 開放 RCT，T2D＋微量白蛋白尿，n=160 | 7.8 y | CVD HR 0.47（0.24–0.73）；nephropathy 0.39（0.17–0.87）；retinopathy 0.42（0.21–0.86）；autonomic neuropathy 0.37（0.18–0.79） | 硬終點 | 高風險小樣本；2000 年代藥物；僅有 abstract 本地證據 |
| **Steno-2 2008** [18256393 📌] | 同族群後續觀察 | 13.3 y | 死亡 HR 0.54（0.32–0.89）；CV 死亡 0.43（0.19–0.94）；ESRD 1 vs 6 | 硬終點 | 觀察階段；ESRD 事件少 |
| **Steno-2 2016** [27531506 📄] | 21.2 y 追蹤 | 21.2 y | 死亡 38 vs 55，HR 0.55（0.36–0.83）；中位存活 +7.9 y；peripheral neuropathy HR 1.12；**校正 CVD 狀態後死亡 HR 0.83（0.54–1.30）** | 硬終點 | 前 7.8 y 後兩組都強化治療，**非 21 年持續隨機對照**；死亡下降主要經由 CVD 下降 |
| **ADDITION-Europe 2011** [21705063 📄] | cluster RCT，篩檢發現 T2D，n=3,057 | 5.3 y | CVD 7.2% vs 8.5%，HR 0.83（0.65–1.05）；死亡 HR 0.91（0.69–1.21） | 硬終點（陰性） | 風險因子僅「slightly but significantly」較好；事件率低於預期 |
| **ADDITION 10 y** [31748169 📌] | post hoc | 9.6 y | HR 0.87（0.73–1.04）；死亡 0.90（0.76–1.07）；組間差異 y10 已減弱 | 硬終點（陰性） | 第 5 年後未維持對比 |
| **J-DOIT3** [29079252 📌] | 開放 RCT，n=2,542 | 8.5 y | 主要複合 HR 0.81（0.63–1.04）p=0.094；腦血管事件 HR 0.42（0.24–0.74, post hoc）；死亡 1.01（0.68–1.51） | 硬終點（主要終點陰性） | 非嚴重低血糖 41% vs 22%；水腫 15% vs 10% |
| **CARRS 2016** [27398874 📄] | 開放 RCT，n=1,146（印度／巴基斯坦） | 28 mo | 18.2% vs 8.1%，RR 2.24（1.71–2.92）；HbA1c −0.50 pp | 代理指標 | 輕度低血糖 133 vs 21（p<0.001）；協調員＋軟體綑綁 |
| **CARRS 6.5 y** [38829880 📄] | post hoc，854/1,146（74.5%）有資料 | 6.5 y | micro+macro 首發 40.5% vs 48.0%，HR 0.72（0.61–0.86）；微血管 HR 0.68（0.56–0.83）；**大血管無組間差異**；**僅繼續介入之站點有效** | 硬終點（部分） | post hoc、站點層級持續為非隨機、25.5% 缺值 |
| **JADE 2021** [33929522 📄] | 兩階段 RCT，n=20,834（50 站、8 國） | 12 mo | 事件 OR 0.94（0.74–1.21）／1.02（0.83–1.25）；≥2 目標 OR 1.34／1.25 | 代理指標（事件陰性） | 12 個月再評估完成率：第一階段 59.9%、第二階段 29.3%（占隨機人數）；對照組定義兩階段不同 |
| **JADE-DKD 2022** [35333363 📄] | 三臂 RCT，n=2,393 | 12 mo | team-based vs usual RR 1.20（1.03–1.40）；vs empowered 1.27（1.07–1.49）；empowered vs usual 0.95（0.80–1.12） | 代理指標 | 模型 1 對 usual 之 RR 下限 =1.00；事件無組間差；「達標者事件較少」為非隨機關聯 |
| **TEAMcare 2010** [21190455 📄] | 單盲 RCT，n=214 | 12 mo | HbA1c 差 0.58%、LDL 6.9 mg/dl、SBP 5.1 mmHg、SCL-20 0.40（P<0.001） | 代理指標＋PRO | 主要結局分析計畫於 2009-08 修改；高經驗護理；無等接觸量對照；飲食運動依從無差異 |
| **INDEPENDENT 2020** [32809002 📌；Key Points 見 PMC7435347] | 開放 RCT，n=404 | 24 mo（介入 12 mo） | 71.6% vs 57.4%（abstract），RD 16.9（8.5–25.2）；Key Points 寫 71.6% vs 54.7% | 代理指標＋PRO | **16 項預先設定次要結局：12 個月 10 項、24 個月 13 項無顯著組間差異**；severe hypoglycemia 8（4.1%）vs 0；abstract 與 Key Points 數字不一致（71.6−54.7=16.9 與 RD 吻合） |
| **Taiwan P4P 2016** [27399144 📄] | PSM 世代，2,090 對 | 5.13 y | 死亡 HR 0.76（0.64–0.92） | 硬終點（觀察性） | 殘餘混雜 |
| **Taiwan P4P 2020** [32049836 📄] | PSM 世代，5,478 對 | 約 4.3–4.4 y | aHR 0.58（0.48–0.69）；依從≥1 y 0.48、≥2 y 0.36 | 硬終點（觀察性） | 效果量與依從梯度提示 healthy-adherer；不可作因果 |

### 5.2 系統性回顧

- **Cochrane 2023（Konnyu）[37254718 📄]：** 553 RCT、412,161 人；對 HbA1c，case management 在基準 HbA1c >8.3% 時降 0.27%（0.39–0.15），≤8.3% 時約 0；三元件組合可降 HbA1c 0.41–0.62、SBP 4.39 mmHg（CM+TC+PSM，基準 SBP >136）；retinopathy／foot screening 模型估計可大幅增加，但 case management 單獨對 screening OR 為 1.09（0.66–1.78, very low）。**GRADE 多為 low／very low，追蹤平均 12.5 個月，搜尋到 2019/2021。**
- 足部 MDT [32192509 📄；38461443 📌]、連續性 [34217212 📄]：觀察性為主（見上）。
- **UNRESOLVED：** 近 5 年專門以 multidisciplinary／integrated care in T2D 為題、且報告 ROB 與 heterogeneity 的獨立 MA，本輪僅命中 Cochrane QI（最接近）與足部 MDT；其他命中者與主題不符。若 lead 需要，可進一步在 Embase／Cochrane 檢索。

### 5.3 三層終點區分（避免把達標當成結局）

| 層級 | 本輪證據 | 一句話 |
| --- | --- | --- |
| 篩檢／流程完成 | UACR 22–49%（異質）；眼底 cascade；ACCESS 100% vs 22%（青少年） | 完成篩檢 ≠ 治療；ACCESS AI 陽性者追蹤完成 64% |
| 代理指標 | CARRS、JADE、JADE-DKD、TEAMcare、INDEPENDENT、Cochrane | 一致但 modest（HbA1c 約 −0.3 至 −0.6 pp 級） |
| 硬終點 | Steno-2 正向；ADDITION、J-DOIT3、JADE 陰性或中性；CARRS 微血管 HR 0.68 但大血管無；P4P 觀察性 | 條件：高風險族群、持續介入、足夠追蹤；強化目標有低血糖代價 |

---

## 6. 篩檢異常後的處理與追蹤完成度（研究問題 5）

建議的追蹤迴圈（`screening → confirmation → treatment → referral completion`）與本輪可量化的「流失率」：

| 步驟 | 本輪最佳量化 | 來源 |
| --- | --- | --- |
| 篩檢做了沒有 | UACR 22%（固定）／49%（隨機，CI 7–93%）；CKD 病人 59% 無 albuminuria 測試；DR 兩年內篩檢中位 59.4% | [41345917 📄；36434513 📄；42270111 📄] |
| 異常是否確認 | 新偵測 albuminuria 1 年內 retest 46%（中度 45%→極重度 70%） | [41360255 📄] |
| 是否開始治療 | RASi／SGLT2i 1 年起始 10%／12%／37% | [41360255 📄] |
| 是否轉介並完成 | 腎臟科轉介 28%；DR 確診後首次連結 52.0%、追蹤中斷 70.3%；ACCESS AI 陽性追蹤完成 16/25 | [41360255 📄；42270111 📄；38212308 📄] |
| 結果是否改善 | 以上研究**均無**失明、ESKD、截肢等結局連結 | — |

- **閱讀須知：** 各步驟來自不同族群與制度，不能串接成單一「漏斗」機率。
- 缺口：沒有一個研究在同一批成人 T2D 中同時追蹤 screening→treatment→硬終點；ACCESS 的 follow-through 只觀察 6 個月且僅 25 個陽性。

---

## 7. 既有文件須修正清單

核對方式：以本地全文逐項 grep（見 `grep_verification.md`）。**結論：`docs/03` 與 `claim_review.csv` 的主要數字（n、PMID、期刊年份、HR／RR）未發現錯誤；須修的是省略與界線不精確。**

### 7.1 `docs/03-integrated-care-evidence.md`

| 行 | 現況 | 問題與建議（含來源） |
| --- | --- | --- |
| L7 TEAMcare | 12 個月多項改善；飲食運動無差異 | 數字正確（n=214=106+108；差值 0.58% HbA1c／LDL 6.9／SBP 5.1／SCL-20 0.40）📄。**補：** 主要結局分析計畫於 2009-08 改為合併模型；無等接觸量對照；高經驗護理；對事件未具檢定力（原文 limitations） |
| L8 INDEPENDENT | 24 個月複合結果較佳 | 方向正確。**補：** (a) 16 項預先設定次要結局中 12 個月 10 項、24 個月 13 項無顯著差異；(b) severe hypoglycemia 8 vs 0；(c) abstract 71.6 vs 57.4 與 Key Points 71.6 vs 54.7 並存（RD 16.9 吻合 54.7），需保留註記（對應 claim C03）📌 |
| L9 CARRS | 只引 2016 | 數字正確（1,146）📄。**補：** 18.2% vs 8.1%，RR 2.24（1.71–2.92）；輕度低血糖 133 vs 21；**6.5 年追蹤顯示微血管 HR 0.68、大血管無差異、僅續行站點有效**[38829880] 📄 |
| L10 JADE | 「對照組也接受部分結構化評估」 | 不精確：兩階段隨機（7,537＋13,297），第一階段對照有評估＋個人報告、第二階段僅評估。**補：** 事件 OR 0.94（0.74–1.21）／1.02（0.83–1.25）；12 個月再評估完成率 59.9%／29.3%；50 站 8 國 📄 |
| L11 JADE DKD | 加入團隊面談較有利 | 方向正確。**補：** 模型 1 對 usual 之 RR 1.17（1.00–1.37），下限貼近 1；empowered care 單獨相對 usual RR 0.95（0.80–1.12）無益；usual 臂也有 portal 評估；12 個月、無事件差異 📄 |
| L12 P4P | 2020 研究 | 正確（5,478 對）。**補：** aHR 0.58（0.48–0.69）；依從梯度 0.48／0.36 提示 healthy-adherer；並列 2016 研究 HR 0.76（0.64–0.92）；並說明 P4P 是以誘因驅動之結構化方案 📄 |
| 整表 | 只有 6 項，皆為正向或達標改善 | **缺：** Steno-2、ADDITION-Europe、J-DOIT3（中性／陰性）與 Cochrane QI；應加列以符合「保留陰性或不確定試驗」 |
| L14 | 「評估之後需要有人解釋結果…持續追蹤」 | 有 JADE-DKD empowered-care 無益的證據支持（上列），可加註來源 |

### 7.2 `workflow/claim_review.csv`（建議 `claude_status` 更新值，由 lead 寫入）

| 行／claim | 建議狀態 | 依據 |
| --- | --- | --- |
| L2 C01 | `verified_fulltext` | JADE ITT OR 0.94／1.02（事件）、OR 1.34／1.25（目標）📄 PMC8087959 |
| L4 C03 | `partially_verified` | PubMed abstract 71.6 vs 57.4 與 PMC Key Points 71.6 vs 54.7 皆確認；**Table 2 本 session 取不到（PMC 無本文）→ UNRESOLVED**；54.7 與 RD 16.9 算術一致 |
| L5 C04 | `partially_verified` | 13 點、neuropathy 0–1：由 Hu 2023（PMC10069524 L49）確認為 **aDCSI**；Young 2008 PMC3810070 無本文，Table 1 無法本地核對；注意 DCSI 與 aDCSI 勿混稱 |
| L7 C06 | `verified_fulltext` | ACCESS：青少年 8–21 歲（T1D＋T2D）、單中心；完成率 100%（81）vs 22%（83）；無視力結局 📄 PMC10784572 |
| L12 C10 | `verified_fulltext` | follow-through 16/25=64%（AI 陽性）vs 18/83=22%（對照，無人有 DED）→ 分母不同，補充限制成立 📄 |
| C02、C05、C07、C08、C09、C11 | `not_checked_by_complications` | 不屬本 session 範圍 |

### 7.3 其他連帶（lead 酌情處理）

- `research/DM_AI_Integrated_Literature_Review_20261111.md` L101–106 與 `docs/03` 同文，適用 7.1。
- `sources/evidence_matrix_20261111.csv` L4（ADDITION-Europe 2011）DOI 空白 → `10.1016/S0140-6736(11)60698-3`；L12（Taiwan newly diagnosed P4P 2020）DOI 空白 → `10.1097/MD.0000000000019139`。
- `docs/12-deep-research-update.md` L29–37、L66–67：本輪核對 Steno-2 2003／2016、ADDITION、J-DOIT3、CARRS、JADE、P4P 的數字皆吻合。

---

## 8. 對上位問題的含義（限於本 session 證據）

- 「如何整合」不是增加更多資料欄位，而是**把評估、解讀、決策、追蹤與轉介完成綁成有人負責的迴圈**；證據顯示迴圈中「人力／團隊」比「報告」更關鍵（JADE-DKD、Cochrane、CARRS 長期）。
- 若導入 AI／軟體（交 methods_ai 評估），本 session 的證據只能支持「軟體＋人力協調」的組合，**不能支持以軟體取代人力**（CARRS、INDEPENDENT 均為綑綁介入）；ACCESS 顯示 AI 可提高篩檢完成率，但下游追蹤仍會流失。
- 評估完整度與風險分數必須區分「未做／未知／陰性」；不可合成全人總分。

## 9. 限制與 UNRESOLVED 彙整

1. 11 筆為 abstract-only（見 `evidence_table.csv` `access_level`）；其中 Steno-2 兩篇、ADDITION 10 年、J-DOIT3、INDEPENDENT 之 Methods／harms／limitation 欄只含 abstract 內容。
2. ADA 2026 Sec.4 內容未取得。
3. HF／PAD／認知／frailty、IWGDF、門診時間限制、health literacy 的量化研究：本輪未得到可核對資料。
4. 獨立的「近 5 年 multidisciplinary care in T2D MA（含 ROB）」只找到 Cochrane QI 與足部 MDT。
5. Meloni 2024 足部 MDT MA（38461443）數字未驗證。
6. 本報告所有引用皆為原文數字；未做任何新統計。

---

## 10. crosscheck 後修訂（第二階段；以下補充／更正前文，前文未改動）

### 10.1 全文取得結果

- 依 `SESSION_PROTOCOL_v2.md` 的 Sci-Hub 最後備援條款嘗試 5 篇：**ADDITION-Europe 10 年、J-DOIT3、INDEPENDENT 取得全文**（LlamaParse＋`verify` PASS＋grep 通過，`PMID31748169_ADDITION10y.md`、`PMID29079252_JDOIT3.md`、`PMID32809002_INDEPENDENT.md`）；**Steno-2 2003、2008 兩次被 auto-mode 權限分類器拒絕，維持 no_fulltext**，未重試、未改道。第 1 節「5 篇無全文」因此改為 2 篇（Steno-2 2003／2008）。
- 證據表 E05、E06、E12 已更新為全文驗證；新增 E41–E51（縱向心理／認知結局證據）。

### 10.2 更正／降級（對前文）

1. **INDEPENDENT（§0 第 2 點、§5.1 該列、§7.1 L8）：** 全文 Table 2（`PMID32809002_INDEPENDENT.md` L387）確認複合結局 **71.6% vs 54.7%**，RD 16.9（8.5–25.2）；abstract 的 57.4% 為離群值。成分層級（24 個月）：SCL-20 ≥50% 改善 77.7% vs 63.6%（RD 14.1, 6.7–21.6）；HbA1c ≥0.5 pp 下降 RD 8.7（−0.9 到 18.4）NS；SBP、LDL 成分 RD 0.3、−2.5 皆 NS；平均 HbA1c 8.7 vs 8.6。→ **此試驗在 24 個月主要是「憂鬱改善」，心代謝成分未能獨立確認；§5.3「代理指標一致」對 INDEPENDENT 應附此限制。**
   - 前文 §7.1 L8 的建議「保留 abstract 57.4 vs Key Points 54.7 註記」更新為：**正文與 Table 2 為 54.7；abstract 為 57.4（與 RD 16.9 不吻合，疑為 abstract 錯植）**；claim C03 可由 `partially_verified` 升為 `verified_fulltext`（Table 2 已核對，離群值在 abstract）。
2. **J-DOIT3（§0 第 2 點、§5.1）：** 全文 L423–L431：主要終點 HR 0.81（0.63–1.04）p=0.094 仍為陰性；但預先設定的基線校正分析 HR 0.76（0.59–0.99）p=0.042，主要次要終點（死亡＋MI＋stroke）HR 0.74（0.54–1.01）p=0.055；腎病變發生／進展 181 vs 257 件、HR 0.68（0.56–0.82）；視網膜病變發生／進展 317 vs 362 件、HR 0.86（0.74–1.00）p=0.046；任一組均無視力喪失，且無 ESRD 作為首發事件。→ 結論由「主要終點陰性」改為「**主要終點陰性，但中間微血管次要終點偏向有益；代價為非嚴重低血糖 41% vs 22%**」。這些次要終點為 albuminuria 階段轉換等中間結局，非 ESKD／失明。
3. **ADDITION 10 年（§5.1）：** 全文確認 HR 0.87（0.73–1.04）、3,057 人同意參加、14 人失聯、12 人退出、3,031 人納入分析（L15、L288、L326），與 abstract 一致，無更動。
4. **§2.1 的 clinical inertia 與流程斷點資料不變。**

### 10.3 新增：併發症事件後心理／認知結局（縱向 vs 橫斷）

詳見 `crosscheck.md` §2.1。摘要：登記縱向資料（Horsbøl 2024，N=265,799）顯示 T2D 發生併發症後憂鬱／焦慮 HR 1.77（1.73–1.80），amputation 2.16 最強、retinopathy 1.13 最弱 📌；彙整性的「併發症→憂鬱」證據僅 HR 1.14（2 項研究）📌；視力喪失、透析、足潰瘍後的 DD／憂鬱縱向研究未檢出（`UNRESOLVED`）；嚴重低血糖後的**失智** HR 2.38–2.85 📌，憂鬱／DD 無縱向證據。結局多為診斷碼／處方定義，非 DD 量表。

### 10.4 新增：「僅提醒」不是有效元件

Cochrane QI 的 clinician reminders 單獨：HbA1c、SBP、LDL 的 CrI 皆跨 0；retinopathy screening OR 1.10（0.70–2.09）、foot screening OR 1.30（0.71–2.57），very low 確定性（`PMC10233616.md` Summary of findings 5）📄。與 §5.2 搭配：有效元件集中於 case management、team changes、教育與自我管理。
