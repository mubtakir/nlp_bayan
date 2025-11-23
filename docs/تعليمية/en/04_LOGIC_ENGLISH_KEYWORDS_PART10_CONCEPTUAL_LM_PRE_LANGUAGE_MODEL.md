# Logic in Bayan Language (10): Pre-Language Model Layers (Conceptual LM)

> In this part we connect everything we've seen (entities, events, causal networks, semantic networks, probabilities)
> with **pre-language model layers** called in Bayan: **Conceptual LM**.
>
> These layers work on «raw meaning» (conceptual trace) before we decide how to write it in Arabic or English.

---

## 1. From the World to a Single «Conceptual Trace»

Bayan assumes that the system (entities, states, events, transformations, probabilities, causes…) ultimately produces
a **unified conceptual trace** `conceptual_trace`:

- List of entities: people, things, organizations...
- States and properties for each entity (e.g., «Ahmad's happiness = 0.7»).
- Events (e.g., «Ahmad studies», «medicine affects disease»).
- State transformations (before/after).
- Causal links between events.

This `conceptual_trace` doesn't yet care about Arabic or English phrasing; it's **semantic representation only**.

---

## 2. Conceptual Blueprints

Next comes a file like `ai/conceptual_blueprints.bayan` that defines **meaning templates**:

- `Generic_Interaction_Event` (general interaction event).
- `State_Change_Template` (state change on a 0..1 axis).
- `Basic_Cause_Effect` (cause and effect).
- And other patterns: uncertainty, description, intensity, comparison, temporal ordering...

### 2.1 Example from the Templates File

The following template expresses a «interaction event» in general:

```bayan
conceptual_pattern Generic_Interaction_Event {
    type: "EventPattern"
    roles: {
        "Actor":      { "kind": "entity" },
        "Target":     { "kind": "entity",  "optional": True },
        "ActionKind": { "kind": "action" },
        "Context":    { "kind": "context" }
    }
    linguistic_templates: ["ActionSentencePattern"]
}
```

The idea:

- `Actor`: the doer (entity).
- `Target`: action target (optional).
- `ActionKind`: action type (study, treatment, investment...).
- `Context`: context (time, place, general state).
- `linguistic_templates`: tells later layers this is suitable for an «action» sentence (ActionSentence).

Another template expresses state change:

```bayan
conceptual_pattern State_Change_Template {
    type: "StatePattern"
    roles: {
        "Entity":      { "kind": "entity" },
        "PropertyAxis":{ "kind": "axis" },
        "BeforeValue": { "kind": "value", "range": [0,1] },
        "AfterValue":  { "kind": "value", "range": [0,1] }
    }
    linguistic_templates: ["StateChangeSentencePattern"]
}
```

This directly connects to the state axes we saw in entities (like «happiness» between 0 and 1).

---

## 3. Conceptual Language Bridge

After matching `conceptual_trace` with templates like `Generic_Interaction_Event` or
`State_Change_Template`, comes the **language bridge** stage:

- Files like `ai/conceptual_language_bridge.bayan` define how to convert
  *conceptual pattern* to **conceptual sentence pattern**:
  - `ActionSentence`
  - `StateChangeSentence`
  - `CausalSentence`
  - `UncertaintySentence` ...

This stage still **doesn't choose Arabic or English words**; it just says:

> We have an «action» sentence with such actor, such target, such action content, such context.

---

## 4. Surface Planning and Sentence Tree

After the language bridge come two layers:

1. **Surface planner** `ai/conceptual_surface_planner.bayan`:
   - Decides role ordering according to language:
     - In English: Subject-Verb-Object (SVO).
     - In Arabic: usually Verb-Subject-Object (VSO) in verbal sentences.
   - Decides where to mention adverbials (time, place, cause...).

2. **Sentence tree** `ai/conceptual_sentence_tree.bayan`:
   - Builds a symbolic tree representing:
     - Sentence type (verbal, nominal, conditional...).
     - Nodes (verb, subject, object, adverb...).

At this stage we have a **linguistically ready sentence structure** (positions known),
but the precise word choice and final synonyms can still benefit from:

- The synonyms and proximity layer (Part 9).
- The symbolic language model `ai/nlp` and `nlp_bayan`.

---

## 5. Conceptual Circuits and Meaning Programs

Above these layers exist files like:

- `ai/conceptual_circuits.bayan`
- `ai/conceptual_programs.bayan`
- `ai/conceptual_orchestrator.bayan`
- `ai/conceptual_nl_mapper.bayan`

These represent **logic/conceptual circuits** and higher-level meaning programs, for example:

- Scenario «student studies subject with certain effort over time».
- Scenario «medical treatment with uncertainty in outcome».
- Scenario «financial investment with risk and expected return».
- Scenario «enhanced detailed comparison between two options for decision making».

Each meaning program uses:

1. Entities, states, events, and causal relations.
2. Builds a rich `conceptual_trace`.
3. Passes it through conceptual templates + language bridge + surface planning.
4. Uses synonyms, similarity, and language model to choose best phrasing.

---

## 6. Summary of the Path from Logic to Language

You can imagine the entire chain as layers:

1. **Logic + entities + probabilities + causes + semantic networks**
   (Parts 1–8 + Part 7 for advanced entities).
2. **Synonyms and proximity layer** (Part 9):
   - `similar/5`, `close/3`, `synonym/3`, synonyms DSL.
3. **Unified conceptual trace** `conceptual_trace`.
4. **Conceptual templates** (blueprints) like `Generic_Interaction_Event`.
5. **Conceptual language bridge** → conceptual sentence patterns.
6. **Surface planning + sentence tree** according to language (Arabic/English).
7. **Symbolic language model + generation** (using synonyms, similarity, n-grams...).

This shows that **logic, entities, causal and semantic networks** don't live separately,
but feed the Conceptual LM layer that stays **before the language model**,
working on the conceptual trace then gradually handing it to surface language layers.

## 7. Complete Example: From Student Entity to English Sentence

Imagine the following scenario that combines what we learned in previous parts:

- In the entity layer (Parts 6 & 7):
  - Entity `student` with states like "focus" and "fatigue".
  - Action "study" raises focus and increases fatigue with ratios depending on `power` and `sensitivity`.
- In the causal network (Part 5):
  - "studying" → "understanding" → "high_grade" → "scholarship".
- In semantic programming (Part 8):
  - Information about the student: which subject they study, where and when.

When running a meaning program from Conceptual LM files:

1. The student's state, events, and causal links are collected in one `conceptual_trace`.
2. This trace is matched with templates like `Generic_Interaction_Event` and `State_Change_Template`.
3. The language bridge builds a representation for an English action sentence: subject = the student, verb = studying, object = mathematics subject, context = in the library in the evening.
4. The surface planner and sentence tree decide element ordering (subject → verb → object → adverb).
5. The synonyms and similarity layer (Part 9) and language model choose the most appropriate phrasing among alternatives like:
   - «The student studies mathematics diligently in the library in the evening.»
   - «The student is studying mathematics in the library with high focus.»

With this example you see how **numbers, states, probabilities, and causal relations** that we defined in parts (1–9)
transition to **an understandable English sentence** through Conceptual LM layers before any traditional language model intervenes.


