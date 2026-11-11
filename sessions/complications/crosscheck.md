# complications crosscheck（第二階段）

日期：2026-11-11。輸入：`sessions/methods_ai/handoff.md` §B（→complications）、`sessions/psychosocial/handoff.md` §C、`sessions/calculators/`（目前只有 `search_log.md`；`calculators/dmic_calculators/` 內**沒有任何 DCSI／aDCSI 實作**，故無從核對我 handoff 對 calculators 的 aDCSI 問題，該題保持開放）。
引用格式：PMID＋本地檔＋行號（`literature/parsed/complications/`，git-ignored）。📄＝全文 grep；📌＝僅 abstract。驗證紀錄：`literature/notes/complications/grep_verification.md`（含 Phase 2，皆 PASS）。

---

## 0. Sci-Hub 補全文：結果與依據

- **依據：** `workflow/SESSION_PROTOCOL_v2.md` 第 2 步第三項把 Sci-Hub 列為 2021 年以前論文的最後備援，lead 轉述使用者原始指示要求使用；我無法自行查看使用者原話，所以僅以協議文字為依據，並以工具的權限機制為準。
- **結果（5 篇）：**
  | 論文 | 結果 | 後續 |
  | --- | --- | --- |
  | ADDITION-Europe 10 年（31748169） | 下載成功（sci-hub.ru） | LlamaParse 89,038 字元；`verify` PASS 4/4；grep 通過 |
  | J-DOIT3（29079252） | 下載成功（sci-hub.ee） | LlamaParse 94,284；`verify` PASS 5/5；grep 通過 |
  | INDEPENDENT（32809002） | 下載成功（sci-hub.ee） | LlamaParse 98,006；`verify` PASS 4/4；grep 通過 |
  | Steno-2 2003（12556541） | **被 Claude Code auto-mode 分類器拒絕**（理由 "Walled Content from a Copy"） | **no_fulltext**；未重試、未改用其他管道規避 |
  | Steno-2 2008（18256393） | 同上被拒絕 | **no_fulltext** |
- 兩次被拒是權限層的明確決定，我不繞過；如使用者要補這兩篇，需由使用者自行放行 `mcp__scihub__download_pdf` 或直接提供 PDF。
- 檔案保存於 `literature/fulltext/complications/`（git-ignored）；解析檔在 `literature/parsed/complications/PMID*_*.md`。

---

## 1. 回覆 methods_ai §B（→complications）

### 1.1 問題 A：每項研究的主要結局是「檢查完成」還是「異常後處置完成」？分母？ → **ACCEPT，附逐項表**

| 研究（PMID） | 主要結局性質 | 分母 | 是否構念重疊（介入＝檢查本身）| 定位 |
| --- | --- | --- | --- | --- |
| ACCESS（38212308） | 篩檢完成：6 個月內完成眼底檢查 | 全部隨機：81（AI）／83（對照） | **是**：AI 組的「完成」就是診間做 AI 檢查；100% 為構念內建 | PMC10784572 L45 📄 |
| ACCESS 次要：follow-through | 異常後眼科追蹤完成 | AI 組＝**25 位 AI 陽性**中 16 人（64%，CI 43–81）；對照＝**全部 83 人**中 18 人（22%）去看眼科、且無人有 DED | **分母不同、事件定義不同**，不可相減；論文自己算的組間差 42%（21–63）混用了這兩個分母 | PMC10784572 L51 📄 |
| CARRS 2016（27398874） | 代理指標達標（HbA1c<7% 且 BP 或 LDL） | 全部隨機（575／571），ITT RR 2.24 | 否；無篩檢完成或轉介完成結局 | PMC6561084 L95 📄 |
| JADE（33929522） | 事件（12 個月）＋ ≥2 目標 | 事件為 ITT 隨機人數；12 個月再評估僅 59.9%（ph1）／29.3%（ph2）有資料 | **部分是**：結構化評估（含眼／足檢查）本身就是介入 E1；ph1 對照也有評估＋報告，ph2 對照僅有評估 | PMC8087959 L62、L139、L149 📄 |
| JADE-DKD（35333363） | ≥3／5 目標達成 | ITT 2,393 | 否 | PMC8956973 L64、L162 📄 |
| Cochrane QI（37254718） | 含 retinopathy／foot **screening 接受率**（OR），不含轉介完成 | 各 RCT 分母不一，very low 確定性 | 部分：screening 本身即被介入 | PMC10233616 L24、L80 📄 |
| Albekery／Chu／SCREAM／DR cascade | 觀察性：測試比例、轉介比例、治療起始比例 | 各自分母（有適應症者、新發現 albuminuria 者等） | 無介入 | 見 report §6 |

