#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Baseline predictor: echo reference bayan_code.

Usage:
  python -m eval_framework.baselines.echo_ref --dataset datasets/alignment/sample_social_interactions.jsonl \
    --out eval_framework/examples/predictions.sample.jsonl
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_jsonl(path: str | Path) -> list[dict]:
    path = Path(path)
    rows: list[dict] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def main() -> None:
    ap = argparse.ArgumentParser(description="Echo reference bayan_code as predictions")
    ap.add_argument("--dataset", required=True, help="Path to reference dataset JSONL")
    ap.add_argument("--out", required=True, help="Where to write predictions JSONL")
    args = ap.parse_args()

    ref = load_jsonl(args.dataset)
    outp = Path(args.out)
    outp.parent.mkdir(parents=True, exist_ok=True)

    with outp.open("w", encoding="utf-8", newline="\n") as f:
        for r in ref:
            obj = {"id": r.get("id"), "bayan_code": r.get("bayan_code", "")}
            f.write(json.dumps(obj, ensure_ascii=False) + "\n")

    print(f"Wrote {len(ref)} predictions -> {outp}")


if __name__ == "__main__":
    main()

