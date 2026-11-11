"""Unified result structure and strict input helpers (stdlib only)."""
from __future__ import annotations

import math
from typing import Any, Dict, List, Optional

KINDS = (
    "disease_burden",
    "organ_function",
    "stratification",
    "risk_estimate",
    "symptom_score",
    "screening_index",
)


def result(
    tool: str,
    version: str,
    value: Any,
    units: Optional[str],
    population_ok: Optional[bool],
    reasons_unavailable: Optional[List[str]],
    inputs_used: Dict[str, Any],
    source: str,
    kind: str,
    **details: Any,
) -> Dict[str, Any]:
    """Build the unified dict. ``value`` must be None whenever reasons exist."""
    reasons = list(reasons_unavailable or [])
    if reasons:
        value = None
    assert kind in KINDS, kind
    det = {"kind": kind}
    det.update(details)
    return {
        "tool": tool,
        "version": version,
        "value": value,
        "units": units,
        "population_ok": population_ok,
        "reasons_unavailable": reasons,
        "inputs_used": dict(inputs_used),
        "source": source,
        "details": det,
    }


def is_number(x: Any) -> bool:
    return (
        isinstance(x, (int, float))
        and not isinstance(x, bool)
        and math.isfinite(x)
    )


def need_number(name: str, x: Any, reasons: List[str], positive: bool = False,
                minimum: Optional[float] = None, maximum: Optional[float] = None) -> Optional[float]:
    """Return float(x) if valid, else None and append a reason (no imputation)."""
    if x is None:
        reasons.append("missing:%s" % name)
        return None
    if not is_number(x):
        reasons.append("invalid_type:%s" % name)
        return None
    if positive and x <= 0:
        reasons.append("non_positive:%s" % name)
        return None
    if minimum is not None and x < minimum:
        reasons.append("below_minimum:%s<%s" % (name, minimum))
        return None
    if maximum is not None and x > maximum:
        reasons.append("above_maximum:%s>%s" % (name, maximum))
        return None
    return float(x)


def need_sex(x: Any, reasons: List[str]) -> Optional[str]:
    """Return 'male'/'female' or None (+reason). No default sex."""
    if x is None:
        reasons.append("missing:sex")
        return None
    if isinstance(x, str):
        s = x.strip().lower()
        if s in ("m", "male"):
            return "male"
        if s in ("f", "female"):
            return "female"
    reasons.append("invalid_value:sex")
    return None
