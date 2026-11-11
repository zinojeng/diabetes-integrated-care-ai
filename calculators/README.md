# dmic_calculators

研究用 Python 實作（**不是**已部署的臨床系統，也**不是**已驗證的醫療器材）。

- 只實作「係數／公式能在本地全文、附錄或官方文件 grep 到」的工具；其餘在 `registry.py` 標 `spec_only` 並寫明缺什麼。
- 缺值、單位不明、非正值、超出適用族群 → `value=None` 並在 `reasons_unavailable` 說明；**絕不靜默代入**。
- 統一輸出：`{tool, version, value, units, population_ok, reasons_unavailable, inputs_used, source, details}`。
  `details.kind` 區分 `disease_burden / organ_function / stratification / risk_estimate / symptom_score / screening_index`。
- 不提供、也不應該建立跨模型「全人風險總分」。
- 測試：`python3 -m unittest discover -s tests/calculators`（Python ≥3.9，純 stdlib）。
- 出處與逐項證據等級：`sessions/calculators/report.md`、`evidence_table.csv`。
