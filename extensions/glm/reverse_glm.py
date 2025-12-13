import re
from typing import List, Dict, Any, Tuple

def _build_entity(id, kind="generic_entity", domain="abstract_domain", properties=None):
    ent = {
        "id": id,
        "kind": kind,
        "domain": domain
    }
    if properties:
        ent["properties"] = properties
    return ent

def _build_event(id, action, actors, targets, context, probability=1.0, intensity=None):
    evt = {
        "id": id,
        "action": action,
        "actors": actors,
        "targets": targets,
        "context": context,
        "probability": probability
    }
    if intensity is not None:
        evt["intensity"] = intensity
    return evt

def build_action_state_eval_circuit(actor_id, patient_id, action_kind, state_axis, before_value, after_value, evaluation_degree, context_label, action_intensity, action_probability):
    delta_value = after_value - before_value
    entities = [
        _build_entity(actor_id),
        _build_entity(patient_id, properties={state_axis: before_value})
    ]
    action_event_id = "Event_Action_1"
    events = [
        _build_event(action_event_id, action_kind, [actor_id], [patient_id], context_label, action_probability, action_intensity)
    ]
    transforms = [{
        "event_id": action_event_id,
        "entity_id": patient_id,
        "property": state_axis,
        "before": before_value,
        "after": after_value,
        "law": "default_state_change"
    }]
    meta = {"source": "action_state_eval_circuit", "confidence": action_probability}
    trace = {"entities": entities, "events": events, "transforms": transforms, "meta": meta}
    
    # Simplified roles for demo
    roles = {
        "Generic_Interaction_Event": {"Actor": actor_id, "Target": patient_id, "ActionKind": action_kind},
        "State_Change_Template": {"Entity": patient_id, "PropertyAxis": state_axis, "Delta": delta_value}
    }
    return {"trace": trace, "roles": roles}

def build_causal_link_circuit(cause_event_id, effect_event_id, cause_actor_id, effect_actor_id, cause_action_kind, effect_action_kind, context_label, causal_strength, conditional_probability):
    entities = [_build_entity(cause_actor_id), _build_entity(effect_actor_id)]
    events = [
        _build_event(cause_event_id, cause_action_kind, [cause_actor_id], [effect_actor_id], context_label, conditional_probability),
        _build_event(effect_event_id, effect_action_kind, [effect_actor_id], [], context_label, conditional_probability)
    ]
    causal_links = [{"cause": cause_event_id, "effect": effect_event_id, "strength": causal_strength, "prob": conditional_probability}]
    meta = {"source": "causal_link_circuit", "confidence": conditional_probability, "context": context_label}
    trace = {"entities": entities, "events": events, "causal_links": causal_links, "meta": meta}
    roles = {
        "Basic_Cause_Effect": {"CauseEvent": cause_event_id, "EffectEvent": effect_event_id, "Strength": causal_strength}
    }
    return {"trace": trace, "roles": roles}

def build_comparison_in_context_circuit(entity1_id, entity2_id, axis_name, value1, value2, comparison_type, context_label):
    entities = [
        _build_entity(entity1_id, properties={axis_name: value1}),
        _build_entity(entity2_id, properties={axis_name: value2})
    ]
    meta = {"source": "comparison_in_context_circuit", "confidence": 1.0, "context": context_label}
    trace = {"entities": entities, "meta": meta}
    roles = {
        "ComparativePattern": {"Entity1": entity1_id, "Entity2": entity2_id, "Axis": axis_name, "ComparisonType": comparison_type}
    }
    return {"trace": trace, "roles": roles}

def build_uncertain_cause_effect_circuit(cause_event_id, effect_event_id, cause_actor_id, effect_actor_id, cause_action_kind, effect_action_kind, context_label, causal_strength, conditional_probability):
    # Reuse causal link logic but with different meta/roles
    base = build_causal_link_circuit(cause_event_id, effect_event_id, cause_actor_id, effect_actor_id, cause_action_kind, effect_action_kind, context_label, causal_strength, conditional_probability)
    base["trace"]["meta"]["source"] = "uncertain_cause_effect_circuit"
    base["roles"]["UncertaintyPattern"] = {"Content": "CauseEffectRelation", "Degree": conditional_probability}
    return base

