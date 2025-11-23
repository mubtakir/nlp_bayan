import pytest
from bayan.libraries.arabic_nlp_lib import segment, pos_tag, extract_entities

def test_segmentation():
    text = "بالسيارة"
    result = segment(text)
    assert len(result) == 1
    assert result[0]['prefix'] == "بال"
    assert result[0]['stem'] == "سيارة" or result[0]['stem'] == "سيار" # Depending on suffix logic
    # "بالسيارة" -> prefix="بال", stem="سيارة" (if suffix not matched) or stem="سيار"+suffix="ة"
    # Let's check logic: "بال" len 3. stem "سيارة". suffix "ة" len 1.
    # stem "سيار".
    assert result[0]['suffix'] == "ة"

def test_pos_tag():
    text = "الولد يلعب في الحديقة"
    tags = pos_tag(text)
    assert len(tags) == 4
    assert tags[0]['tag'] == "NOUN" # الولد
    assert tags[1]['tag'] == "VERB" # يلعب
    assert tags[2]['tag'] == "PART" # في
    assert tags[3]['tag'] == "NOUN" # الحديقة

def test_ner():
    text = "سافر الدكتور أحمد إلى الرياض"
    entities = extract_entities(text)
    assert len(entities) == 2
    
    # Order depends on loop, but usually sequential
    assert entities[0]['type'] == "PERSON"
    assert "الدكتور أحمد" in entities[0]['text']
    
    assert entities[1]['type'] == "LOCATION"
    assert "الرياض" in entities[1]['text']
