#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate a 500-line bilingual alignment dataset for Bayan.
- Primary: JSONL (one object per line)
- Mirror: CSV
- Deterministic generation with seed=42

Schema per line:
{id, lang, natural_text, bayan_code, logic_explanation, entities, actions, states, split}

Splits: train (1..400), val (401..450), test (451..500)
"""
from __future__ import annotations
import argparse
import csv
import json
import random
from dataclasses import dataclass
from pathlib import Path

random.seed(42)

OUT_DIR = Path(__file__).parent
JSONL_PATH = OUT_DIR / "sample_social_interactions.jsonl"
CSV_PATH = OUT_DIR / "sample_social_interactions.csv"
# Dynamic total for splits (set by gen_examples)
N_TOTAL = 500


# Pools
AR_NAMES = [
    "أحمد", "محمد", "خالد", "سارة", "مريم", "ليلى", "يوسف", "نور", "علي", "فاطمة",
]
EN_NAMES = [
    "Ahmed", "Mohammed", "Khaled", "Sarah", "Maryam", "Layla", "Youssef", "Noor", "Ali", "Fatimah",
]

# Social actions/states (expanded)
AR_SOCIAL_ACTIONS = [
    ("تقديم_وجبة", "الطعام يقلل الجوع ويزيد الامتنان", [("جوع", -0.4), ("امتنان", +0.3)]),
    ("مواساة", "المواساة تقلل الحزن", [("حزن", -0.3)]),
    ("تشجيع", "التشجيع يرفع الثقة", [("ثقة", +0.25)]),
    ("نصح", "النصح بالهدوء يحسن التركيز", [("تركيز", +0.2)]),
    ("اعتذار", "الاعتذار يقلل الغضب ويزيد الثقة قليلًا", [("غضب", -0.2), ("ثقة", +0.1)]),
    ("تهنئة", "التهنئة ترفع السعادة", [("سعادة", +0.2)]),
    ("إرشاد", "الإرشاد يحسن الثقة", [("ثقة", +0.15)]),
    ("توجيه", "التوجيه يحسن التركيز", [("تركيز", +0.15)]),
    ("مساعدة", "المساعدة تقلل التوتر وتزيد الامتنان", [("توتر", -0.2), ("امتنان", +0.2)]),
    ("اعتناء", "الاعتناء يرفع الراحة ويقلل الخوف", [("راحة", +0.2), ("خوف", -0.1)]),
    ("شكوى", "الشكوى ترفع الغضب وتقلل الثقة", [("غضب", +0.2), ("ثقة", -0.1)]),
    ("طمأنة", "الطمأنة تقلل الخوف", [("خوف", -0.25)]),
]
EN_SOCIAL_ACTIONS = [
    ("serve_meal", "Serving food reduces hunger and increases gratitude", [("hunger", -0.4), ("gratitude", +0.3)]),
    ("comfort", "Comforting reduces sadness", [("sadness", -0.3)]),
    ("encourage", "Encouragement increases trust", [("trust", +0.25)]),
    ("advise", "Advice to stay calm improves focus", [("focus", +0.2)]),
    ("apologize", "Apology reduces anger and slightly increases trust", [("anger", -0.2), ("trust", +0.1)]),
    ("congratulate", "Congratulations increase happiness", [("happiness", +0.2)]),
    ("guide", "Guidance improves trust", [("trust", +0.15)]),
    ("direct", "Direction improves focus", [("focus", +0.15)]),
    ("assist", "Assistance reduces stress and increases gratitude", [("stress", -0.2), ("gratitude", +0.2)]),
    ("care_for", "Care increases comfort and reduces fear", [("comfort", +0.2), ("fear", -0.1)]),
    ("complain", "Complaint increases anger and reduces trust", [("anger", +0.2), ("trust", -0.1)]),
    ("reassure", "Reassurance reduces fear", [("fear", -0.25)]),
]

# Physical actions/states
AR_PHYS_ACTIONS = [
    ("دفع", "الدفع يزيد السرعة وفق القوة والكتلة", [("سرعة", +0.2), ("طاقة", -0.05)]),
    ("سحب", "السحب يغير السرعة وقد يقلل الطاقة", [("سرعة", +0.1), ("طاقة", -0.05)]),
    ("تسخين", "التسخين يرفع الحرارة", [("حرارة", +0.3), ("طاقة", -0.05)]),
    ("تبريد", "التبريد يخفض الحرارة", [("حرارة", -0.3)]),
    ("تسريع", "التسريع يرفع السرعة", [("سرعة", +0.25)]),
]
EN_PHYS_ACTIONS = [
    ("push", "Pushing increases speed based on force and mass", [("speed", +0.2), ("energy", -0.05)]),
    ("pull", "Pulling changes speed and may reduce energy", [("speed", +0.1), ("energy", -0.05)]),
    ("heat", "Heating raises temperature", [("temperature", +0.3), ("energy", -0.05)]),
    ("cool", "Cooling lowers temperature", [("temperature", -0.3)]),
    ("accelerate", "Acceleration raises speed", [("speed", +0.25)]),
    ("brake", "Braking reduces speed", [("speed", -0.25)]),
]

# Transport domain actions
AR_TRANSPORT_ACTIONS = [
    ("ركوب_حافلة", "الركوب يقلل الطاقة قليلاً", [("طاقة", -0.1)]),
    ("قيادة_سيارة", "القيادة تتطلب تركيزًا وتستهلك طاقة", [("تركيز", +0.2), ("طاقة", -0.15)]),
    ("انتظار_مترو", "الانتظار قد يزيد الملل", [("ملل", +0.2)]),
    ("تفادي_ازدحام", "تفادي الازدحام يقلل التوتر", [("توتر", -0.15)]),
]
EN_TRANSPORT_ACTIONS = [
    ("board_bus", "Boarding slightly reduces energy", [("energy", -0.1)]),
    ("drive_car", "Driving requires focus and consumes energy", [("focus", +0.2), ("energy", -0.15)]),
    ("wait_metro", "Waiting may increase boredom", [("boredom", +0.2)]),
    ("avoid_traffic", "Avoiding traffic reduces stress", [("stress", -0.15)]),
]

# Health/Emergency domain actions
AR_HEALTH_ACTIONS = [
    ("إسعافات_أولية", "الإسعافات تقلل الخوف وترفع الراحة", [("خوف", -0.2), ("راحة", +0.2)]),
    ("صرف_دواء", "صرف الدواء يقلل الألم", [("ألم", -0.3)]),
    ("قياس_ضغط", "القياس يعطي طمأنينة", [("طمأنينة", +0.2)]),
    ("اتصال_إسعاف", "الاتصال يرفع الأمان ويقلل التوتر", [("أمان", +0.2), ("توتر", -0.15)]),
]
EN_HEALTH_ACTIONS = [
    ("first_aid", "First aid reduces fear and increases comfort", [("fear", -0.2), ("comfort", +0.2)]),
    ("dispense_med", "Dispensing medicine reduces pain", [("pain", -0.3)]),
    ("measure_bp", "Measuring blood pressure provides reassurance", [("reassurance", +0.2)]),
    ("call_ambulance", "Calling ambulance increases safety and reduces stress", [("safety", +0.2), ("stress", -0.15)]),
]

# Education domain actions
AR_EDU_ACTIONS = [
    ("شرح_درس", "الشرح يحسن الفهم", [("فهم", +0.25)]),
    ("مراجعة", "المراجعة تزيد الثقة وتقلل التوتر", [("ثقة", +0.15), ("توتر", -0.1)]),
    ("تعاون_طلابي", "التعاون يرفع التعاون والثقة", [("تعاون", +0.2), ("ثقة", +0.1)]),
    ("حل_واجب", "حل الواجب يحسن المهارة", [("مهارة", +0.2)]),
]
EN_EDU_ACTIONS = [
    ("explain_lesson", "Explanation improves understanding", [("understanding", +0.25)]),
    ("review", "Review increases confidence and reduces stress", [("confidence", +0.15), ("stress", -0.1)]),
    ("student_collab", "Collaboration raises teamwork and trust", [("teamwork", +0.2), ("trust", +0.1)]),
    ("do_homework", "Homework improves skill", [("skill", +0.2)]),
]

# Work domain actions
AR_WORK_ACTIONS = [
    ("تغذية_راجعة", "التغذية الراجعة تقلل التوتر وتزيد التحسن", [("توتر", -0.1), ("تحسن", +0.2)]),
    ("تفويض_مهمة", "التفويض يرفع المسؤولية", [("مسؤولية", +0.2)]),
    ("اجتماع", "الاجتماع يحسن التنسيق ويستهلك طاقة", [("تنسيق", +0.2), ("طاقة", -0.1)]),
    ("تخطيط", "التخطيط يرفع الوضوح", [("وضوح", +0.25)]),
]
EN_WORK_ACTIONS = [
    ("feedback", "Feedback reduces stress and increases improvement", [("stress", -0.1), ("improvement", +0.2)]),
    ("delegate_task", "Delegation increases responsibility", [("responsibility", +0.2)]),
    ("meeting", "Meeting improves coordination and uses energy", [("coordination", +0.2), ("energy", -0.1)]),
    ("planning", "Planning increases clarity", [("clarity", +0.25)]),
]

# Market/Service domain actions
AR_MARKET_ACTIONS = [
    ("إرجاع_منتج", "الإرجاع يرفع الرضا والثقة", [("رضا", +0.2), ("ثقة", +0.1)]),
    ("استبدال", "الاستبدال يرفع الرضا", [("رضا", +0.2)]),
    ("تفاوض", "التفاوض قد يرفع الثقة", [("ثقة", +0.05)]),
    ("خدمة_سيئة", "الخدمة السيئة ترفع الغضب وتقلل الثقة", [("غضب", +0.25), ("ثقة", -0.2)]),
]
EN_MARKET_ACTIONS = [
    ("return_item", "Return increases satisfaction and trust", [("satisfaction", +0.2), ("trust", +0.1)]),
    ("exchange_item", "Exchange increases satisfaction", [("satisfaction", +0.2)]),
    ("negotiate", "Negotiation may increase trust", [("trust", +0.05)]),
    ("bad_service", "Bad service increases anger and reduces trust", [("anger", +0.25), ("trust", -0.2)]),
]

# Public spaces domain actions
AR_PUBLIC_ACTIONS = [
    ("حجز_طاولة", "الحجز يرفع الرضا", [("رضا", +0.15)]),
    ("اصطفاف", "الاصطفاف قد يزيد الملل ويرفع الصبر", [("ملل", +0.1), ("صبر", +0.1)]),
    ("استعارة_كتاب", "الاستعارة ترفع المعرفة", [("معرفة", +0.2)]),
    ("تنظيف_مكان", "التنظيف يرفع الراحة", [("راحة", +0.2)]),
]
EN_PUBLIC_ACTIONS = [
    ("book_table", "Booking a table increases satisfaction", [("satisfaction", +0.15)]),
    ("queue", "Queuing may increase boredom and patience", [("boredom", +0.1), ("patience", +0.1)]),
    ("borrow_book", "Borrowing a book increases knowledge", [("knowledge", +0.2)]),
    ("clean_area", "Cleaning increases comfort", [("comfort", +0.2)]),
]

AR_PHYS_ENTITIES = ["كرة", "جسم", "ماء", "صندوق", "سيارة", "كرة_معدنية"]
EN_PHYS_ENTITIES = ["Ball", "Object", "Water", "Box", "Car", "MetalBall"]

# Mixed templates (social cause -> physical or performance effect)
AR_MIXED = [
    ("مدرب", "عدّاء", "تشجيع", "سرعة", +0.2, "التشجيع يرفع سرعة العدّاء"),
    ("معلّم", "طالب", "نصح", "تركيز", +0.2, "النصح يحسن تركيز الطالب"),
    ("طبيب", "مريض", "طمأنة", "خوف", -0.25, "الطمأنة تقلل الخوف"),
]
EN_MIXED = [
    ("Coach", "Runner", "encourage", "speed", +0.2, "Encouragement increases runner speed"),
    ("Teacher", "Student", "advise", "focus", +0.2, "Advice improves student focus"),
    ("Doctor", "Patient", "reassure", "fear", -0.25, "Reassurance reduces fear"),
]

CONTEXTS_AR = ["في المدرسة", "في المستشفى", "في السوق", "في البيت", "في العمل", "في الحديقة", "في المترو", "في الحافلة"]
CONTEXTS_EN = ["at school", "at the hospital", "at the market", "at home", "at work", "in the park", "in the metro", "on the bus"]

@dataclass
class Example:
    id: str
    lang: str
    natural_text: str
    bayan_code: str
    logic_explanation: str
    entities: list[str]
    actions: list[str]
    states: list[str]
    split: str


def make_id(i: int) -> str:
    return f"ex{i:03d}"


def split_for(i: int) -> str:
    # Dynamic 80/10/10 split based on N_TOTAL
    train_cut = int(0.8 * N_TOTAL)
    val_cut = int(0.9 * N_TOTAL)
    if i <= train_cut:
        return "train"
    elif i <= val_cut:
        return "val"
    return "test"


def clip_delta(x: float) -> float:
    # Keep magnitudes reasonable
    return round(max(-1.0, min(1.0, x)), 3)


def ar_social_example(i: int) -> Example:
    a, b = random.sample(AR_NAMES, 2)
    action, rationale, effects = random.choice(AR_SOCIAL_ACTIONS)
    # Pick one context
    ctx = random.choice(CONTEXTS_AR)
    # Build natural text
    nt = f"{a} {ctx} يقوم بفعل '{action}' مع {b}"
    # Build code/effects
    stmts = [f"{a}.{action}({b})"]
    states = []
    for st, delta in effects:
        op = "+=" if delta > 0 else "-="
        stmts.append(f"{b}.{st} {op} {abs(clip_delta(delta))}")
        states.append(st)
    code = "; ".join(stmts)
    return Example(
        id=make_id(i),
        lang="ar",
        natural_text=nt,
        bayan_code=code,
        logic_explanation=rationale,
        entities=[a, b],
        actions=[action],
        states=states,
        split=split_for(i),
    )


def en_social_example(i: int) -> Example:
    a, b = random.sample(EN_NAMES, 2)
    action, rationale, effects = random.choice(EN_SOCIAL_ACTIONS)
    ctx = random.choice(CONTEXTS_EN)
    nt = f"{a} {ctx} performs '{action}' with {b}"
    stmts = [f"{a}.{action}({b})"]
    states = []
    for st, delta in effects:
        op = "+=" if delta > 0 else "-="
        stmts.append(f"{b}.{st} {op} {abs(clip_delta(delta))}")
        states.append(st)
    code = "; ".join(stmts)
    return Example(
        id=make_id(i),
        lang="en",
        natural_text=nt,
        bayan_code=code,
        logic_explanation=rationale,
        entities=[a, b],
        actions=[action],
        states=states,
        split=split_for(i),
    )
# Generic pair-based generators for domains that involve person-to-person actions

def ar_pair_example(i: int, actions_pool: list[tuple[str, str, list[tuple[str, float]]]]) -> Example:
    a, b = random.sample(AR_NAMES, 2)
    action, rationale, effects = random.choice(actions_pool)
    ctx = random.choice(CONTEXTS_AR)
    nt = f"{a} {ctx} يقوم بفعل '{action}' مع {b}"
    stmts: list[str] = [f"{a}.{action}({b})"]
    states: list[str] = []
    for st, delta in effects:
        op = "+=" if delta > 0 else "-="
        stmts.append(f"{b}.{st} {op} {abs(clip_delta(delta))}")
        states.append(st)
    code = "; ".join(stmts)
    return Example(
        id=make_id(i),
        lang="ar",
        natural_text=nt,
        bayan_code=code,
        logic_explanation=rationale,
        entities=[a, b],
        actions=[action],
        states=states,
        split=split_for(i),
    )


def en_pair_example(i: int, actions_pool: list[tuple[str, str, list[tuple[str, float]]]]) -> Example:
    a, b = random.sample(EN_NAMES, 2)
    action, rationale, effects = random.choice(actions_pool)
    ctx = random.choice(CONTEXTS_EN)
    nt = f"{a} {ctx} performs '{action}' with {b}"
    stmts: list[str] = [f"{a}.{action}({b})"]
    states: list[str] = []
    for st, delta in effects:
        op = "+=" if delta > 0 else "-="
        stmts.append(f"{b}.{st} {op} {abs(clip_delta(delta))}")
        states.append(st)
    code = "; ".join(stmts)
    return Example(
        id=make_id(i),
        lang="en",
        natural_text=nt,
        bayan_code=code,
        logic_explanation=rationale,
        entities=[a, b],
        actions=[action],
        states=states,
        split=split_for(i),
    )


# Wrappers per new domain

def ar_transport_example(i: int) -> Example:
    return ar_pair_example(i, AR_TRANSPORT_ACTIONS)

def en_transport_example(i: int) -> Example:
    return en_pair_example(i, EN_TRANSPORT_ACTIONS)

def ar_health_example(i: int) -> Example:
    return ar_pair_example(i, AR_HEALTH_ACTIONS)

def en_health_example(i: int) -> Example:
    return en_pair_example(i, EN_HEALTH_ACTIONS)

def ar_education_example(i: int) -> Example:
    return ar_pair_example(i, AR_EDU_ACTIONS)

def en_education_example(i: int) -> Example:
    return en_pair_example(i, EN_EDU_ACTIONS)

def ar_work_example(i: int) -> Example:
    return ar_pair_example(i, AR_WORK_ACTIONS)

def en_work_example(i: int) -> Example:
    return en_pair_example(i, EN_WORK_ACTIONS)

def ar_market_example(i: int) -> Example:
    return ar_pair_example(i, AR_MARKET_ACTIONS)

def en_market_example(i: int) -> Example:
    return en_pair_example(i, EN_MARKET_ACTIONS)

def ar_public_example(i: int) -> Example:
    return ar_pair_example(i, AR_PUBLIC_ACTIONS)

def en_public_example(i: int) -> Example:
    return en_pair_example(i, EN_PUBLIC_ACTIONS)



def ar_physical_example(i: int) -> Example:
    obj = random.choice(AR_PHYS_ENTITIES)
    action, rationale, effects = random.choice(AR_PHYS_ACTIONS)
    ctx = random.choice(CONTEXTS_AR)
    nt = f"{ctx}: {action} على {obj}"
    stmts = [f"{obj}.{action}()"]
    states = []
    for st, delta in effects:
        op = "+=" if delta > 0 else "-="
        stmts.append(f"{obj}.{st} {op} {abs(clip_delta(delta))}")
        states.append(st)
    code = "; ".join(stmts)
    return Example(
        id=make_id(i),
        lang="ar",
        natural_text=nt,
        bayan_code=code,
        logic_explanation=rationale,
        entities=[obj],
        actions=[action],
        states=states,
        split=split_for(i),
    )


def en_physical_example(i: int) -> Example:
    obj = random.choice(EN_PHYS_ENTITIES)
    action, rationale, effects = random.choice(EN_PHYS_ACTIONS)
    ctx = random.choice(CONTEXTS_EN)
    nt = f"{ctx}: {action} on {obj}"
    stmts = [f"{obj}.{action}()"]
    states = []
    for st, delta in effects:
        op = "+=" if delta > 0 else "-="
        stmts.append(f"{obj}.{st} {op} {abs(clip_delta(delta))}")
        states.append(st)
    code = "; ".join(stmts)
    return Example(
        id=make_id(i),
        lang="en",
        natural_text=nt,
        bayan_code=code,
        logic_explanation=rationale,
        entities=[obj],
        actions=[action],
        states=states,
        split=split_for(i),
    )


def ar_mixed_example(i: int) -> Example:
    a, b, action, st, delta, rationale = random.choice(AR_MIXED)
    ctx = random.choice(CONTEXTS_AR)
    nt = f"{ctx}: {a} يقوم بـ{action} لـ {b}"
    stmts = [f"{a}.{action}({b})", f"{b}.{st} {'+=' if delta>0 else '-='} {abs(clip_delta(delta))}"]
    code = "; ".join(stmts)
    return Example(
        id=make_id(i),
        lang="ar",
        natural_text=nt,
        bayan_code=code,
        logic_explanation=rationale,
        entities=[a, b],
        actions=[action],
        states=[st],
        split=split_for(i),
    )


def en_mixed_example(i: int) -> Example:
    a, b, action, st, delta, rationale = random.choice(EN_MIXED)
    ctx = random.choice(CONTEXTS_EN)
    nt = f"{ctx}: {a} performs {action} for {b}"
    stmts = [f"{a}.{action}({b})", f"{b}.{st} {'+=' if delta>0 else '-='} {abs(clip_delta(delta))}"]
    code = "; ".join(stmts)
    return Example(
        id=make_id(i),
        lang="en",
        natural_text=nt,
        bayan_code=code,
        logic_explanation=rationale,
        entities=[a, b],
        actions=[action],
        states=[st],
        split=split_for(i),
    )


def gen_examples(n: int = 500, weights_str: str | None = None, start_index: int = 1) -> list[Example]:
    """Generate examples with weighted domain distribution and 50/50 AR/EN balance.

    start_index allows sharded generation with correct ids/splits.
    """
    global N_TOTAL
    N_TOTAL = (start_index - 1) + n

    # Allowed domains and default weights
    domains = [
        "social", "physical", "mixed",
        "transport", "health", "education", "work", "market", "public",
    ]
    default_weights = {
        "social": 0.30,
        "physical": 0.20,
        "mixed": 0.20,
        "transport": 0.10,
        "health": 0.08,
        "education": 0.05,
        "work": 0.04,
        "market": 0.02,
        "public": 0.01,
    }

    def parse_weights(s: str | None) -> dict[str, float]:
        if not s:
            return default_weights.copy()
        weights = default_weights.copy()
        for tok in s.replace(",", " ").split():
            if "=" in tok:
                k, v = tok.split("=", 1)
                k = k.strip().lower()
                try:
                    val = float(v)
                except ValueError:
                    continue
                if k in weights:
                    weights[k] = max(0.0, val)
        total = sum(weights.values())
        if total <= 0:
            return default_weights.copy()
        for k in list(weights.keys()):
            weights[k] = weights[k] / total
        return weights

    weights = parse_weights(weights_str)

    def pick_domain() -> str:
        r = random.random()
        cum = 0.0
        last = domains[-1]
        for k in domains:
            cum += weights.get(k, 0.0)
            if r <= cum:
                return k
        return last

    gens = {
        "social": {"ar": ar_social_example, "en": en_social_example},
        "physical": {"ar": ar_physical_example, "en": en_physical_example},
        "mixed": {"ar": ar_mixed_example, "en": en_mixed_example},
        "transport": {"ar": ar_transport_example, "en": en_transport_example},
        "health": {"ar": ar_health_example, "en": en_health_example},
        "education": {"ar": ar_education_example, "en": en_education_example},
        "work": {"ar": ar_work_example, "en": en_work_example},
        "market": {"ar": ar_market_example, "en": en_market_example},
        "public": {"ar": ar_public_example, "en": en_public_example},
    }

    examples: list[Example] = []
    for i in range(start_index, start_index + n):
        d = pick_domain()
        lang = "ar" if (i % 2 == 1) else "en"
        ex = gens[d][lang](i)
        examples.append(ex)

    # Sort by id for stable splits
    examples.sort(key=lambda e: e.id)
    return examples


def write_jsonl(examples: list[Example], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        for ex in examples:
            obj = {
                "id": ex.id,
                "lang": ex.lang,
                "natural_text": ex.natural_text,
                "bayan_code": ex.bayan_code,
                "logic_explanation": ex.logic_explanation,
                "entities": ex.entities,
                "actions": ex.actions,
                "states": ex.states,
                "split": ex.split,
            }
            f.write(json.dumps(obj, ensure_ascii=False) + "\n")


def _read_existing_ids(path: Path) -> set[str]:
    ids: set[str] = set()
    if not path.exists():
        return ids
    try:
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                    rid = obj.get("id")
                    if isinstance(rid, str):
                        ids.add(rid)
                except Exception:
                    continue
    except FileNotFoundError:
        return ids
    return ids


def append_jsonl(examples: list[Example], path: Path, dedup: bool = False) -> tuple[int, int]:
    """Append examples to JSONL. If dedup=True, skip examples whose id already exists.
    Returns (written, skipped)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    existing: set[str] = _read_existing_ids(path) if dedup else set()
    written = 0
    skipped = 0
    with path.open("a", encoding="utf-8", newline="\n") as f:
        for ex in examples:
            if dedup and ex.id in existing:
                skipped += 1
                continue
            obj = {
                "id": ex.id,
                "lang": ex.lang,
                "natural_text": ex.natural_text,
                "bayan_code": ex.bayan_code,
                "logic_explanation": ex.logic_explanation,
                "entities": ex.entities,
                "actions": ex.actions,
                "states": ex.states,
                "split": ex.split,
            }
            f.write(json.dumps(obj, ensure_ascii=False) + "\n")
            written += 1
            if dedup:
                existing.add(ex.id)
    return written, skipped


