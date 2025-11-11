---
pretty_name: Bayaan Alignment (v1.2)
language:
  - ar
  - en
license: cc-by-4.0
tags:
  - arabic
  - bilingual
  - logic
  - code
  - hybrid-language
  - evaluation
  - alignment
  - education
task_categories:
  - text-generation
size_categories:
  - 1K<n<10K
---

# Bayaan Alignment Dataset (v1.2) — مجموعة التوافق لِـ «بيان»

Bilingual Arabic–English alignment dataset for the Bayaan hybrid programming language.
- 9 domains (social, physical, mixed, transport, health, education, work, market, public)
- 1000 examples (train=800, val=100, test=100)
- Balanced languages: 50% Arabic, 50% English
- JSONL schema with natural text, Bayaan code, logic explanation, entities/actions/states
- License: CC BY 4.0

روابط مهمة:
- GitHub: https://github.com/mubtakir/bayaan-lang
- Eval Framework (CLI + metrics): https://github.com/mubtakir/bayaan-lang/tree/main/eval_framework
- Detailed metrics JSON (v1.2): https://raw.githubusercontent.com/mubtakir/bayaan-lang/main/eval_framework/results/metrics_v1.2_detailed.json
- Hugging Face Space (demo): https://huggingface.co/spaces/Mubtakir/bayaan-demo

## Quickstart — البداية السريعة

```python
from datasets import load_dataset

# Load dataset
# Arabic+English bilingual JSONL with 9 domains, v1.2 (1000 rows)
ds = load_dataset("Mubtakir/bayaan-alignment-sample")
print(ds)
print(ds["train"][0])

# Filter by language
ar_train = [x for x in ds["train"] if x.get("lang") == "ar"]
print("Arabic train examples:", len(ar_train))
```

## Schema — البنية

Each JSONL line follows this schema:
```json
{
  "id": "ex001",
  "lang": "ar | en",
  "natural_text": "...",
  "bayan_code": "محمد.تقديم_وجبة(أحمد); أحمد.امتنان += 0.3",
  "logic_explanation": "...",
  "entities": ["محمد", "أحمد"],
  "actions": ["تقديم_وجبة"],
  "states": ["امتنان"],
  "split": "train | validation | test"
}
```

Notes:
- bayan_code uses semicolons as statement separators; our evaluator normalizes them to newlines.
- `+=` / `-=` are normalized to standard assignments for parser compatibility.

## Domains & Weights — المجالات والأوزان

Default domain distribution used to generate v1.2:
- social=0.30, physical=0.20, mixed=0.20, transport=0.10, health=0.08, education=0.05, work=0.04, market=0.02, public=0.01

You can customize weights when re-generating locally with the generator script:
```bash
python datasets/alignment/generate_dataset.py --total 1000 --seed 42 \
  --weights 'social=0.30 physical=0.20 mixed=0.20 transport=0.10 health=0.08 education=0.05 work=0.04 market=0.02 public=0.01'
```

## Splits — التقسيمات

Dynamic 80/10/10 split based on dataset size (N):
- train = 0.8N, validation = 0.1N, test = 0.1N

## Reproducible Generation — توليد قابل للإعادة

Generator supports sharding and safe appends:
- `--start-index`, `--append`
- `--dedup-on-append` to skip duplicate IDs when appending
- `--resume-auto` to continue from last ID automatically

Examples:
```bash
# Shard 1
python datasets/alignment/generate_dataset.py --total 1000 --seed 42 --start-index 1 --out-jsonl data.jsonl

# Resume/append safely
python datasets/alignment/generate_dataset.py --total 1000 --seed 44 --out-jsonl data.jsonl --resume-auto --dedup-on-append
```

## Evaluation — التقييم

Run dataset-quality metrics locally:
```bash
python -m eval_framework.cli \
  --dataset datasets/alignment/sample_social_interactions.jsonl \
  --pretty --out eval_framework/results/metrics_local.json
```

Filter and dump failing cases:
```bash
python -m eval_framework.cli \
  --dataset datasets/alignment/sample_social_interactions.jsonl \
  --lang-filter ar --split-filter train \
  --dump-fail eval_framework/results/failing_ids.jsonl --dump-mode ids
```

## Citation — الاستشهاد
If you use this dataset, please cite the repository.

## License — الرخصة
CC BY 4.0. You may use, share, and adapt with attribution.

