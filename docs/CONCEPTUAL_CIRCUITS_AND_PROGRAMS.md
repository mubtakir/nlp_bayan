# Conceptual Circuits and Meaning Programs

This document describes the **next layer** above the existing Conceptual LM stack in Bayan:

- We already have: conceptual traces, blueprints (conceptual patterns), language bridge, surface planning, sentence trees, surface realization, and symbolic n-gram LMs.
- We now add: **Conceptual Circuits** (دوائر تصورية أساسية) and **Meaning Programs** (برامج معاني) built from these circuits.

The goal is to mirror your mental model:

> Abstract templates of thought → concrete mental scenes → linguistic realization.

Where circuits model *reusable mental scenes*, and programs orchestrate them.

---

## 1. Recap: Existing Conceptual LM Architecture

We keep the existing 4-layer design as the foundation:

1. **Conceptual substrate (trace format)**
   - Entities, states, events, transforms, ideas, meta information.
   - Represents "what happened" and "to whom" in a language-neutral way.

2. **Conceptual patterns (blueprints)**
   - Library of ~14 patterns: Action, StateChange, Causal, Uncertainty, Description, Intensity, Comparative, TemporalOrder, Contextualization, etc.
   - Each blueprint maps trace roles to **sentence-level roles** (subject, predicate, axis, degree, value, cause_event, effect_event...).

3. **Concept–language bridge**
   - Realizes blueprint structures into symbolic sentence representations (e.g. `ActionSentence`, `DescriptionSentence`).
   - Independent of any specific natural language.

4. **Surface + LM layer**
   - Surface planner + sentence tree + surface realizer → symbolic tokens/text.
   - Symbolic bigram/trigram LM over these tokens, for diagnostics / toy training.

All new work must **respect and reuse** these layers, not bypass them.

---

## 2. Motivation: Why Conceptual Circuits?

Right now, blueprints are like **primitive components**:

- Analogy: transistors, resistors, capacitors, diodes.
- In our system: ActionSentencePattern, StateChangeSentencePattern, CausalSentencePattern, ComparativePattern, etc.

What we are missing is the layer of **small reusable circuits**:

- Analogy: amplifiers, oscillators, adders, counters.
- In our system: "micro-scenarios" composed of multiple blueprints that recur across many domains of thought.

Examples of such micro-scenarios:

1. **Action → StateChange → Evaluation**
   - A does X to B → B's state on some axis changes → we evaluate the new state.

2. **Comparison in context**
   - Compare Entity1 vs Entity2 on Axis with degrees and a contextual frame.

3. **Short causal chain**
   - Event A causes Event B, which in turn leads to Event C, with temporal ordering.

Conceptual Circuits will capture these as **first-class, reusable abstractions**.

---

## 3. Definition: What is a Conceptual Circuit?

A **Conceptual Circuit** is a *language-neutral* construct that:

1. Takes **structured conceptual inputs** (entities, events, axes, values, context, probabilities...).
2. Internally **invokes one or more blueprints** to build a small coherent scenario.
3. Produces as outputs:
   - A **coherent conceptual trace segment** (entities + events + transforms + ideas).
   - One or more **bridge structures** (e.g. DescriptionSentence, CausalSentence).
   - Optionally, a ready-made set of **LM training examples** (via the existing LM bridge).

In code terms, each circuit will be exposed as a Bayan-level API function inside a new module, e.g. `ai/conceptual_circuits.bayan`.

---

## 4. Design Principles for Circuits

Conceptual Circuits should obey these principles:

1. **Language neutrality**
   - Inputs and outputs are conceptual; no direct mention of English/Arabic.
   - Language-specific realization is always done via the existing bridge + surface pipeline.

2. **Compositionality**
   - A circuit is built *only* by composing existing blueprints and trace structures.
   - No hidden ad-hoc logic that bypasses the conceptual representation.

