# Eval Framework

Initial utilities (PR #3):
- syntax_checker.py — parse Bayan code to validate syntax (no execution)
- logic_validator.py — heuristic logical checks on entities/actions/states
- metrics.py — dataset quality metrics and optional prediction metrics
- cli.py — command-line entry point to compute metrics

## Install/Run
Project vendors the Bayan interpreter; no extra deps required.

Examples:

1) Dataset-only metrics (v1.2, 1000 ex):
```
python -m eval_framework.cli \
  --dataset datasets/alignment/sample_social_interactions.jsonl \
  --pretty
```

2) With predictions (JSONL aligned by `id`, each with `bayan_code`):
```
python -m eval_framework.cli \
  --dataset datasets/alignment/sample_social_interactions.jsonl \
  --pred eval_framework/examples/predictions.sample.jsonl \
  --out metrics.json --pretty
```

3) Filters (optional):
- By language: `--lang-filter ar` أو `--lang-filter en` أو `--lang-filter ar,en`
- By split: `--split-filter train` أو `--split-filter val,test`
```
python -m eval_framework.cli \
  --dataset datasets/alignment/sample_social_interactions.jsonl \
  --lang-filter ar --split-filter train --pretty
```

4) Baseline: echo reference (generates predictions identical to reference)
```
python -m eval_framework.baselines.echo_ref \
  --dataset datasets/alignment/sample_social_interactions.jsonl \
  --out eval_framework/examples/predictions.sample.jsonl
```

## Predictions format (JSONL)
One object per line with at least:
- `id`: string matching a reference example id
- `bayan_code`: model-generated or proposed Bayan snippet

Sample file (3 lines):
- eval_framework/examples/predictions.sample.jsonl

## Reported Metrics
- syntax_valid_rate: Fraction of snippets whose Bayan syntax parses
- logic.entities_ok_rate: `entities[]` tokens appear in bayan_code
- logic.actions_ok_rate: `actions[]` appear in bayan_code (method calls)
- logic.states_ok_rate: `states[]` appear in updates (+=, -=, or =)
- logic.no_contradiction_rate: same state not both increased and decreased
- logic.all_pass_rate: all four checks pass simultaneously

If predictions are provided:
- action_suggestion_precision: Micro-precision of predicted actions vs reference actions
- state_coverage_rate: Fraction of reference states updated in predicted code (proxy)
- causal_coverage: Alias of state_coverage_rate for now

## Notes
- Syntax check uses HybridLexer/HybridParser but does not interpret/execute
- Logic checks are string/regex-based and language-agnostic (AR/EN)
- IDs must align between reference and predictions for prediction metrics

