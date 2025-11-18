# Logic in Bayan Language (5): Causal Networks (Cause–Effect Relationship Engine)

> In this part we enter one of **the most powerful new features** in Bayan:
> **The causal networks engine** that allows you to represent a world of causes and effects in any domain (social, professional, psychological, scientific…).
> 
> We will commit to English in names and data, using engine command names as they are (`create_network`, `add_node`, `add_causal_relation`, ...)
> because they are executed from Bayan's core itself.

## 1. What is a Causal Network?

A causal network consists of:

- **Nodes** representing things or states:
  - People: "friend", "liar", "leader".
  - States: "trust", "respect", "cooperation", "shared_success".
- **Causal relations** between nodes:
  - "honesty" **leads to** "trust".
  - "trust" **enables** "respect".
  - "respect" **enhances** "cooperation".
  - "cooperation" **leads to** "shared_success".

Like drawing a map: from cause to effect, with connection strength (a number between 0 and 1).

## 2. Creating a Simple English Causal Network

### 2.1 Creating a "Professional Relations" Network

```bayan
hybrid {
    # Create a network for the professional domain
    create_network("work_rel", "Professional Relations Network", "professional");
}
```

- `"work_rel"`: network identifier (we choose it freely).
- `"Professional Relations Network"`: English name for the network.
- The domain `"professional"` indicates this network is in the professions and work domain.

### 2.2 Adding English Nodes

```bayan
hybrid {
    create_network("work_rel", "Professional Relations Network", "professional");

    # People, states, and behaviors
    add_node("work_rel", "honesty", "behavior", "behavior");
    add_node("work_rel", "trust", "state", "state");
    add_node("work_rel", "respect", "state", "state");
    add_node("work_rel", "cooperation", "behavior", "behavior");
    add_node("work_rel", "shared_success", "state", "state");
}
```

- The names (`"honesty"`, `"trust"`, ...) are English.
- The types (`"behavior"`, `"state"`) determine the node type in the engine.

### 2.3 Adding English Causal Relations

```bayan
hybrid {
    create_network("work_rel", "Professional Relations Network", "professional");

    add_node("work_rel", "honesty", "behavior", "behavior");
    add_node("work_rel", "trust", "state", "state");
    add_node("work_rel", "respect", "state", "state");
    add_node("work_rel", "cooperation", "behavior", "behavior");
    add_node("work_rel", "shared_success", "state", "state");

    # Causal relations (with approximate strength)
    add_causal_relation("work_rel", "honesty", "trust", "causes", "0.9");
    add_causal_relation("work_rel", "trust", "respect", "leads_to", "0.8");
    add_causal_relation("work_rel", "respect", "cooperation", "enhances", "0.85");
    add_causal_relation("work_rel", "cooperation", "shared_success", "causes", "0.9");
}
```

- Relation types (`"causes"`, `"leads_to"`, `"enhances"`) are types supported in the engine.
- Each relation has a **strength** between 0 and 1 expressing how stable this connection is.

## 3. Causal Reasoning: From Cause to Effect

### 3.1 Discovering the Path from "honesty" to "shared_success"

```bayan
hybrid {
    create_network("work_rel", "Professional Relations Network", "professional");
    # ... (add nodes and relations as in previous example) ...

    # Inference: find causal chain from honesty to shared_success
    infer_causal_chain("work_rel", "honesty", "shared_success", "5");
}
```

- The function `infer_causal_chain` searches for a chain like:

  `honesty → trust → respect → cooperation → shared_success`

- The number `"5"` is the maximum chain length (maximum number of steps we allow).

### 3.2 Finding All Effects of Honesty

```bayan
hybrid {
    create_network("work_rel", "Professional Relations Network", "professional");
    # ... (nodes and relations) ...

    # Find all effects up to depth 3 steps
    find_all_effects("work_rel", "honesty", "3");
}
```

- `find_all_effects` gives you **all nodes** that come after "honesty" in the network up to a certain depth.

### 3.3 Finding All Causes of a Certain Event

```bayan
hybrid {
    create_network("work_rel", "Professional Relations Network", "professional");
    # ...

    # What causes lead to shared_success?
    find_all_causes("work_rel", "shared_success", "3");
}
```

- Here we explore everything before "shared_success" in the network up to depth 3.

## 4. Brief Example: Cause–Effect Network for Academic Life

```bayan
hybrid {
    create_network("study", "Academic Life Network", "professional");

    add_node("study", "studying", "behavior", "behavior");
    add_node("study", "understanding", "state", "state");
    add_node("study", "high_grade", "state", "state");
    add_node("study", "scholarship", "state", "state");

    add_causal_relation("study", "studying", "understanding", "causes", "0.9");
    add_causal_relation("study", "understanding", "high_grade", "causes", "0.85");
    add_causal_relation("study", "high_grade", "scholarship", "leads_to", "0.8");

    # Infer success path
    infer_causal_chain("study", "studying", "scholarship", "4");
}
```

- All names are English.
- The engine here can display a chain like:

  `studying → understanding → high_grade → scholarship`

## 5. Summary of This Part

- We learned about **the causal networks engine** in Bayan and how it represents:
  - English nodes (people, states, behaviors…)
  - And causal relations (causes, leads_to, enhances, ...).
- We saw how to build a simple network for professional relations, and how to infer:
  - The path from cause to effect (`infer_causal_chain`).
  - All effects of a certain cause (`find_all_effects`).
  - All causes of a certain effect (`find_all_causes`).
- This foundation will later facilitate connecting causal networks with:
  - **Entities** and their states.
  - **Probabilistic reasoning** (relation strengths can be interpreted probabilistically).
  - **The broader model** of idea–event–result and Conceptual LM layers.

In the next part we will move to **entities, equations, and linguistic operators** and how they interact with logic, probabilities, and causal networks.