3. **Typed roles and clarity**
   - Each circuit defines clear, named roles (e.g. `Actor`, `Target`, `StateAxis`, `BeforeValue`, `AfterValue`, `EvaluationDegree`).
   - These map directly onto roles expected by the blueprints it uses.

4. **Introspectable outputs**
   - The output trace of a circuit should be easy to inspect/debug.
   - Developers should be able to print it and understand the scenario at a glance.

5. **Deterministic behaviour**
   - Given the same conceptual inputs, the circuit always produces the same trace and bridge structures.

6. **Reusability across domains**
   - Circuits must not encode domain-specific assumptions (e.g. "student", "teacher").
   - Instead, they work with abstract entities and axes; domain comes from how the user instantiates them.

---

## 5. Canonical Circuits (initial library)

We start the circuits library with a small set of **canonical circuits** that match your mental patterns and reuse the existing blueprints directly.

### 5.1 Action → StateChange → Evaluation

**Intent:** Model a minimal narrative: an agent performs an action that changes a patient's state along some axis, then we evaluate the result.

**Inputs (conceptual roles / function signature):**

Exposed in code as:

- `build_action_state_eval_circuit(actor_id, patient_id, action_kind, state_axis, before_value, after_value, evaluation_degree, context_label, action_intensity, action_probability)`

Where conceptually:

- `Actor` / `actor_id`: entity performing the action.
- `Patient` / `patient_id`: entity affected.
- `ActionKind` / `action_kind`: abstract label for the action.
- `StateAxis` / `state_axis`: axis for the state (e.g. Satisfaction, Health, Wealth).
- `BeforeValue`, `AfterValue`: numeric or symbolic values on that axis.
- `EvaluationDegree`: e.g. high / low / moderate.
- `Context`: abstract context for the situation.
- `Intensity` / `Probability`: how strong / how likely the action is.

**Internal composition:**

1. Use a generic interaction blueprint for the action event (`Generic_Interaction_Event`).
2. Use a state-change blueprint to represent the change on `StateAxis` (`State_Change_Template`).
3. Use description/intensity blueprints to evaluate the new state (`DescriptionPattern`, `IntensityPattern`).

**Outputs (returned structure):**

- `trace`: a small conceptual trace with:
  - Entities: `Actor`, `Patient`.
  - Events: one interaction event, plus a transform representing the state change.
- `roles`: role assignments for the involved blueprints.
- `bridge_structures`: pre-assembled bridge structures for:
  - `ActionSentencePattern`
  - `StateChangeSentencePattern`
  - `DescriptionPattern`
  - `IntensityPattern`

These bridge structures can later be realized into EN/AR sentences and LM examples using the existing bridge + surface + LM layers.

### 5.2 Comparison in context

**Intent:** Compare two entities along a shared axis, with explicit numeric/symbolic values, and summarize the comparison in a descriptive sentence, optionally tied to a context.

**Inputs (conceptual roles / function signature):**

- `build_comparison_in_context_circuit(entity1_id, entity2_id, axis_name, value1, value2, comparison_type, context_label)`

Where:

- `Entity1`, `Entity2`: entities being compared.
- `Axis`: state axis (e.g. Quality, Satisfaction, Speed).
- `Value1`, `Value2`: values of each entity on that axis.
- `ComparisonType`: label such as `greater`, `less`, `equal`.
- `Context`: optional abstract context label.

**Internal composition:**

1. Create a trace segment with two entities, each having a property on `Axis` with values `Value1` / `Value2`.
2. Use `ComparativePattern` for the conceptual comparison roles.
3. Use `DescriptionPattern` to produce a description sentence that summarizes the comparison from the perspective of `Entity1` (e.g. "Entity1 is greater on Axis").

**Outputs:**

- `trace`: entities with axis-values and contextual meta.
- `roles`: assignments for `ComparativePattern` and `DescriptionPattern`.
- `bridge_structures`: a `DescriptionPattern` bridge structure ready to be realized into EN/AR.

### 5.3 Causal link (basic cause → effect)