def write_csv(examples: list[Example], path: Path) -> None:
    header = [
        "natural_text",
        "bayan_code",
        "logic_explanation",
        "lang",
        "entities",
        "actions",
        "states",
        "split",
        "id",
    ]
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        for ex in examples:
            w.writerow([
                ex.natural_text,
                ex.bayan_code,
                ex.logic_explanation,
                ex.lang,
                json.dumps(ex.entities, ensure_ascii=False),
                json.dumps(ex.actions, ensure_ascii=False),
                json.dumps(ex.states, ensure_ascii=False),
                ex.split,
                ex.id,
            ])


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Bayan alignment dataset (JSONL+CSV)")
    parser.add_argument("--total", type=int, default=500, help="Total number of examples (default: 500)")
    parser.add_argument("--seed", type=int, default=42, help="RNG seed (default: 42)")
    parser.add_argument("--weights", type=str, default="", help="Domain weights, e.g. 'social=0.35 physical=0.25 transport=0.1' or comma-separated")
    parser.add_argument("--start-index", type=int, default=1, help="1-based starting id index for sharding (default: 1)")
    parser.add_argument("--out-jsonl", type=str, default="", help="Optional output JSONL path (default: datasets/alignment/sample_social_interactions.jsonl)")
    parser.add_argument("--out-csv", type=str, default="", help="Optional output CSV path (default: datasets/alignment/sample_social_interactions.csv)")
    parser.add_argument("--append", action="store_true", help="Append to JSONL (skip CSV) for sharded generation")
    parser.add_argument("--dedup-on-append", action="store_true", help="When used with --append, skip examples whose id already exists in the output JSONL")
    args = parser.parse_args()

    random.seed(args.seed)

    out_jsonl = Path(args.out_jsonl) if args.out_jsonl else JSONL_PATH
    out_csv = Path(args.out_csv) if args.out_csv else CSV_PATH
    out_jsonl.parent.mkdir(parents=True, exist_ok=True)

    examples = gen_examples(args.total, args.weights, start_index=args.start_index)

    if args.append:
        written, skipped = append_jsonl(examples, out_jsonl, dedup=args.dedup_on_append)
        print(f"Appended: {written} written, {skipped} skipped (dedup={'on' if args.dedup_on_append else 'off'}) -> {out_jsonl}")
    else:
        write_jsonl(examples, out_jsonl)
        write_csv(examples, out_csv)
        # Quick validation
        assert out_jsonl.exists() and out_csv.exists()
        with out_jsonl.open("r", encoding="utf-8") as f:
            cnt = sum(1 for _ in f)
        assert cnt == args.total, f"Expected {args.total} lines, got {cnt}"
        print("Generated:", out_jsonl, out_csv, "(total=", args.total, ")")


if __name__ == "__main__":
    main()

