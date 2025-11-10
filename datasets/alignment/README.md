# Alignment Dataset (Social/Physical Interactions)

Primary format: JSONL (one JSON object per line)
Optional: CSV mirror of the same content
Encoding: UTF-8 (no BOM)
License: CC BY 4.0 (Attribution required)

## JSONL schema
Each line follows:

- id: string (e.g., "ex001")
- lang: "ar" | "en"
- natural_text: string (short description in the given language)
- bayan_code: string (concise Bayaan code: actions and effects)
- logic_explanation: string (1-line rationale)
- entities: array of strings
- actions: array of strings
- states: array of strings (affected states)
- split: "train" | "val" | "test"

Example (AR):
```
{"id":"ex001","lang":"ar","natural_text":"محمد قدم وجبة لأحمد","bayan_code":"محمد.تقديم_وجبة(أحمد); أحمد.امتنان += 0.3","logic_explanation":"تقديم الطعام يزيد الامتنان","entities":["محمد","أحمد"],"actions":["تقديم_وجبة"],"states":["امتنان"],"split":"train"}
```

Example (EN):
```
{"id":"ex002","lang":"en","natural_text":"Mohammed serves a meal to Ahmed","bayan_code":"Mohammed.serve_meal(Ahmed); Ahmed.gratitude += 0.3","logic_explanation":"Food offering increases gratitude","entities":["Mohammed","Ahmed"],"actions":["serve_meal"],"states":["gratitude"],"split":"train"}
```

## Splits
- Dynamic: 80% train, 10% val, 10% test (by index after sorting)
- Example (n=1000): train=800, val=100, test=100

## CLI
- Generate dataset:
  - `python datasets/alignment/generate_dataset.py --total 1000 --seed 42 --weights 'social=0.30 physical=0.20 mixed=0.20 transport=0.10 health=0.08 education=0.05 work=0.04 market=0.02 public=0.01'`
- Supported domains: social, physical, mixed, transport, health, education, work, market, public

- Sharded/append mode (optional, لا يغيّر السلوك الافتراضي):
  - `--start-index` لتحديد بداية الترقيم (1-based)
  - `--out-jsonl` مسار ملف JSONL مخصص، و`--out-csv` لمسار CSV
  - `--append` لضم النتائج إلى JSONL بدلاً من الاستبدال (CSV يُتجاوز في هذه الحالة)

أمثلة:
- shard 1 (ex001..ex1000):
  - `python datasets/alignment/generate_dataset.py --total 1000 --seed 42 --start-index 1 --out-jsonl data_sharded.jsonl`
- shard 2 (ex1001..ex2000) مع إضافة:
  - `python datasets/alignment/generate_dataset.py --total 1000 --seed 43 --start-index 1001 --out-jsonl data_sharded.jsonl --append`

## Notes
- Keep numbers in [0,1] when modeling fuzzy states
- Prefer short, concrete sentences
- Actions and states should be consistent with Bayaan's entity system style
- CSV mirror uses columns:
  - natural_text,bayan_code,logic_explanation,lang,entities,actions,states,split,id
- Arrays are serialized as JSON strings inside CSV cells

