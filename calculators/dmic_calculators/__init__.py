"""dmic_calculators: research-only calculator implementations with strict missing-data handling.

Not a deployed clinical system. Each function returns the unified dict
{tool, version, value, units, population_ok, reasons_unavailable, inputs_used, source, details}.
No cross-model 'whole-person risk score' exists or should be built from these outputs.
"""
__version__ = "0.1.0"
from . import ckd, comorbidity, cvd, foot, liver, recode, registry, result, scales, staging  # noqa: F401
