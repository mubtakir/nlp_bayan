# Logic in Bayan Language (6): Entities, Equations, Linguistic Operators, and Idea–Event–Result

> In this part we move from abstract logic to **the world of states, effects, and meanings**:
> - Entities (states, properties, actions, and reactions).
> - Equations that link states together.
> - Linguistic operators like `go`, `affect`, and `eat`.
> - The idea–event–result model via `idea`, `cognitive_event`, and `cognitive_entity`.
>
> We will commit as much as possible to English keywords, using `hybrid` only as a technical gateway.

## 1. Entities: Representing a Person or Thing with States and Actions

### 1.1 Simple Example: Ahmad's Hunger and "serve_meal" Action

```bayan
hybrid {
    entity Ahmad {
        states: {"hunger": 0.6, "fatigue": 0.3},
        properties: {"age": {"type": "numeric", "value": 20}},
        actions: {
            "serve_meal": {
                "strength": 1.0,
                "effects": [
                    {"on": "hunger", "formula": "value - 0.5*action_value"}
                ]
            }
        }
    }

    entity restaurant {
        actions: {
            "serve_meal": {"strength": 1.0, "effects": []}
        }
    }

    apply restaurant.serve_meal(Ahmad, action_value=1.0)
}
```

- The entity `Ahmad` has a `"hunger"` state with fuzziness 0.6.
- When we execute `apply restaurant.serve_meal(Ahmad, action_value=1.0)` the formula
  `value - 0.5*action_value` is applied to Ahmad's hunger state.

### 1.2 Reading Entity State (with English Interface)

The entity engine generates a logic fact named `state(Entity, Key, Value)`.

We can wrap it with an English relation:

```bayan
hybrid {
    entity_state(?entity, ?key, ?value) :- state(?entity, ?key, ?value).
}
query entity_state("Ahmad", "hunger", ?value)?
```

This way the educational code remains English, using `state/3` internally only.

## 2. Equations: Automatically Linking States (Opposites and Complement)

### 2.1 Defining Opposites: hot ↔ cold

```bayan
hybrid {
    entity weather {
        "states": {
            "hot":  {"type": "fuzzy", "value": 0.0},
            "cold": {"type": "fuzzy", "value": 1.0}
        }
    }

    define_opposites("weather", "state", "hot", "cold", 1.0)
    set_state("weather", "cold", 0.2)
}

hybrid {
    entity_state(?entity, ?key, ?value) :- state(?entity, ?key, ?value).
}
query entity_state("weather", "hot", ?hot_value)?
```

- `define_opposites` makes `hot` and `cold` complement each other to 1.0.
- When we set `cold = 0.2`, the value of `hot ≈ 0.8` automatically.

## 3. Linguistic Operators: go, affect, eat, link, transform

### 3.1 Example: "go" Operator for Entity Movement on x-axis

```bayan
hybrid {
    entity Ahmad {
        "properties": {"x": {"type": "numeric", "value": 0.0}},
        "actions": {
            "go": {
                "effects": [
                    {"on": "x", "formula": "value + 2*sensitivity"}
                ]
            }
        }
    }

    go(["Ahmad.0.5"])  # x += 1.0
}

hybrid {
    entity_property(?entity, ?key, ?value) :- property(?entity, ?key, ?value).
}
query entity_property("Ahmad", "x", ?position)?
```

- `go([...])` is an English wrapper over `perform("go", participants, ...)`.
- We use sensitivity 0.5 so the increase becomes `2 * 0.5 = 1.0`.

### 3.2 Defining a Custom Linguistic Operator

```bayan
hybrid {
    entity pusher {
        "properties": {"x": {"type": "numeric", "value": 0.0}},
        "actions": {
            "go": {
                "effects": [
                    {"on": "x", "formula": "value + sensitivity"}
                ]
            }
        }
    }

    define_operator("push", action="go")
    push(["pusher:1.0"])  # wraps perform("go", ...)
}
```

This way we can build English linguistic operators that express complex actions over the entity engine.

## 4. Idea–Event–Result Model (cognitive_entity + cognitive_event + idea)

### 4.1 Defining Cognitive Entities and Cognitive Events

```bayan
hybrid {
    cognitive_entity land {
        color: "brown",
        state: "dry"
    }

    cognitive_event rain_falls {
        participants: {
            "land": {"role": "affected", "degree": 1.0}
        },
        strength: 0.8,
        transformation: {
            "land.color": "green",
            "land.state": "wet"
        }
    }
}
```

### 4.2 Triggering the Event and Building an Idea that Combines Entities and Result

```bayan
hybrid {
    trigger rain_falls
}

idea "green_land" {
    entities: {
        "land": {"state": "dry"}
    },
    event: "rain_falls",
    result: {
        "state_changes": {
            "land.color": "green"
        }
    }
}
```

- `cognitive_entity` defines a linguistic/cognitive entity.
- `cognitive_event` defines an event that affects entities.
- `trigger` executes the event and changes entity states.
- `idea` links entities, event, and result in one model.

## 5. Summary of This Part

- We learned about **entities** and how to give them states, actions, and reactions.
- We saw how to use **equations** like `define_opposites` to automatically link states.
- We used **linguistic operators** (`go`, `push`, ...) as an English gateway to the action engine.
- We introduced the **idea–event–result model** via `cognitive_entity`, `cognitive_event`, and `idea`.

With these building blocks, Bayan can combine classical logic, fuzzy states, meanings, and events in one rich model with an English interface.
It also provides **Conceptual LM layers** (in parts 9–10) with an organized conceptual trace of what happens so it can later be converted to understandable English sentences.

