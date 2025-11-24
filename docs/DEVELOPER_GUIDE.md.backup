# nlp_bayan Developer Guide and Project Reference

This document records the recent conventions, changes, utilities, and how to work with this repository so future developers can continue smoothly.


## Quick Links
- Roadmap: [docs/ROADMAP.md](./ROADMAP.md)
- Changelog: [CHANGELOG.md](../CHANGELOG.md)
- Root README: [README.md](../README.md)


## Sync to external repo (mubtakir/nlp_bayan)
We added a GitHub Actions workflow to mirror only the `nlp_bayan/` subtree to a separate repository.
- Workflow file: `.github/workflows/sync-nlp-bayan.yml`
- Trigger: on push to main affecting `nlp_bayan/**` (or run manually via workflow_dispatch)
- Destination: `github.com/mubtakir/nlp_bayan` → branch `main`

Setup required once by the repository owner:
1) Create a fine-grained Personal Access Token limited to `mubtakir/nlp_bayan` with `contents: read/write` only.
2) Add it as a Repository Secret here: Settings → Secrets and variables → Actions → New repository secret
   - Name: `NLP_BAYAN_PUSH_TOKEN`
   - Value: the token
3) Push changes touching `nlp_bayan/**` or run the workflow manually. The action will split the subtree and force-push it to the external repo.

Notes:
- The secret is masked in GitHub Actions logs. Do NOT paste tokens in issues/PRs or plaintext.
- To include additional paths (e.g., selected docs) in the external repo, we can change from `subtree split` to a packaging step that copies specific folders before pushing.

## Contents
- Overview and goals
- English-only identifiers policy (scoped to nlp_bayan)
- Linter and pre-commit hook
- CI workflow (GitHub Actions)
- Integrated Knowledge Base (integrated_kb)
- Demos and how to run
- Tests and how to run
- Recommendations and future work
- Troubleshooting

---

## Overview and goals
- Build a logical NLP model on top of the Bayan hybrid language (traditional + logical).
- Keep Bayan and nlp_bayan co-located and integrated (the language benefits from the model and vice versa).
- Ensure consistency and portability by enforcing English-only programming identifiers inside nlp_bayan, while allowing data in any language (Arabic/English, etc.).

Key additions made:
- English-only identifiers policy enforced for nlp_bayan via a linter.
- Git pre-commit hook to run the linter only for staged Bayan files inside nlp_bayan.
- GitHub Actions workflow to run the linter and the test suite on pushes/PRs.
- Enriched integrated knowledge base with a selective loading API.
- Examples updated to load integrated knowledge when needed.
- Added tests validating selective loading behavior.

---

## English-only identifiers policy (scoped to nlp_bayan)
- Scope: Only applies to the nlp_bayan module. This keeps our model universal without preventing others from coding in Arabic in unrelated parts of the repo.
- Enforced on: programming identifiers (predicate/function/class/variable names) via token types IDENTIFIER and VARIABLE.
- Allowed: Any language in string literals (data values), numbers, and comments.

Manual run of the linter:
- Command: `python scripts/bayan_lint_identifiers.py nlp_bayan`
- Output example: `OK: 23 file(s) checked; no violations found.`

Internals:
- Uses Bayan's HybridLexer to tokenize and flag Arabic code points in IDENTIFIER/VARIABLE tokens only.
- Path: `scripts/bayan_lint_identifiers.py`

---

## Pre-commit hook (local developer workflow)
- Path: `.githooks/pre-commit`
- Behavior: Runs the Bayan identifier linter on staged `.bayan`/`.by` files under `nlp_bayan/` only.
- Activation (one-time per repo clone):
  1) `git config core.hooksPath .githooks`
  2) `chmod +x .githooks/pre-commit`

Hook excerpt:

```bash
# Only staged files under nlp_bayan ending with .bayan/.by
changed_files=$(git diff --cached --name-only --diff-filter=ACM | \
  grep -E '^nlp_bayan/.*\.(bayan|by)$' || true)
```