**Intent:** Represent a simple causal relation where one event (cause) leads to another (effect), with a strength and probability, and produce a causal sentence.

**Inputs (conceptual roles / function signature):**

- `build_causal_link_circuit(cause_event_id, effect_event_id, cause_actor_id, effect_actor_id, cause_action_kind, effect_action_kind, context_label, causal_strength, conditional_probability)`

Where:

- `CauseEvent`, `EffectEvent`: abstract event identifiers.
- `CauseActor`, `EffectActor`: entities associated with each event.
- `CauseActionKind`, `EffectActionKind`: abstract labels for the event types.
- `Context`: context label for the causal relation.
- `CausalStrength`: scalar [0,1] for how strong the link is.
- `ConditionalProb`: scalar [0,1] for how probable the effect is given the cause.

**Internal composition:**

1. Build a trace with two events (cause and effect) and their associated entities.
2. Add a `causal_links` collection tying `CauseEvent` to `EffectEvent` with `strength` and `prob`.
3. Use `Basic_Cause_Effect` and `Probabilistic_Causation` at the conceptual level.
4. Use `CausalSentencePattern` to produce a causal bridge structure.

**Outputs:**

- `trace`: entities, two events, and a causal link structure.
- `roles`: assignments for `Basic_Cause_Effect` and `Probabilistic_Causation`.
- `bridge_structures`: a `CausalSentencePattern` bridge structure ready for realization into EN/AR.

---


### 5.4 Temporal sequence (Event1 before/after Event2)

**Intent:** Represent a simple temporal ordering between two events (e.g. Event1 happens before Event2) and prepare a bridge structure that can mention this ordering.

**Inputs (conceptual roles / function signature):**

- `build_temporal_sequence_circuit(event1_id, event2_id, temporal_relation, context_label)`

Where:

- `Event1`, `Event2`: identifiers of the two events.
- `TemporalRelation`: label such as `before` / `after`.
- `Context`: optional abstract context label.

**Internal composition:**

1. Build a trace with two abstract events, both attached to the same context.
2. Use `TemporalOrderPattern` to capture the ordering relation between `Event1` and `Event2`.
3. Optionally reuse `CausalSentencePattern` as a linguistic bridge by encoding the temporal relation in the `Context` slot (e.g., "Event1 (before) Event2").

**Outputs:**

- `trace`: events with temporal meta.
- `roles`: assignments for `TemporalOrderPattern` (and optionally `Basic_Cause_Effect`).
- `bridge_structures`: a `CausalSentencePattern`-style bridge structure where `Context` carries the temporal relation.

### 5.5 Contextualized event

**Intent:** Wrap a focus event inside a contextual frame (e.g. "Event_X happens in the background of Context_Y") and summarize that relation in a descriptive sentence.

**Inputs (conceptual roles / function signature):**

- `build_contextualized_event_circuit(focus_event_id, actor_id, action_kind, context_frame, scope_label)`

Where:

- `FocusEvent`: identifier of the event of interest.
- `Actor`: entity performing the event.
- `ActionKind`: abstract label for the event type.
- `ContextFrame`: contextual frame label (e.g. global context, local scene).
- `Scope`: label describing how the event sits within the context (e.g. `background`, `foreground`).

**Internal composition:**

1. Build a trace with one event whose `context` field is `ContextFrame`.
2. Use `ContextualizationPattern` to bind `FocusEvent` to `ContextFrame` and `Scope`.
3. Use a `DescriptionPattern`-like bridge to generate a sentence that describes the event with respect to its context (e.g. "Event_X is background in ContextFrame").

**Outputs:**

- `trace`: one event with contextual meta.
- `roles`: assignments for `ContextualizationPattern` and a derived descriptive role.
- `bridge_structures`: a `DescriptionPattern` bridge structure encoding context and scope.

### 5.6 Uncertain cause-effect

**Intent:** Represent an uncertain causal relation where the effect is not guaranteed, and explicitly surface the uncertainty degree.

