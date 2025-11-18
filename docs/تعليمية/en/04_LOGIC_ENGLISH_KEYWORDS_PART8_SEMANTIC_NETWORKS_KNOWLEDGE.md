# Logic in Bayan Language (8): Semantic Networks, Knowledge, and Meanings

> In this part we enter **the world of meaning and knowledge** in Bayan:
> - Meaning networks `meaning`.
> - Cognitive information `information`.
> - Inference rules `inference_rule`.
> - Detecting contradictions `contradiction between`.
> - Evolving knowledge, ontology, semantic memory, and similarity.
>
> We will keep examples fully English in names and data, using the English keywords provided by the interpreter.

## 1. Meaning Networks: `meaning`

A meaning network represents **the meaning of an entity** (person, thing, concept) as a dictionary of relations.

### 1.1 Simple Example: Meaning of a Student

```bayan
meaning Mohammed:
{
    "is": "student",
    "studies": "mathematics",
    "age": 20
}

meaning Ali:
{
    "is": "student",
    "studies": "programming",
    "age": 22
}
```

### 1.2 Logic Query Over Meaning Network

We can write logic rules that use `meaning` as an implicit relation, for example to search for who studies a certain subject:

```bayan
hybrid {
    who_studies(?person, ?subject) :- meaning ?person: {"studies": ?subject}.
}

query who_studies(?person, "mathematics")?
```

> The precise internal syntax for `meaning ?person: {...}` is determined by the interpreter, but the educational idea here is that **the meaning network** can be used inside English logic rules.

## 2. Cognitive Information: `information`

`information` stores content + context (time, place, source, certainty).

### 2.1 Example: «Earth is spherical» with English Context

```bayan
information "Earth is spherical":
{
    "content": {"shape": "spherical", "diameter": 12742},
    "context": {
        "time": "2024",
        "place": "astronomy",
        "source": "observatory",
        "certainty": 0.99
    }
}
```

We can later use this information in reasoning, or compare its certainty with other information.

## 3. Inference Rules: `inference_rule` and `infer_from`

**Inference rules** allow us to derive new knowledge from existing information.

### 3.1 Example: «A student who studies mathematics is smart»

```bayan
inference_rule "If a student studies mathematics then they are smart":
{
    "if": ["studies", "mathematics"],
    "then": {"smart": 1}
}

information "Mohammed studies mathematics":
{
    "content": {"name": "Mohammed", "studies": "mathematics"},
    "context": {"certainty": 0.9}
}

infer_from: "Mohammed studies mathematics"  # infers that Mohammed is smart
```

The goal here is educational: to see how the rule is written in English, and how English information is used as a basis for inference.

## 4. Detecting Contradictions: `contradiction between`

Bayan can examine a list of information and search for contradictions between them based on certainty degree.

### 4.1 Example: «Earth is flat» vs «Earth is spherical»

```bayan
information "Earth is flat":
{
    "content": {"shape": "flat"},
    "context": {"certainty": 0.1}
}

information "Earth is spherical":
{
    "content": {"shape": "spherical"},
    "context": {"certainty": 0.99}
}

contradiction between: ["Earth is flat", "Earth is spherical"]
# The system chooses the information with higher certainty (Earth is spherical)
```

This connects semantic programming with what we saw in **probabilities and uncertainty**: certainty (0..1) enters into the decision of which information to rely on.

## 5. Evolving Knowledge: `evolving_knowledge`

`evolving_knowledge` allows tracking how knowledge changes over time.

### 5.1 Example: Evolution of Our Understanding of the Universe

```bayan
evolving_knowledge "our understanding of the universe":
{
    "current_value": "Big Bang theory",
    "history": [
        {"time": "17th century", "value": "static universe"},
        {"time": "20th century", "value": "expanding universe"}
    ],
    "future_prediction": "more precise theories"
}
```

This can later be linked to the world of causes (causal networks) or to the «idea–event–result» model.

## 6. Ontology, Semantic Memory, and Similarity

We won't go too deep here, but we'll show quick English examples to illustrate the picture.

### 6.1 Simple Ontology for Living Beings

```bayan
ontology "living beings":
{
    "root": "living being",
    "classification": {
        "animal": {
            "mammals": ["cat", "dog", "human"],
            "birds": ["sparrow", "eagle"]
        },
        "plant": {
            "trees": ["palm", "pine"],
            "flowers": ["rose", "jasmine"]
        }
    }
}
```

### 6.2 Personal Semantic Memory

```bayan
semantic_memory "my memories":
{
    "storage": {
        "event1": "graduated from university",
        "event2": "visited Mecca",
        "event3": "learned Bayan language"
    },
    "retrieval": "event1"
}
```

### 6.3 Semantic Similarity Between Two Concepts

```bayan
concept "cat":
{
    "type": "animal",
    "size": "small",
    "sound": "meow"
}

concept "dog":
{
    "type": "animal",
    "size": "medium",
    "sound": "bark"
}

similarity_degree = similarity("cat", "dog")  # approximate value between 0 and 1
```

- Here we see **semantic similarity** built on features (type, size, sound...).
- In part (9) we will see a general similarity layer `similar/5` that this `similarity` function can benefit from,
  to link synonyms and meanings in `meaning` and `concept` networks.

## 7. Linking Semantic Programming to Other Parts

- **meaning / information / evolving_knowledge** provide a «meaning and knowledge» layer over:
  - Classical logic (facts and rules).
  - Probabilities and uncertainty (certainty degrees).
  - Entities, states, and actions (what happens in the world).
  - Causal networks (why it happens).
- All of this with a **fully English** interface, keeping technical details internal.

With this part, the big picture is complete: we don't just have objects, states, causes, and probabilities, but also **meaning networks and semantic knowledge** that can be reasoned from, their contradictions detected, and their evolution tracked over time.

