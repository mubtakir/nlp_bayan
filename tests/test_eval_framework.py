#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io, json, tempfile, os
from pathlib import Path

from eval_framework.syntax_checker import check_syntax
from eval_framework.logic_validator import validate_example
from eval_framework.metrics import load_jsonl, dataset_quality_metrics, prediction_metrics


def make_jsonl(tmp: Path, rows):
    p = tmp / "tmp.jsonl"
    with p.open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    return p


def test_syntax_and_logic_and_metrics_minimal():
    rows = [
        {
            "id": "ex001",
            "lang": "ar",
            "natural_text": "أحمد ينصح خالد في المدرسة",
            "bayan_code": "أحمد.نصح(خالد); خالد.تركيز += 0.2",
            "logic_explanation": "النصح يحسن التركيز",
            "entities": ["أحمد", "خالد"],
            "actions": ["نصح"],
            "states": ["تركيز"],
            "split": "train",
        },
        {
            "id": "ex002",
            "lang": "en",
            "natural_text": "Ahmed complains to Khaled at work",
            "bayan_code": "Ahmed.complain(Khaled); Khaled.trust -= 0.1",
            "logic_explanation": "complaint can reduce trust",
            "entities": ["Ahmed", "Khaled"],
            "actions": ["complain"],
            "states": ["trust"],
            "split": "val",
        },
        {
            "id": "ex003",
            "lang": "en",
            "natural_text": "A neutral line with no updates",
            "bayan_code": "Mohammed.guide(Ahmed)",
            "logic_explanation": "guidance",
            "entities": ["Mohammed", "Ahmed"],
            "actions": ["guide"],
            "states": [],
            "split": "test",
        },
    ]

    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        p = make_jsonl(tdp, rows)
        data = load_jsonl(str(p))

        # Syntax check on first row
        assert check_syntax(rows[0]["bayan_code"]).ok

        # Logic validation
        chk = validate_example(rows[0])
        assert chk.entities_ok and chk.actions_ok and chk.states_ok and chk.no_contradiction

        # Dataset metrics
        m = dataset_quality_metrics(data)
        assert m["counts"]["total"] == 3
        assert 0.6 <= m["syntax_valid_rate"] <= 1.0
        assert m["logic"]["all_pass_rate"] >= 0.33

        # Prediction metrics: craft a simple pred
        preds = [
            {"id": "ex001", "bayan_code": "أحمد.نصح(خالد); خالد.تركيز += 0.1"},
            {"id": "ex002", "bayan_code": "Ahmed.complain(Khaled); Khaled.trust -= 0.05"},
            {"id": "ex003", "bayan_code": "Mohammed.guide(Ahmed)"},
        ]
        pp = make_jsonl(tdp, preds)
        mm = prediction_metrics(data, load_jsonl(str(pp)))
        assert mm["pairs"] == 3
        assert 0.66 <= mm["action_suggestion_precision"] <= 1.0
        assert 0.3 <= mm["state_coverage_rate"] <= 1.0