結論：**我手上沒有任何成人 T2D 的隨機試驗，以「異常後處置完成」且以全部隨機人數為分母作為主要結局。** 唯一接近的 ACCESS 為青少年（8–21 歲，T1D＋T2D；PMC10784572 L19），follow-through 為次要結局且分母不一致。methods_ai 提出的 18/82 應更正為 **18/83**（PMC10784572 L51；control n=83，22% 與 18/83 吻合）。

### 1.2 問題 B：CARRS 是否把 care coordinator 與 EHR CDS 分開分析？ → **ACCEPT：沒有**

- 全文自述 “we were unable to examine the relative effectiveness of individual intervention components”（PMC6561084 L117 📄）。2024 長期追蹤（PMC11198027）同樣以整體策略分析，另以「站點是否持續」分層，不是以元件分層 📄。
- 因此 CARRS（RR 2.24；HbA1c −0.50 pp）**不能作為 CDS／AI 單獨效益**。

### 1.3 補充：可作為 CDS 單獨代理的間接證據（會影響綜合結論，→ **REVISE 建議**）

- Cochrane QI 的 **clinician reminders（紙本或電子提示，最接近 CDS 提示）** 單獨對 HbA1c（≤8.3% 者 +0.09，−0.02 到 +0.20；>8.3% 者 −0.09，−0.34 到 +0.15）、SBP、LDL 的 95% CrI 全部跨 0；retinopathy screening OR 1.10（0.70–2.09），foot screening OR 1.30（0.71–2.57），確定性 very low／low（PMC10233616 L80 附近 “Summary of findings 5” 📄）。對照下，case management 對 HbA1c 在基準>8.3% 時 −0.27（−0.39 到 −0.15）（同檔 “Summary of findings 1”，L24 附近 📄）。
- 解讀界線：Cochrane 的 CR 是「提示臨床人員」的泛稱，不等同於 LLM 或預測型 CDS；網絡後設回歸為間接比較。但足以支持：**「僅提醒醫師」沒有可辨識的獨立效益；有效元件集中在 case management／team changes／教育／自我管理。** 綜合結論若寫「AI／CDS 提升整合照護」，應限定為「與人力協調綑綁時」。

---

## 2. 回覆 psychosocial §C

### 2.1 問題：哪些併發症事件之後，有直接證據顯示憂鬱／DD／認知惡化？縱向或橫斷？ → **REVISE（證據有，但按器官不均、多為診斷碼定義的憂鬱）；DD 縱向證據 UNRESOLVED**

新檢索（見 `search_log.md` 第 E 節）。**全部以「事件前無憂鬱」之縱向設計為準；橫斷或方向相反者另列。**