**Inputs (conceptual roles / function signature):**

- `build_uncertain_cause_effect_circuit(cause_event_id, effect_event_id, cause_actor_id, effect_actor_id, cause_action_kind, effect_action_kind, context_label, causal_strength, conditional_probability)`

Where (extending the causal link circuit):

- `CauseEvent`, `EffectEvent`, `CauseActor`, `EffectActor`, `CauseActionKind`, `EffectActionKind`, `Context` as before.
- `CausalStrength`: how strong the link is conceptually.
- `ConditionalProb`: the probability of the effect given the cause.

**Internal composition:**

1. Reuse the structure of the basic causal-link trace (two events + `causal_links`).
2. Use `Probabilistic_Causation` to capture strength and probability.
3. Use `CausalSentencePattern` for the main causal statement.
4. Use `UncertaintyPattern` to add a separate bridge structure that focuses on the uncertainty degree, grounded in `ConditionalProb` or `meta.confidence`.

**Outputs:**
- `trace`: as in the causal-link circuit, but marked as probabilistic.
- `roles`: assignments for `Probabilistic_Causation` and `UncertaintyPattern`.
- `bridge_structures`: at least two structures:
  - `CausalSentencePattern` (cause-effect statement).
  - `UncertaintyPattern` (explicit uncertainty phrase).

### 5.7 Enhanced Comparison Circuit

**Intent:** Compare two entities/options on multiple axes with detailed comparative analysis. This is useful for decision-making scenarios where we need to evaluate alternatives.

**Inputs (conceptual roles / function signature):**

- `build_enhanced_comparison_circuit(entity1_id, entity2_id, axis_name, value1, value2, comparison_type, context_label, confidence)`

Where:

- `Entity1`, `Entity2`: entities/options being compared.
- `Axis`: primary comparison axis.
- `Value1`, `Value2`: values on that axis.
- `ComparisonType`: label such as `greater`, `less`, `better`, `worse`.
- `Context`: abstract context label.
- `Confidence`: scalar [0,1] representing confidence in the comparison.

**Internal composition:**

1. Build a trace with two entities (options) and their properties.
2. Use `ComparativePattern` for the detailed comparison roles (including delta).
3. Use `DescriptionPattern` to describe the result.
4. Use `IntensityPattern` to highlight the magnitude of the difference (delta).

**Outputs:**

- `trace`: entities with properties and meta-data about the comparison.
- `roles`: assignments for `ComparativePattern`, `DescriptionPattern`, and `IntensityPattern`.
- `bridge_structures`: three structures:
  - `ComparativePattern` (detailed comparison).
  - `DescriptionPattern` (summary).
  - `IntensityPattern` (difference magnitude).

---

## 6. Meaning Programs (برامج المعاني)

**Meaning Programs** are higher-level compositions of circuits that achieve a cognitive task. They are analogous to a full electronic device built from multiple circuits.

In code terms, these now live in `ai/conceptual_programs.bayan`, and they are orchestrated (from the outside) by an `orchestrator` that chooses which program to run based on a control message.

**Note on Settings:**
Meaning programs are responsible for interpreting high-level settings like `detail_level` and `focus`:
- **`detail_level`**: Controls how many circuits are included in the narrative (e.g., `low` = core circuits only, `high` = add temporal/contextual/uncertainty circuits).
- **`focus`**: Adjusts parameters (e.g., `causal` focus boosts causal strength, `uncertainty` focus lowers probabilities) or adds specific circuits (e.g., extra temporal links).

### 6.1 Student study narrative (implemented)

The first concrete meaning program lives in `ai/conceptual_programs.bayan`:

- **Function:** `build_student_study_narrative_program()`
- **Circuits used together:**
  - `build_action_state_eval_circuit(...)`
  - `build_causal_link_circuit(...)`
  - `build_temporal_sequence_circuit(...)`
  - `build_contextualized_event_circuit(...)`
  - `build_uncertain_cause_effect_circuit(...)`
