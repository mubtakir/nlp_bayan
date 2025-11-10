#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CLI for evaluating Bayan datasets and optional predictions.

Usage:
  python -m eval_framework.cli --dataset datasets/alignment/sample_social_interactions.jsonl
  python -m eval_framework.cli --dataset <ref.jsonl> --pred <pred.jsonl> --out metrics.json --pretty
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from .metrics import load_jsonl, dataset_quality_metrics, prediction_metrics


def main() -> None:
    ap = argparse.ArgumentParser(description="Evaluate Bayan dataset and optional predictions")
    ap.add_argument("--dataset", required=True, help="Path to reference dataset JSONL")
    ap.add_argument("--pred", default="", help="Optional path to predictions JSONL (with id,bayan_code)")
    ap.add_argument("--out", default="", help="Optional path to write metrics JSON")
    ap.add_argument("--pretty", action="store_true", help="Pretty-print JSON")
    args = ap.parse_args()

    ref = load_jsonl(args.dataset)
    out = {
        "dataset_metrics": dataset_quality_metrics(ref)
    }

    if args.pred:
        pred = load_jsonl(args.pred)
        out["prediction_metrics"] = prediction_metrics(ref, pred)

    text = json.dumps(out, ensure_ascii=False, indent=2 if args.pretty else None)
    if args.out:
        Path(args.out).write_text(text + ("\n" if not text.endswith("\n") else ""), encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

