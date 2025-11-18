# Logic in Bayan Language (7): Advanced Entities and Participation Ratios

> In this part we focus on a fundamental idea in the entity engine:
> **Almost everything has a ratio**:
> - For state (degree 0..1).
> - For property or value.
> - For action strength.
> - And for the extent of each entity's participation in the action (**sensitivity**).
>
> These ratios allow Bayan to represent a rich world: one person is affected 0.7 by the action, another 0.3, and so on.

## 1. Ratio Levels in the Entity Engine

Simply put, we have:

- **State degree**: like `"happiness": 0.6` or `"hunger": 0.3` (fuzzy 0..1).
- **Action strength**: the `"strength"` field in the action definition inside the entity.
- **Action value**: the `action_value` parameter passed to `apply` / `perform`.
- **Target sensitivity**: `sensitivity`, comes from the **participation ratio** of each entity.

Inside the effect formula you can use:

- `value` → current value of the state.
- `action_value` → passed action value.
- `power` → action strength.
- `sensitivity` → participation/sensitivity ratio of this target.

## 2. The «perform» Function and Participants with Ratios

The global function:

- English: `perform(action_name, participants, states=None, properties=None, action_value=1.0)`

**Participants format** can be:

- List of strings: `[
  "Ahmad.1.0",   # full participation
  "Ali:0.5"      # medium participation
]`
- Or list of tuples: `[ ("Ahmad", 1.0), ("Ali", 0.5) ]`.
- Or dictionary: `{ "Ahmad": 1.0, "Ali": 0.5 }`.

### 2.1 Example: Ahmad and Ali Move with Different Ratios

```bayan
hybrid {
    entity Ahmad {
        "properties": {"x": {"type": "numeric", "value": 0.0}},
        "actions": {"go": {"effects": [
            {"on": "x", "formula": "value + 3*sensitivity"}
        ]}}
    }

    entity Ali {
        "properties": {"x": {"type": "numeric", "value": 1.0}}
    }

    perform("go", ["Ahmad.1.0", "Ali.0.5"], action_value=1.0)
}
```

- Ahmad participates with ratio 1.0 → his `x` increases by a larger amount.
- Ali participates with ratio 0.5 → the change for him is about half of Ahmad's (according to the formula).

We can define an English interface to read properties:

```bayan
hybrid {
    entity_property(?entity, ?key, ?value) :- property(?entity, ?key, ?value).
}
query entity_property("Ahmad", "x", ?ahmad_position)?
query entity_property("Ali", "x", ?ali_position)?
```

## 3. Groups and Pronouns: Applying Action to a Group with Ratios

You can define a **group** of entities then refer to it in participants:

```bayan
hybrid {
    entity Ahmad { "properties": {"x": {"type": "numeric", "value": 0.0}},
                "actions": {"go": {"effects": [
                    {"on": "x", "formula": "value + 2*sensitivity"}
                ]}} }

    entity Ali   { "properties": {"x": {"type": "numeric", "value": 1.0}} }

    define_group("team", ["Ahmad", "Ali"])

    perform("go", ["group:team.0.5"])  # applies to all group members
    perform("go", ["they.0.2"])        # pronoun reference to last used group
}
```

- `"group:team.0.5"` means: apply the action to all group members with sensitivity ratio 0.5 for each member.
- `"they.0.2"` (or similar pronoun) reuses the last participant group with a new ratio.

## 4. Reactions: When an Entity Receives an Action with a Certain Ratio

Besides «actions» there are **reactions**, which is the way
**an entity responds when a certain action is applied to it**:

```bayan
hybrid {
    entity Ahmad {
        "states": {"happiness": 0.5},
        "reactions": {
            "serve_meal": {
                "sensitivity": 0.7,
                "response": "happiness += sensitivity*0.3"
            }
        }
    }

    entity restaurant {
        "actions": {"serve_meal": {"effects": []}}
    }

    perform("serve_meal", ["restaurant.1.0", "Ahmad.1.0"], action_value=1.0)
}
```

- When Ahmad is a target of the `serve_meal` action:
  - His sensitivity `0.7` is used in the reaction.
  - `happiness` increases by approximately `0.7 * 0.3 = 0.21` (according to the formula).

## 5. Complete Example: A Lesson Affects Focus and Fatigue of Two Students with Different Ratios

```bayan
hybrid {
    entity student1 {
        "states": {"focus": 0.6, "fatigue": 0.2},
        "actions": {
            "study": {
                "strength": 1.0,
                "effects": [
                    {"on": "focus", "formula": "clamp(value + power*0.2*sensitivity, 0, 1)"},
                    {"on": "fatigue", "formula": "clamp(value + power*0.3*sensitivity, 0, 1)"}
                ]
            }
        }
    }

    entity student2 {
        "states": {"focus": 0.3, "fatigue": 0.4}
    }

    perform("study", ["student1.1.0", "student2.0.5"], action_value=1.0)
}

hybrid {
    entity_state(?e, ?k, ?v) :- state(?e, ?k, ?v).
}
query entity_state("student1", "focus", ?focus1)?
query entity_state("student2", "focus", ?focus2)?
```

- `student1` participates with ratio 1.0 → their focus improves more and they get more tired.
- `student2` with lower sensitivity (0.5) → the effect on them is weaker in both states.

This shows how **states, actions, groups, and reactions** cooperate through one shared concept:

> **Each entity and each action has a participation ratio and sensitivity, translated into numbers in formulas,
> but they remain expressed through a clear English interface.**
> And these numbers are what the Conceptual LM layers later use when building the conceptual trace and English sentences.

