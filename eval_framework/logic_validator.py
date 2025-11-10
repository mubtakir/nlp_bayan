#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lightweight logical consistency validator for dataset examples.
Heuristic (non-executing) checks:
- Entities listed appear in bayan_code text
- Actions listed appear in bayan_code text
- States listed appear in bayan_code updates (+= or -= or direct assignment)
- No direct contradiction: same state updated in both directions in one example
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple
import re


@dataclass
class LogicChecks:
    entities_ok: bool
    actions_ok: bool
    states_ok: bool
    no_contradiction: bool


POS_UPDATE = re.compile(r"(?P<state>[\w\u0600-\u06FF]+)\s*\+=\s*")
NEG_UPDATE = re.compile(r"(?P<state>[\w\u0600-\u06FF]+)\s*-=\s*")
EQ_UPDATE = re.compile(r"(?P<state>[\w\u0600-\u06FF]+)\s*=(?!=)\s*")  # '=' but not '=='


def _contains_all(text: str, tokens: List[str]) -> bool:
    return all(t in text for t in tokens)


def _states_updates(text: str) -> Tuple[set, set, set]:
    """Return states seen in "+=", "-=" and any single "=" direct assignments."""
    pos = set(m.group("state") for m in POS_UPDATE.finditer(text))
    neg = set(m.group("state") for m in NEG_UPDATE.finditer(text))
    eq = set(m.group("state") for m in EQ_UPDATE.finditer(text))
    return pos, neg, eq


def validate_example(example: Dict) -> LogicChecks:
    code = example.get("bayan_code", "") or ""
    entities = example.get("entities", []) or []
    actions = example.get("actions", []) or []
    states = example.get("states", []) or []

    entities_ok = _contains_all(code, entities)
    actions_ok = _contains_all(code, actions)

    pos, neg, eq = _states_updates(code)
    # A state is considered present if it appears in any of pos/neg/eq
    states_present = {s for s in states if (s in pos or s in neg or s in eq)}
    states_ok = len(states_present) == len(states)

    # Contradiction: same state both increased and decreased in same snippet
    contradictory = any((s in pos and s in neg) for s in (pos | neg))
    no_contradiction = not contradictory

    return LogicChecks(
        entities_ok=entities_ok,
        actions_ok=actions_ok,
        states_ok=states_ok,
        no_contradiction=no_contradiction,
    )


__all__ = ["LogicChecks", "validate_example"]
