# Logic in Bayan Language (4): Probabilistic Reasoning and Uncertainty

> In this part we define **how Bayan language handles uncertainty** using probabilities and English uncertainty tools.
> We will stay committed to English as much as possible, noting that probabilistic logic keywords are now **bilingual**:
> - We will use the hybrid block in English form `hybrid { ... }` in examples.
> - Probabilistic facts can be written as either `fact[0.8]` or `حقيقة[0.8]`.
> In the examples below we commit to English as much as possible, referring to the Arabic form only when needed.
> While the interpreter can understand the full Arabic equivalent in actual code.

## 1. Probabilistic Facts `fact[0.8]`

### 1.1 Example: Probability of Rain

```bayan
hybrid {
    # 90% probability that it will rain today
    fact[0.9] rains("today").

    # 30% probability of strong winds
    fact[0.3] strong_winds("today").
}
```

- General syntax: `fact[probability] relation(arguments...).`
- Probability is a number between 0 and 1 (e.g., 0.9 = 90%).
- When these facts are used in rules and queries, the Bayan engine **combines probabilities** along the inference path (by multiplication).

### 1.2 Example: Probability of a Mood State

```bayan
hybrid {
    fact[0.8] good_sleep("Ahmad").
    fact[0.6] drank_coffee("Ahmad").

    good_mood(?person) :-
        good_sleep(?person),
        drank_coffee(?person).
}
```

- Here the probability of `good_mood("Ahmad")` is approximately `0.8 × 0.6 = 0.48` (48%).

## 2. English Uncertainty Tools: maybe, likely, unlikely, possible, certain

Bayan language provides five English uncertainty tools related to the current probability of the solution:

| Tool | Condition on p | Approximate Meaning |
|------|---------------|---------------------|
| `maybe` | `p > 0.5` | More than 50% |
| `likely` | `p > 0.7` | Strong (more than 70%) |
| `unlikely` | `p < 0.3` | Very weak (less than 30%) |
| `possible` | `0.2 < p < 0.8` | In the middle, neither very weak nor very strong |
| `certain` | `p > 0.95` | Near certainty (more than 95%) |

These tools are used in queries to check the strength of probability of a certain event.

## 3. Complete Example: Tomorrow's Weather with Uncertainty Tools

```bayan
hybrid {
    # Probabilistic facts about tomorrow's weather
    fact[0.75] will_rain("tomorrow").
    fact[0.15] will_snow("tomorrow").

    # Uncertainty queries in English
    query maybe("will_rain", "tomorrow").        # yes (75% > 50%)
    query likely("will_rain", "tomorrow").       # yes (75% > 70%)
    query unlikely("will_snow", "tomorrow").     # yes (15% < 30%)

    # Query to verify the event is nearly certain
    query certain("will_rain", "tomorrow").      # no (75% < 95%)
}
```

- The names (`"will_rain"`, `"will_snow"`, `"tomorrow"`) are fully English data.
- Uncertainty tools (`maybe`, `likely`, `unlikely`, `possible`, `certain`) are English.

## 4. Reading Probability Value Numerically (For Advanced Use)

Sometimes we need to get **the probability value as a number** inside the rule itself, not just as a ready condition.

Bayan language provides a built-in tool `probability(?P)` that gives you the current probability of the solution.

### 4.1 Example: Patient in Critical Condition if Probability Exceeds 70%

```bayan
hybrid {
    # Probabilistic facts about patient condition
    fact[0.8] has_flu("patient").
    fact[0.9] has_fever("patient").

    critical_condition(?person) :-
        has_flu(?person),
        has_fever(?person),
        probability(?P),
        ?P > 0.7.

    # Query: Is the patient in critical condition?
    query critical_condition("patient")?
}
```

- Inside the inference of `critical_condition("patient")` the engine multiplies probabilities (`0.8 × 0.9 = 0.72`).
- `probability(?P)` binds `?P` to this value (about 0.72) then we use the numerical condition `?P > 0.7`.

## 5. Summary of This Part

- We defined **probabilistic facts** using `fact[0.x]` or the Arabic equivalent `حقيقة[0.x]` with English relations and names.
- We used English uncertainty tools `maybe`, `likely`, `unlikely`, `possible`, `certain` to query about event strength.
- We saw how we can access **the probability value numerically** inside the rule using `probability(?P)` then deal with it using numerical conditions.

In the coming parts we will connect this probabilistic foundation with:
- **Causal networks** (how these probabilities propagate through a network of causes and effects),
- And with **entities** and **linguistic equations and operators**,
- Within a broader model of idea–event–result and Conceptual LM layers and linguistic interpretation.

