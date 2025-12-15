# Tezniti 3D System Reference | مرجع نظام تزنيتي 3D

> **Version**: 2.0 (Enhanced AI Edition)
> **Date**: 2025-12-15

---

## 1. System Architecture | بنية النظام

Tezniti 3D connects a Kivy-based Frontend to a sophisticated AI Backend ("Cognitive Bridge").

```mermaid
graph TD
    User[User / Input] -->|Text/Voice| Interface[Tezniti UI]
    Interface -->|Natural Language| Bridge[AI Bridge]
    
    subgraph "The Brain (Bayan)"
        Bridge -->|Try| Engine[Istinbat Engine]
        Engine -.->|Fallback| Mock[Rule-Based Classifier]
        Bridge -->|Lookup| Vocab[Vocabulary System (key.md)]
    end
    
    Bridge -->|Shape Equation| Generator[3D Generator]
    Generator -->|Mesh| Viewer[3D Viewer]
```

### Components
1.  **UI (`tezniti_3d.py`)**: Handles user interaction, visualization, and parameter inputs.
2.  **AI Bridge (`ai_bridge.py`)**: The "Brain". Translates intent -> math.
    -   *Logic*: Uses `IstinbatEngine` (Bayan) or robust rules.
    -   *Vocabulary*: Dynamically loads terms from `key.md`.
    -   *Semantics*: Understands modifiers ("Heavy", "Precision").
3.  **Template Library (`template_library.py`)**: Standard parts catalog (ISO/DIN).

---

## 2. Capabilities & Shapes | القدرات والأشكال

Tezniti supports over **25 parametric mechanical shapes**.

### New in v2.0
| Shape | Arabic | Keywords |
|-------|--------|----------|
| **Spring** | نابض (زنبرك) | `spring`, `coil`, `compression` |
| **Pulley** | بكرة | `pulley`, `sheave`, `belt` |

### Standard Mechanical Parts
-   **Gears**: Spur, Helical, Bevel, Worm, Rack & Pinion.
-   **Transmission**: Shafts (with Keyways), Couplings, Bearings.
-   **Fasteners**: Bolts (Hex), Nuts, Washers (Flat).
-   **Structure**: Beams (I-Beam), Pipes, Flanges, Brackets (L & Mounting).
-   **Housing**: Enclosures, Gearbox casings.

### Furniture & Panels
-   **Furniture**: Chairs, Table Tops, Shelves.
-   **Panels**: Curved panels, Plates.

---

## 3. Artificial Intelligence | الذكاء الاصطناعي

### A. Semantic Logic (Deep AI)
Tezniti understands *qualitative* descriptions and modifies parameters automatically.

| Adjective | Effect | Logic |
|-----------|--------|-------|
| **"Heavy Duty"**, **"Strong"** | **Strength Boost** | Increases `thickness` (x1.5), `module` (x1.25), `wire_diameter` (x1.4). |
| **"Precision"**, **"Fine"** | **Resolution Boost** | Decreases `module` (x0.8) for finer teeth/threads. |

### B. Integrated Vocabulary (`key.md`)
The system dynamically loads external vocabulary.
-   **Materials**: Recognizes 80+ materials (e.g., *Titanium Alloy, Carbon Fiber v2*).
-   **Context**: If a recognized material is mentioned, it is automatically assigned to the `material` parameter.

---

## 4. Developer Guide | دليل المطور

### Adding a New Shape
1.  **Define Geometry**: Add `create_newshape(params)` in `tezniti_3d.py`.
2.  **Update Dispatcher**: Add logic in `generate_model` (e.g., `elif type == 'newshape'`).
3.  **Update AI**: Add keyword detection in `ai_bridge.py`.

### Running Verification
Use the built-in verification script to test logic without GUI:
```bash
python3 verify_tezniti_v2.py
```
*Tests: Classification correctness, Semantic modifier logic, Vocabulary loading.*

---

## 5. API Reference

### `TeznitiIntelligenceBridge`
-   `understand_request(text)`: Main entry point. Returns `ShapeEquation`.
-   `_classify_rule_based(text)`: Fallback logic with Regex.
-   `_apply_semantic_modifiers(text, params)`: Applies logic like "Heavy Duty".

### `TemplateLibrary`
-   `get(id)`: Retrieve standard part.
-   `search(query)`: Fuzzy search for parts.
