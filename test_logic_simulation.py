
import re
from dataclasses import dataclass, field
from typing import Dict, Any, List

# --- MOCK CLASSES ---
@dataclass
class ShapeEquation:
    equation_type: str
    parameters: Dict[str, Any]
    confidence: float
    reasoning: str

@dataclass
class MockEquation:
    event: str = "create"
    entities: dict = field(default_factory=dict)
    
@dataclass
class MockResult:
    equation: MockEquation = field(default_factory=MockEquation)
    dialect: str = "Standard"

# --- CORE LOGIC EXTRACTED FROM AI_BRIDGE.PY ---
def understand_request_logic(text_prompt: str):
    print(f"Analyzing: {text_prompt}")
    
    # Mocking NLP output (Assuming Bayan parser extracts entities if present)
    # For now, we rely on the keyword extraction logic inside the function which falls back to `text_lower`
    linguistic_concepts = [] 
    
    text_lower = text_prompt.lower()
    
    # -- Detect Type --
    # Use Equation Event/Entities to determine type
    is_gear = any(k in ['rotate', 'turn', 'mesh', 'gear', 'ترس', 'دوران'] for k in linguistic_concepts) or 'gear' in text_lower or 'ترس' in text_lower
    is_bearing = any(k in ['bearing', 'roll', 'crub', 'رومان', 'بلي'] for k in linguistic_concepts) or 'bearing' in text_lower
    is_bolt = any(k in ['thread', 'fasten', 'screw', 'bolt', 'vis', 'مسمار', 'برغي'] for k in linguistic_concepts) or 'bolt' in text_lower or 'screw' in text_lower
    
    # FIRST BATCH TYPES
    is_nut = any(k in ['nut', 'ecrou', 'صامولة', 'صموله'] for k in linguistic_concepts) or 'nut' in text_lower or 'صامولة' in text_lower or 'ecrou' in text_lower
    is_washer = any(k in ['washer', 'rondelle', 'حلقة', 'رونديل'] for k in linguistic_concepts) or 'washer' in text_lower or 'rondelle' in text_lower or 'حلقة' in text_lower
    is_shaft = any(k in ['shaft', 'arbre', 'عمود', 'axe'] for k in linguistic_concepts) or 'shaft' in text_lower or 'arbre' in text_lower or 'عمود' in text_lower
    is_pipe = any(k in ['pipe', 'tube', 'أنبوب', 'انبوب', 'tuyau'] for k in linguistic_concepts) or 'pipe' in text_lower or 'tube' in text_lower or 'أنبوب' in text_lower
    is_flange = any(k in ['flange', 'bride', 'فلنجة', 'شفة'] for k in linguistic_concepts) or 'flange' in text_lower or 'bride' in text_lower or 'فلنجة' in text_lower
    
    # EXTENDED TYPES
    is_spur_gear = 'spur' in text_lower or 'مستقيم' in text_lower
    is_bevel_gear = 'bevel' in text_lower or 'مخروطي' in text_lower or 'conique' in text_lower
    is_worm_gear = 'worm' in text_lower or 'دودي' in text_lower or 'vis sans fin' in text_lower
    is_pulley = any(k in ['pulley', 'poulie', 'بكرة', 'belt'] for k in linguistic_concepts) or 'pulley' in text_lower or 'poulie' in text_lower or 'بكرة' in text_lower
    is_rack = 'rack' in text_lower or 'pinion' in text_lower or 'جريدة' in text_lower or 'crémaillère' in text_lower
    is_hinge = any(k in ['hinge', 'charnière', 'مفصلة', 'pivot'] for k in linguistic_concepts) or 'hinge' in text_lower or 'مفصلة' in text_lower
    
    # --- DETECT BRACKET (UPDATED LOGIC) ---
    is_bracket = any(k in ['bracket', 'support', 'كتيفة', 'equerre'] for k in linguistic_concepts) or 'bracket' in text_lower or 'support' in text_lower or 'كتيفة' in text_lower or 'equerre' in text_lower
    
    is_beam = any(k in ['beam', 'poutre', 'عارضة', 'i-beam'] for k in linguistic_concepts) or 'beam' in text_lower or 'poutre' in text_lower or 'عارضة' in text_lower
    is_ball_screw = 'ball screw' in text_lower or 'برغي كروي' in text_lower or 'vis à billes' in text_lower
    is_lead_screw = 'lead screw' in text_lower or 'برغي قيادي' in text_lower or 'vis mère' in text_lower
    is_housing = any(k in ['housing', 'boîtier', 'غلاف', 'casing', 'enclosure'] for k in linguistic_concepts) or 'housing' in text_lower or 'غلاف' in text_lower or 'boitier' in text_lower
    is_spring = any(k in ['spring', 'ressort', 'نابض', 'زنبرك', 'coil'] for k in linguistic_concepts) or 'spring' in text_lower or 'نابض' in text_lower or 'ressort' in text_lower
    
    # NEW: Furniture and Panel types
    is_explicit_part = 'backrest panel' in text_lower or 'chair backrest' in text_lower or 'part of' in text_lower or 'component' in text_lower or 'only' in text_lower
    is_full_chair = ('chair' in text_lower or 'كرسي' in text_lower or 'seat' in text_lower) and not is_explicit_part
    is_curved_panel = 'backrest' in text_lower or 'curved panel' in text_lower or 'curved plate' in text_lower or 'ظهر' in text_lower
    is_plate = any(k in ['plate', 'plaque', 'صفيحة', 'لوح', 'sheet'] for k in linguistic_concepts) or 'plate' in text_lower or 'plaque' in text_lower or 'صفيحة' in text_lower
    is_table_top = 'table' in text_lower and ('top' in text_lower or 'surface' in text_lower) or 'سطح طاولة' in text_lower
    is_shelf = any(k in ['shelf', 'étagère', 'رف'] for k in linguistic_concepts) or 'shelf' in text_lower or 'رف' in text_lower
    
    shape_type = 'unknown'
    params = {}
    reasoning_parts = []
    
    # PRIORITY ORDER
    if is_full_chair:
        shape_type = 'chair'
    elif is_curved_panel:
        shape_type = 'curved_panel'
    elif is_plate:
        shape_type = 'plate'
    elif is_table_top:
        shape_type = 'table_top'
    elif is_shelf:
        shape_type = 'shelf'
        
    # HIGH PRIORITY: MOUNTING BRACKET
    elif is_bracket:
        # Check logic from ai_bridge.py
        has_bolt_holes = 'bolt hole' in text_lower or 'hole' in text_lower or 'ثقب' in text_lower
        has_vertical_arm = 'vertical' in text_lower or 'support arm' in text_lower or 'ذراع' in text_lower
        is_mounting = 'mounting' in text_lower or 'mount' in text_lower or 'تركيب' in text_lower
        
        if is_mounting or has_bolt_holes or has_vertical_arm:
            shape_type = 'mounting_bracket'
        else:
            shape_type = 'bracket'
            
    elif is_spur_gear: shape_type = 'spur_gear'
    elif is_bevel_gear: shape_type = 'bevel_gear'
    elif is_worm_gear: shape_type = 'worm_gear'
    elif is_gear: shape_type = 'helical_gear'
    elif is_pulley: shape_type = 'pulley'
    elif is_rack: shape_type = 'rack_and_pinion'
    elif is_ball_screw: shape_type = 'ball_screw'
    elif is_lead_screw: shape_type = 'lead_screw'
    elif is_hinge: shape_type = 'hinge'
    elif is_beam: shape_type = 'beam'
    elif is_housing: shape_type = 'housing'
    elif is_spring: shape_type = 'spring'
    elif is_nut: shape_type = 'nut'
    elif is_washer: shape_type = 'washer'
    elif is_shaft: shape_type = 'shaft'
    elif is_pipe: shape_type = 'pipe'
    elif is_flange: shape_type = 'flange'
    elif is_bearing: shape_type = 'bearing'
    elif is_bolt: shape_type = 'bolt'
    else:
        shape_type = 'box'

    return shape_type

if __name__ == "__main__":
    text = "Design a mechanical mounting bracket with a rectangular base of 120 mm length, 80 mm width, and 10 mm thickness. Add four bolt holes of 10 mm diameter, positioned 15 mm from each corner. Include a vertical support arm 80 mm high, 60 mm wide, and 10 mm thick."
    result = understand_request_logic(text)
    print(f"Final Shape Type: {result}")
    
    if result == 'mounting_bracket':
        print("✅ SUCCESS")
    else:
        print("❌ FAILURE")