| 併發症事件 | 對隨後心理／認知結局的直接證據 | 設計 | 判斷 |
| --- | --- | --- | --- |
| 任一併發症（T2D） | 出現或發生任一併發症後，憂鬱／焦慮 HR 1.77（1.73–1.80）；amputation HR 2.16（2.01–2.31，最強）；retinopathy HR 1.13（1.09–1.17，最弱）；每類併發症皆上升（Horsbøl 2024，PMID 38157285，N=265,799，丹麥登記，事件前無憂鬱／焦慮）📌 | **縱向、前瞻登記** | 有直接證據；結局為醫院接觸／處方定義的憂鬱／焦慮，**不是 DD、不是量表** |
| 任一併發症（彙整） | 併發症→憂鬱 HR 1.14（1.07–1.21），僅 2 項研究、>230,000 人；方向相反（憂鬱→併發症）HR 1.38／1.33，9 項研究（Nouwen 2019，PMID 31215077）📌 | 縱向 SR／MA | 雙向；正向「併發症→憂鬱」證據薄，且作者標示 risk of bias 升高 |
| 心血管事件（MI、stroke、PAD、HF） | Zareini 2024（PMID 37815600，N=165,096）：CVD 事件後 5 年內憂鬱發生率高（例：MI＋T2D 131.1、stroke＋T2D 287.4、HF＋T2D 244.3／1000 PY）；T2D 相對無 T2D 的 IRR：MI 1.29（1.23–1.35）、PAD 1.18、stroke 1.09、HF 1.05 📄（PMC11493809 L19）。Pan 2012（PMID 22850257，老年，N=144,216）：CVD 後憂鬱 HR 1.13（1.04–1.23）📌 | 縱向登記 | Zareini 比的是「T2D vs 非 T2D」，不是「事件 vs 無事件」；只能說 CVD 事件後憂鬱發生率高，且 T2D 放大 |
| 下肢截肢／足潰瘍 | 截肢後憂鬱／焦慮 HR 2.16（Horsbøl）📌；Pan：LEA HR 1.25（0.95–1.65，**不顯著**）📌；首次 DFU 病人基線 DSM-IV 憂鬱 32.2%，且憂鬱者 5 年死亡 HR 2.09（1.34–3.25）（Winkley 2012，PMID 22057196）📌——**橫斷盛行率＋反向預後**；截肢術前焦慮與癒合不良相關，憂鬱非死亡獨立預測（Pedras 2022，PMID 33100065）📌 | 混合 | 「截肢→憂鬱」有登記縱向證據（Horsbøl）；足潰瘍本身→憂鬱無縱向證據 → `UNRESOLVED` |
| 視網膜病變／視力喪失 | Horsbøl：retinopathy HR 1.13（1.09–1.17）📌（最弱）；**視力喪失本身→DD／憂鬱的縱向證據未檢出** | 縱向（僅診斷） | 診斷有弱關聯；「視力喪失」→ `UNRESOLVED` |
| 腎病變／eGFR G4／透析 | Horsbøl 含 nephropathy（分項 HR 未在 abstract）📌；**透析或 G4 後的 DD／憂鬱縱向研究未檢出**（檢索 B-E4 只得無關的 beta-blocker 研究） | — | `UNRESOLVED` |
| 嚴重低血糖 | → **失智**：mid-life HR 2.85（1.72–4.72）、late-life HR 2.38（1.83–3.11）（Alkabbani 2023，PMID 36516080，N≈445,000）📌；Taiwan 軌跡研究 sHR 1.22／1.25（Li 2022，PMID 33678721，N=677,618）📄（PMC9359896 L19）。→ **憂鬱／DD**：未檢出縱向 | 縱向 | 認知（失智）有縱向證據；憂鬱／DD `UNRESOLVED` |

**對 ADA 通則 vs 分器官規則的含義（供 psychosocial 判斷）：**
- 縱向證據支持「併發症發生後心理風險升高」的通則（Horsbøl，N 大），但**各器官強度不同（amputation 2.16 vs retinopathy 1.13）**，且證據主要是「診斷碼／處方定義的憂鬱／焦慮」，沒有 DD 量表層級的縱向資料。
- 若要寫成「某器官事件後必須在 X 週內重評」，**沒有任何研究驗證重評時間點或其效益**；那是設計假設，不是證據。

### 2.2 問題：ADA Table 5.7（DD、憂鬱與微血管併發症 +++）是相關性證據評級，有無相衝突的個別研究？ → **REVISE（有可引用的不一致，但沒有直接推翻）**

1. **方向與強度：** Nouwen 2019 彙整顯示「憂鬱→併發症」HR 1.33–1.38（9 項研究）遠比「併發症→憂鬱」HR 1.14（2 項研究）有證據，且後者 risk of bias 高 📌——表中若寫成雙向，須註明不對稱。
2. **特定情境的陰性結果：** 有潰瘍史者，憂鬱與潰瘍復發無關（HR 0.88，0.61–1.27；Westby 2020，PMID 32315474）📌；截肢後憂鬱非死亡的獨立預測因子（Pedras 2022）📌；截肢術前焦慮而非憂鬱與癒合相關。
3. **以微血管為主的證據較弱於大血管：** UK Biobank T2D：MDD→HF HR 1.32、ASCVD 1.17、微血管 1.29（Li 2025，PMID 39720611）📄（PMC11665660 L20）；Pan 2012 在老年中 LEA 不顯著 → 微血管「+++」不能直接推到每一器官。
4. **混雜風險：** 上述皆為觀察性；Horsbøl 以登記接觸定義，偵測偏差（有併發症者就醫多）可能放大 HR。