Notes:
- If no staged Bayan files under `nlp_bayan`, the hook exits quickly.
- If violations exist, the commit is blocked with a clear report of (file:line:col).

---

## CI workflow (GitHub Actions)
- Path: `.github/workflows/lint-and-test.yml`
- What it does:
  - Checks out the code.
  - Sets up Python 3.11.
  - Installs `pytest`.
  - Runs the linter on `nlp_bayan` only.
  - Runs the test suite.
- Triggers: push and pull_request, filtered to relevant paths (nlp_bayan, scripts, bayan, tests, workflows).

Workflow excerpt:

```yaml
- name: Run Bayan identifier linter (scoped to nlp_bayan)
  run: python scripts/bayan_lint_identifiers.py nlp_bayan
```

---

## Integrated Knowledge Base (integrated_kb)
- Path: `nlp_bayan/core/integrated_kb.bayan`
- Provides consolidated facts/rules and helper functions to inject them into any logical engine.
- Functions:
  - `load_into(target_logical)`: copies all predicates/facts/rules into the target logical engine.
  - `load_selective(target_logical, only)`: NEW. Allows loading specific knowledge domains only.

Supported domains (initial set):
- prob → `prob`, `threshold`, `maybe`, `likely`
- information → `information`, `information_equation`
- family → `parent`, `grandparent`, `ancestor`
- events → `event`, `sequential_events`
- shapes → `shape_equation`, `extract_shape_equation`

Usage examples inside a Bayan file:

```bayan
import nlp_bayan.core.integrated_kb as kb
hybrid {
    kb.load_into(logical)
}
```

```bayan
import nlp_bayan.core.integrated_kb as kb
hybrid {
    kb.load_selective(logical, ["prob", "family"])
}
```

Notes and next steps:
- `load_selective` is a pragmatic step toward fully modular KB files; later, we can split into topic-specific `.bayan` modules and compose them.

---

## Demos and how to run
- Demo: `nlp_bayan/examples/demo_generation.bayan`
  - Updated to load integrated knowledge base to produce richer query results.

Run any `.bayan` file:
- `python scripts/bayan_run.py nlp_bayan/examples/demo_generation.bayan`

Excerpt:

```bayan
import nlp_bayan.core.integrated_kb as kb
hybrid { kb.load_into(logical) }
```

---

## Tests and how to run
- Added: `tests/test_integrated_kb_selective.py`
  - Verifies that `load_selective` loads only the requested domains.

Run tests locally:
- `python -m pytest -q`

Excerpt from the test:

```python
def test_kb_load_selective_prob_only():
    code = """
    import nlp_bayan.core.integrated_kb as kb
    hybrid { kb.load_selective(logical, ["prob"]) }
    """
    intr = run(code)
    kb = intr.logical.knowledge_base
    assert "prob" in kb and "parent" not in kb
```

---

## Recommendations and future work
- When we begin building the actual language model, remember: Bayan provides built-in AI/NLP libraries—leverage them where useful.
- Consider splitting the integrated KB into separate modules (e.g., `prob_kb.bayan`, `family_kb.bayan`, etc.) and provide a composite loader.
- Expand tests to cover more nlp_bayan modules and end-to-end flows.

---

## Troubleshooting
- Pre-commit not firing:
  - Ensure `git config core.hooksPath .githooks` and `chmod +x .githooks/pre-commit` were run.
- Linter flags Arabic in code:
  - Ensure Arabic content is inside string literals (data), not in identifiers.
- CI failures:
  - Check the Action logs; re-run locally with the same commands (`python scripts/bayan_lint_identifiers.py nlp_bayan` and `pytest`).

---

## Quick reference (commands)
- Run linter on nlp_bayan: `python scripts/bayan_lint_identifiers.py nlp_bayan`
- Enable pre-commit hook: `git config core.hooksPath .githooks && chmod +x .githooks/pre-commit`
- Run a Bayan demo: `python scripts/bayan_run.py path/to/file.bayan`
- Run tests: `python -m pytest -q`

