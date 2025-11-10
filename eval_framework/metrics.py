#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evaluation metrics for Bayan datasets and (optionally) model predictions.

Two modes:
1) Dataset quality metrics (no predictions):
   - syntax_valid_rate (Bayan parser only, no execution)
   - logic checks (entities/actions/states presence; no_contradiction; all_pass_rate)
   - counts by language and split

2) Prediction metrics (optional, ref + pred):
   - action_suggestion_precision (micro-precision of predicted actions vs reference actions)
   - state_coverage_rate (aka causal_coverage proxy): fraction of reference states that are updated in predicted code

Predictions JSONL should align by id with reference and contain at least `id` and `bayan_code`.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional
import json
import re
from collections import Counter

from .syntax_checker import check_syntax
from .logic_validator import validate_example


# -- Utilities -----------------------------------------------------------------

def load_jsonl(path: str) -> List[Dict]:
    items: List[Dict] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            items.append(json.loads(line))
    return items


CALL_RE = re.compile(r"([\w\u0600-\u06FF]+)\.([\w\u0600-\u06FF]+)\s*\(")
ASSIGN_POS_RE = re.compile(r"([\w\u0600-\u06FF]+)\s*\+=")
ASSIGN_NEG_RE = re.compile(r"([\w\u0600-\u06FF]+)\s*-=")
ASSIGN_EQ_RE = re.compile(r"([\w\u0600-\u06FF]+)\s*=(?!=)")  # '=' but not '=='


def extract_actions(code: str) -> List[str]:
    return [m.group(2) for m in CALL_RE.finditer(code or "")]


def extract_states(code: str) -> Tuple[set, set, set]:
    code = code or ""
    pos = {m.group(1) for m in ASSIGN_POS_RE.finditer(code)}
    neg = {m.group(1) for m in ASSIGN_NEG_RE.finditer(code)}
    eq = {m.group(1) for m in ASSIGN_EQ_RE.finditer(code)}
    return pos, neg, eq


# -- Dataset-only metrics -------------------------------------------------------

def dataset_quality_metrics(examples: List[Dict]) -> Dict:
    n = len(examples)
    langs = Counter(e.get("lang", "?") for e in examples)
    splits = Counter(e.get("split", "?") for e in examples)

    # Syntax
    ok_syntax = 0
    for e in examples:
        code = e.get("bayan_code", "")
        res = check_syntax(code)
        ok_syntax += 1 if res.ok else 0

    # Logic checks
    ent_ok = act_ok = st_ok = no_ctr = all_ok = 0
    for e in examples:
        chk = validate_example(e)
        ent_ok += 1 if chk.entities_ok else 0
        act_ok += 1 if chk.actions_ok else 0
        st_ok += 1 if chk.states_ok else 0
        no_ctr += 1 if chk.no_contradiction else 0
        if chk.entities_ok and chk.actions_ok and chk.states_ok and chk.no_contradiction:
            all_ok += 1

    def rate(x: int) -> float:
        return round(x / n, 4) if n else 0.0

    return {
        "counts": {"total": n, **dict(langs), **{f"split_{k}": v for k, v in splits.items()}},
        "syntax_valid_rate": rate(ok_syntax),
        "logic": {
            "entities_ok_rate": rate(ent_ok),
            "actions_ok_rate": rate(act_ok),
            "states_ok_rate": rate(st_ok),
            "no_contradiction_rate": rate(no_ctr),
            "all_pass_rate": rate(all_ok),
        },
    }


# -- Prediction metrics ---------------------------------------------------------

def align_by_id(ref: List[Dict], pred: List[Dict]) -> List[Tuple[Dict, Dict]]:
    m = {e.get("id"): e for e in pred}
    out: List[Tuple[Dict, Dict]] = []
    for r in ref:
        rid = r.get("id")
        if rid in m:
            out.append((r, m[rid]))
    return out


def prediction_metrics(ref: List[Dict], pred: List[Dict]) -> Dict:
    pairs = align_by_id(ref, pred)
    if not pairs:
        return {"pairs": 0}

    # Action micro-precision
    num_pred_actions = 0
    num_correct_actions = 0

    # State coverage (proxy for causal coverage)
    covered_states = 0
    total_ref_states = 0

    for r, p in pairs:
        ref_actions = set(r.get("actions", []) or [])
        pred_actions = extract_actions(p.get("bayan_code", ""))
        num_pred_actions += len(pred_actions)
        num_correct_actions += sum(1 for a in pred_actions if a in ref_actions)

        ref_states = set(r.get("states", []) or [])
        pos, neg, eq = extract_states(p.get("bayan_code", ""))
        pred_states = pos | neg | eq
        covered_states += len(ref_states & pred_states)
        total_ref_states += len(ref_states)

    action_precision = (num_correct_actions / num_pred_actions) if num_pred_actions else 0.0
    state_cov = (covered_states / total_ref_states) if total_ref_states else 0.0

    return {
        "pairs": len(pairs),
        "action_suggestion_precision": round(action_precision, 4),
        "state_coverage_rate": round(state_cov, 4),
        "causal_coverage": round(state_cov, 4),  # alias
    }


__all__ = [
    "load_jsonl",
    "dataset_quality_metrics",
    "prediction_metrics",
    "extract_actions",
    "extract_states",
]