- **Output structure:**
  - `trace`: merged conceptual trace from all circuits (via the `merge_traces(traces)` helper).
  - `components`: a map from component name to the full circuit output (`{"trace", "roles", "bridge_structures"}`).

There is a demo under:

- `examples/conceptual_program_student_narrative_demo.bayan`

This demo:

1. Calls the meaning program and prints the merged conceptual trace.
2. Uses `lm_bridge.build_lm_examples_for_structure(...)` to realize, for each component, a set of EN/AR examples (action, state-change, evaluation, causal, uncertainty).
3. Trains bigram + trigram LMs on the union of all examples and prints scores for each example.

### 6.2 Medical treatment with uncertainty (implemented)

- **Function:** `build_medical_treatment_uncertainty_program()`
- **Domain:** medical / health.
- **Story:** a patient takes a treatment that usually improves health, with a possible side effect.
- **Circuits:** same five canonical circuits, instantiated with medical entities and events.
- **Demo:** `examples/conceptual_program_medical_treatment_demo.bayan`.

### 6.3 Economic investment with risk (implemented)

- **Function:** `build_economic_investment_risk_program()`
- **Domain:** economic / investment.
- **Story:** an investor studies the market, invests, and may gain or lose wealth.
- **Circuits:** same five canonical circuits, instantiated with economic entities/events.
- **Demo:** this program is used through the orchestrator in
  `examples/conceptual_orchestrator_demo.bayan` (see the orchestrator section below).

### 6.4 Orchestrator and NL mapper (glue above meaning programs)

Although the orchestrator and NL mapper are documented in more detail in
`CONCEPTUAL_LM_AI_HANDOVER.md`, it is useful to see how they relate to circuits and meaning programs:

- **Orchestrator module:** `ai/conceptual_orchestrator.bayan`
  - Holds a registry of meaning programs with metadata (domain, intent, id).
  - Accepts a `control_message` that includes fields such as `domain`, `intent`,
    `detail_level`, `languages`, `perspective`, `focus`, `scenario_variant`,
    `time_horizon`.
  - Chooses the appropriate meaning program, runs it, and passes the resulting
    `components` to the LM bridge to build symbolic examples.

- **NL mapper module:** `ai/conceptual_nl_mapper.bayan`
  - Accepts a free-form Arabic/English text and produces a structured
    `control_message`.
  - Uses simple keyword-based rules to identify the domain/intent and settings.
  - Feeds the resulting `control_message` into the orchestrator.

- **Demos:**
  - `examples/conceptual_orchestrator_demo.bayan` — shows dispatch from explicit
    control messages.
  - `examples/conceptual_nl_mapper_demo.bayan` — shows text → control message →
    orchestrator.
  - `examples/conceptual_interactive_orchestrator_repl.bayan` — interactive REPL
    to try arbitrary inputs.

This completes the picture: circuits → meaning programs → orchestrator/NL mapper → symbolic LM examples.


---

## 7. Implementation Plan (Roadmap)

### ✅ Phase 1: Core Infrastructure - **COMPLETED**

1. ✅ **Create `ai/conceptual_circuits.bayan`**
   - ✅ Defined clean API for circuits (inputs, outputs, naming conventions)
   - ✅ Implemented 6 canonical circuits:
     1. Action → StateChange → Evaluation
     2. Comparison in context
     3. Causal link (basic cause → effect)
     4. Temporal sequence (Event1 before/after Event2)
     5. Contextualized event
     6. Uncertain cause-effect

2. ✅ **Integrate with existing LM bridge**
   - ✅ Each circuit produces LM examples (EN/AR) using `build_lm_examples_for_structure`
   - ✅ Full integration tested and working

3. ✅ **Create demos for circuits**
   - ✅ Examples created under `examples/`:
     - `conceptual_circuit_action_state_eval_demo.bayan`
     - `conceptual_circuit_comparison_demo.bayan`
     - `conceptual_circuit_causal_demo.bayan`
     - `conceptual_circuit_temporal_demo.bayan`
     - `conceptual_circuit_contextual_demo.bayan`
     - `conceptual_circuit_uncertain_demo.bayan`