def build_contextualized_event_circuit(focus_event_id, actor_id, action_kind, context_frame, scope_label):
    entities = [_build_entity(actor_id)]
    events = [_build_event(focus_event_id, action_kind, [actor_id], [], context_frame)]
    meta = {"source": "contextualized_event_circuit", "confidence": 1.0, "context": context_frame}
    trace = {"entities": entities, "events": events, "meta": meta}
    roles = {"ContextualizationPattern": {"FocusEvent": focus_event_id, "ContextFrame": context_frame, "Scope": scope_label}}
    return {"trace": trace, "roles": roles}

def build_temporal_sequence_circuit(event1_id, event2_id, temporal_relation, context_label):
    events = [
        {"id": event1_id, "action": "AbstractAction1", "context": context_label},
        {"id": event2_id, "action": "AbstractAction2", "context": context_label}
    ]
    meta = {"source": "temporal_sequence_circuit", "confidence": 1.0, "temporal_relation": temporal_relation, "context": context_label}
    trace = {"events": events, "meta": meta}
    roles = {"TemporalOrderPattern": {"Event1": event1_id, "Event2": event2_id, "TemporalRelation": temporal_relation}}
    return {"trace": trace, "roles": roles}


class ReverseGLM:
    """
    Reverse General Language Model (Reverse GLM)
    
    Responsible for mapping Natural Language (NL) back to abstract Conceptual Circuits.
    It uses discourse markers to segment the text and infer the underlying
    conceptual structure (Blueprint/Circuit).
    """
    
    def __init__(self):
        # Define discourse markers and their corresponding circuit hints
        self.markers = {
            # Emphasis / Assertion -> ActionStateEval or Fact
            r"إنّ هذا": "assertion",
            r"إنّ": "assertion",
            
            # Inference / Causal -> CausalLink
            r"يتبين من ذلك": "inference",
            r"يتبين من هذا": "inference",
            r"هذا يدل على أنّ": "inference",
            r"هذا يدل على": "inference",
            r"ذلك يشير إلى": "inference",
            r"من هذا يتبين": "inference",
            r"هذا يعني أنّ": "inference",
            r"هذا يعني": "inference",
            
            # Contrast / Comparison -> ComparisonInContext
            r"بينما": "contrast",
            r"في حين": "contrast",
            
            # Correlation / Uncertainty -> UncertainCauseEffect
            r"فكلما كان": "correlation",
            r"كلما": "correlation",
            
            # Conditional / Topic -> ContextualizedEvent
            # User feedback: These are introductory phrases, content starts AFTER them.
            # We include the full phrase including "فعليك" (then you must) to strip it from content.
            r"اذا اردت معرفة تأثير ذلك فعليك": "topic_focus",
            r"اذا اردت معرفة ذلك فعليك": "topic_focus",
            r"اذا اردت دراسة ذلك فعليك": "topic_focus",
            r"اذا اردت معرفة": "topic_focus", # Fallback
            r"إذا أردت دراسة": "topic_focus",
            r"لطالما": "continuity",
        }
        
        # Compile regex pattern for all markers
        # We sort by length descending to match longer phrases first (e.g. "إنّ هذا" before "إنّ")
        sorted_markers = sorted(self.markers.keys(), key=len, reverse=True)
        # Escape markers to ensure special regex chars are treated as literals if any
        # (Though our markers are mostly Arabic text, good practice)
        escaped_markers = [re.escape(m) for m in sorted_markers]
        self.pattern = re.compile(r'(' + '|'.join(escaped_markers) + r')')

    def segment_text(self, text: str) -> List[Tuple[str, str]]:
        """
        Segments the text based on discourse markers.
        Returns a list of (marker, content) tuples.
        The first segment might have an empty marker if the text doesn't start with one.
        """
        segments = []
        
        # Split keeping the delimiters
        parts = self.pattern.split(text)
        
        current_marker = None
        
        # If the text doesn't start with a marker, the first part is content with no marker
        if parts and parts[0] not in self.markers:
             if parts[0].strip():
                segments.append(("START", parts[0].strip()))
             parts = parts[1:]
        
        i = 0
        while i < len(parts):
            item = parts[i]
            # Check if item matches one of our markers (un-escaped)
            # Since split returns the captured group, it should match exactly one of the keys
            if item in self.markers:
                current_marker = item
                content = ""
                if i + 1 < len(parts):
                    content = parts[i+1].strip()
                    i += 1
                segments.append((current_marker, content))
            else:
                # Should not happen if logic is correct, but handle just in case
                if item.strip():
                    segments.append(("UNKNOWN", item.strip()))
            i += 1
            
        return segments

    def map_segment_to_circuit(self, marker: str, content: str) -> Dict[str, Any]:
        """
        Maps a single text segment (marker + content) to a Conceptual Circuit.
        This is a heuristic mapping. In a full system, we would parse the 'content'
        deeply. Here we extract entities/actions naively or use placeholders
        to demonstrate the structural mapping.
        """
        marker_type = self.markers.get(marker, "generic")
        
        # Heuristic extraction of potential entities from content
        # (Very basic: just taking first few words as entity/action for demo)
        words = content.split()
        entity_1 = words[0] if len(words) > 0 else "UnknownEntity"
        entity_2 = words[1] if len(words) > 1 else "TargetEntity"
        remainder = " ".join(words[2:]) if len(words) > 2 else "generic context"
        
        if marker_type == "assertion":
            # Map to ActionStateEvalCircuit
            # "Indeed, [Entity] [Action]..."
            return build_action_state_eval_circuit(
                actor_id=entity_1,
                patient_id=entity_2,
                action_kind="AssertedAction",
                state_axis="Truth",
                before_value=0.0,
                after_value=1.0,
                evaluation_degree="High",
                context_label="AssertionContext",
                action_intensity=0.9,
                action_probability=1.0
            )
            
        elif marker_type == "inference":
            # Map to CausalLinkCircuit
            # "This indicates that [Cause] leads to [Effect]..."
            return build_causal_link_circuit(
                cause_event_id="InferredCause",
                effect_event_id="InferredEffect",
                cause_actor_id=entity_1,
                effect_actor_id=entity_2,
                cause_action_kind="Indication",
                effect_action_kind="Result",
                context_label="InferenceContext",
                causal_strength=0.8,
                conditional_probability=0.9
            )
            
        elif marker_type == "contrast":
            # Map to ComparisonInContextCircuit
            # "While [Entity1] is X, [Entity2] is Y..."
            return build_comparison_in_context_circuit(
                entity1_id=entity_1,
                entity2_id=entity_2,
                axis_name="ContrastAxis",
                value1="ValueA",
                value2="ValueB",
                comparison_type="different",
                context_label="ContrastContext"
            )
            
        elif marker_type == "correlation":
            # Map to UncertainCauseEffectCircuit
            # "The more [X] happens, the more [Y]..."
            return build_uncertain_cause_effect_circuit(
                cause_event_id="CorrelatedEvent1",
                effect_event_id="CorrelatedEvent2",
                cause_actor_id=entity_1,
                effect_actor_id=entity_2,
                cause_action_kind="Increase",
                effect_action_kind="Increase",
                context_label="CorrelationContext",
                causal_strength=0.7,
                conditional_probability=0.6
            )
            
        elif marker_type == "topic_focus":
            # Map to ContextualizedEventCircuit
            # "If you want to study [Topic]..."
            # For the long marker "اذا اردت معرفة تأثير ذلك فعليك", the content is just the action to take.
            # We can infer the context from the marker itself or just focus on the content.
            return build_contextualized_event_circuit(
                focus_event_id="StudyEvent",
                actor_id="Observer",
                action_kind="Study",
                context_frame=entity_1, # The topic (first word of content)
                scope_label="Foreground"
            )
            
        else:
            # Deep Inference: Try IstinbatEngine first
            from .istinbat_engine import IstinbatEngine
            
            istinbat = IstinbatEngine()
            deduction = istinbat.process(content)
            
            if deduction:
                return deduction.circuit
            
            # Fallback: Use DynamicCircuitBuilder directly if Istinbat fails (e.g. parsing error)
            from .dynamic_builder import DynamicCircuitBuilder, Atom
            
            words = content.split()
            atoms = []
            if len(words) > 0:
                atoms.append(Atom("Entity", words[0]))
            if len(words) > 1:
                atoms.append(Atom("Action", words[1]))
            if len(words) > 2:
                atoms.append(Atom("Entity", words[2]))
            
            builder = DynamicCircuitBuilder()
            return builder.assemble(atoms)

    def process_text(self, text: str) -> List[Dict[str, Any]]:
        """
        Full pipeline: Text -> Segments -> Circuits
        """
        segments = self.segment_text(text)
        circuits = []
        
        for marker, content in segments:
            circuit = self.map_segment_to_circuit(marker, content)
            # Annotate with the source text for traceability
            circuit["source_text_segment"] = f"[{marker}] {content}"
            circuits.append(circuit)
            
        return circuits
