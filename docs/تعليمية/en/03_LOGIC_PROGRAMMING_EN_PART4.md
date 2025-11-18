# Bayan Tutorial (EN) — Part 3.D: Logic Programming — Part 4 (Probabilistic & Causal)

> Quick Nav: [PART1](03_LOGIC_PROGRAMMING_EN_PART1.md) | [PART2](03_LOGIC_PROGRAMMING_EN_PART2.md) | [PART3](03_LOGIC_PROGRAMMING_EN_PART3.md) | [PART4](03_LOGIC_PROGRAMMING_EN_PART4.md)

This part introduces probabilistic reasoning in Bayan and explains how it connects to the causal network engine.

## 14) Probabilistic Reasoning (Concepts)

In classical logic programming, facts are either true or false. Probabilistic reasoning lets you attach confidence values in the range `[0.0 .. 1.0]` to states, transitions, or outcomes.

You can use this to model situations such as:
- Noisy sensors ("the sensor is 90% reliable").
- Human decisions ("this person is likely to choose tea with probability 0.7").
- Uncertain world states ("it is probably raining outside").

At a high level you:
- Define the possible states and events.
- Attach probabilities to them or to transitions between them.
- Ask questions such as "what is the probability that event X happens, given that Y is observed?".

Bayan's probabilistic layer is designed to integrate with its logic engine so that logical structure (facts/rules) and numeric uncertainty work together.

## 15) Causal Network Engine (Reference)

The causal network engine is a separate but closely related component that lets you build directed graphs of causes and effects.
You define nodes (variables), edges (causal relations), and quantitative strengths, then ask the engine to perform inference.

Typical tasks include:
- Predicting the probability of some outcome given evidence.
- Performing intervention analysis ("what happens if we force this node to a value?").
- Exploring which variables are most influential for a given effect.

For full details, syntax, and end-to-end examples, see:
- `bayan/docs/CAUSAL_NETWORK_ENGINE_GUIDE.md`

That guide shows how to declare nodes and links, load/save networks, and run probabilistic queries on top of your causal model.