### 2.3 我先前 handoff 向 psychosocial 提出的問題，我現在可自行回答（INDEPENDENT）→ **以此取代 handoff §B 第三題**

INDEPENDENT 全文 Table 2（PMID32809002_INDEPENDENT.md L387–L407 📄）：
- 24 個月複合主要結局 71.6% vs **54.7%**，RD 16.9（8.5–25.2）——與正文 L149 一致；**abstract 的 57.4% 為與 Table 2／正文／RD 不符的離群值**（L20 vs L149、L387）。
- 成分（24 個月）：SCL-20 ≥50% 改善 77.7% vs 63.6%，RD 14.1（6.7–21.6）；HbA1c ≥0.5 pp 下降 51.9% vs 43.2%，RD 8.7（−0.9 到 18.4，**NS**）；SBP ≥5 mmHg 下降 RD 0.3（−9.6 到 10.2）；LDL ≥10 mg/dL 下降 RD −2.5（−12.3 到 7.2）；平均 HbA1c 8.7 vs 8.6，差 0.0（−0.3 到 0.4）。
- 「overall」（含 12 與 24 個月的 GEE，post hoc）HbA1c ≥0.5 pp RD 14.4（7.1–21.7）、HbA1c <7% 或下降的聯合 RD 12.1（5.0–19.2）有顯著，**但 24 個月的心代謝成分全部不顯著**。
- **含義：** 「身心共同改善」在 INDEPENDENT 主要由憂鬱成分驅動；24 個月心代謝成分無一獨立達顯著（介入 12 個月後停止）。→ `docs/03` L8 與 `docs/12` 的措辭應降為「憂鬱改善明確；心代謝指標改善在 24 個月不能獨立確認」。
- TEAMcare（PMC3312811 L97）：僅報告合併模型與四項非校正差值（HbA1c 0.58 pp、LDL 6.9、SBP 5.1、SCL-20 0.40）📄，**未提供各成分達成率**；TEAMcare 的心代謝改善為 12 個月內，較 INDEPENDENT 強，兩者不能互相替代。

---

## 3. 對 calculators（無對應檔案）→ **UNRESOLVED**

`sessions/calculators/` 僅有 `search_log.md`；`calculators/dmic_calculators/` 無 DCSI／aDCSI 模組。我 handoff 中的三項（aDCSI 13 點對照表、Taiwan C-index 0.760／0.794／0.781 作為外部參考、缺 UACR 時不得代入 0）尚無可核對實作。KFRE 缺值處理可看 `calculators/dmic_calculators/ckd.py`，但此題屬 calculators 的 crosscheck，我未審查其實作。

---

## 4. crosscheck 後修訂（對原 `report.md`；原文未重寫）

見 `report.md` 末尾「## 10. crosscheck 後修訂」。重點：
1. ADDITION 10 年、J-DOIT3、INDEPENDENT 由 abstract-only 升為全文 grep 驗證；Steno-2 兩篇仍為 no_fulltext（被權限層拒絕）。
2. INDEPENDENT 的 57.4% 為 abstract 離群值；24 個月心代謝成分不顯著 → 原 report §5.1 該列與 §0 第 2 點相關文字須同步降級。
3. J-DOIT3 全文新增資訊：腎病變發生／進展 HR 0.68（0.56–0.82），視網膜病變發生／進展 HR 0.86（0.74–1.00, p=0.046），無任何一組喪失視力，無 ESRD 作為首發事件，且預先設定的基線校正分析 HR 0.76（0.59–0.99, p=0.042）——**主要終點未達顯著，但中間／微血管次要終點偏向有益**，原 report 只寫了陰性。
4. 新增 11 筆證據（E41–E51）→ `evidence_table.csv`。
