# Claude：Calculator 公式與風險查核

查 DCSI/aDCSI、CCI、CKD-EPI2021、4-variable KFRE、FIB-4、SCORE2-Diabetes、RECODe、UKPDS、PREVENT、WATCH-DM、低血糖工具。
對每個列輸入、單位、缺值、適用/排除、端點、時間窗、development/validation、校準、公式來源與授權。
KFRE 必查 JAMA2016 eAppendix2 PDF p9 的 LP 與 Original/NA/non-NA baseline survival。
DCSI 上限13，neuropathy最高1；PAID1995與現行版不同；WHO5方向與缺值須注意。
心理工具 PHQ9/GAD7/DDS17/PAID20/WHO5 列 scoring 与 clinical response，不把症狀篩檢轉成未來器官風險。
未逐項查到 SCORE2/RECODe 等完整 coefficients 就標 spec_only，不生成看似可用的估計數字。
與 methods_ai 交叉核對 KFRE、與 psychosocial 交叉核對量表。