4. ✅ **Introduce Meaning Programs**
   - ✅ Created `ai/conceptual_programs.bayan` with **5 programs**:
     1. Student study narrative (education domain)
     2. Medical treatment with uncertainty (health domain)
     3. Economic investment with risk (economy domain)
     4. **Social relationship building (social domain)** - NEW
     5. **Daily decision-making (daily life domain)** - NEW
   - ✅ Demos created:
     - `conceptual_program_student_narrative_demo.bayan`
     - `conceptual_program_social_relationship_demo.bayan`
     - `conceptual_program_daily_decision_demo.bayan`

5. ✅ **Orchestrator and NL Mapper**
   - ✅ Created `ai/conceptual_orchestrator.bayan` - program registry and dispatcher
   - ✅ Created `ai/conceptual_nl_mapper.bayan` - natural language to control messages
   - ✅ Supports 5 domains: education, health, economy, **social**, **daily_life**
   - ✅ Demos created:
     - `conceptual_orchestrator_demo.bayan`
     - `conceptual_nl_mapper_demo.bayan`
     - `conceptual_interactive_orchestrator_repl.bayan`
     - **`conceptual_orchestrator_social_demo.bayan`** - NEW

---

### ⏳ Phase 2: Enhancement and Expansion - **IN PROGRESS**

#### Completed in Phase 2:
- ✅ **Task 4.5.1:** Expanded meaning programs to new domains (social, daily_life)
- ✅ **Task 4.5.3:** Expanded NL mapper vocabulary for new domains
- ✅ **Task 4.5.5:** Created educational examples for new programs

#### Remaining Tasks:

6. ⏳ **Use `detail_level` and `focus` settings (Task 4.5.2)**
   - Currently `scenario_variant` and `time_horizon` work
   - TODO: Use `detail_level` to control which circuits are included/excluded
   - TODO: Use `focus` to emphasize certain aspects (causal/temporal/uncertainty)

7. ⏳ **Improve orchestrator selection (Task 4.5.4)**
   - TODO: Support multiple programs per domain with selection policy
   - TODO: Choose different programs based on settings

8. ⏳ **Integrate new patterns into circuits (Task 4.3)**
   - `ComparativePattern`, `TemporalOrderPattern`, `ContextualizationPattern` exist in blueprints
   - TODO: Ensure full integration into circuits and programs
   - TODO: Add examples using these patterns

9. ⏳ **Link with actual LM layer (Task 4.2 & 4.4)**
   - TODO: Design interface between `SentenceTree` and `ai/nlp` modules
   - TODO: Create training data format: `(trace, roles, tree) -> text`
   - TODO: Improve `conceptual_surface_realizer.bayan` to produce natural text

---

### 📚 Documentation Status

- ✅ `docs/CONCEPTUAL_CIRCUITS_AND_PROGRAMS.md` - This document (main reference)
- ✅ `docs/CONCEPTUAL_LM_AI_HANDOVER.md` - Handover guide (updated with new work)
- ✅ `docs/CONCEPTUAL_PROGRAMS_EXPANSION_REPORT.md` - Technical report of expansion
- ✅ `CONCEPTUAL_PROGRAMS_COMPLETION_SUMMARY.md` - Executive summary
- ✅ `docs/NEXT_AI_MODEL_INSTRUCTIONS.md` - Instructions for next AI model

---

### 🎯 Next Steps for Future Development

See `docs/NEXT_AI_MODEL_INSTRUCTIONS.md` for detailed instructions on:
- Using `detail_level` and `focus` settings
- Improving orchestrator program selection
- Integrating comparison patterns into circuits
- Linking with actual LM layer in `ai/nlp`

This document remains the reference for the conceptual architecture; all code follows it step by step, keeping implementation aligned with the conceptual intent described here.

