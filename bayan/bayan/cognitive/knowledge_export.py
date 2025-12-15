"""
تصدير المعرفة - Knowledge Export
================================

تصدير قاعدة المعرفة بصيغ متعددة.

الصيغ المدعومة:
- JSON: للـ APIs
- RDF/OWL: للويب الدلالي
- YAML: للتكوين
- Markdown: للتوثيق

المطور: باسل يحيى عبدالله
"""

import sys
import os
import json
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict
from datetime import datetime

# Ensure we can import bayan packages
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from bayan.bayan.istinbat_engine import IstinbatEngine
from bayan.bayan.logical_engine import Fact, Predicate


class JSONExporter:
    """مصدّر JSON"""
    
    def export(self, knowledge: Dict[str, Any]) -> str:
        """تصدير لـ JSON"""
        return json.dumps(knowledge, ensure_ascii=False, indent=2)
    
    def export_to_file(self, knowledge: Dict[str, Any], filepath: str):
        """تصدير لملف JSON"""
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(knowledge, f, ensure_ascii=False, indent=2)


class RDFExporter:
    """مصدّر RDF/Turtle"""
    
    def __init__(self):
        self.prefixes = {
            "bayan": "http://bayan.ai/ontology#",
            "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
            "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
            "owl": "http://www.w3.org/2002/07/owl#"
        }
    
    def export(self, facts: List[Dict[str, Any]], rules: List[Dict[str, Any]] = None) -> str:
        """تصدير لـ RDF/Turtle"""
        lines = []
        
        # Prefixes
        for prefix, uri in self.prefixes.items():
            lines.append(f"@prefix {prefix}: <{uri}> .")
        lines.append("")
        
        # Facts
        lines.append("# الحقائق / Facts")
        for fact in facts:
            subject = self._sanitize(fact.get('subject', 'unknown'))
            predicate = self._sanitize(fact.get('predicate', 'related_to'))
            obj = fact.get('object')
            
            if obj:
                obj = self._sanitize(obj)
                lines.append(f"bayan:{subject} bayan:{predicate} bayan:{obj} .")
            else:
                lines.append(f"bayan:{subject} a bayan:{predicate} .")
        
        lines.append("")
        
        # Rules
        if rules:
            lines.append("# القواعد / Rules")
            for i, rule in enumerate(rules):
                condition = self._sanitize(rule.get('condition', 'condition'))
                conclusion = self._sanitize(rule.get('conclusion', 'conclusion'))
                lines.append(f"bayan:Rule{i} a bayan:Rule ;")
                lines.append(f"    bayan:hasCondition bayan:{condition} ;")
                lines.append(f"    bayan:hasConclusion bayan:{conclusion} .")
        
        return "\n".join(lines)
    
    def _sanitize(self, text: str) -> str:
        """تنظيف النص للـ RDF"""
        # إزالة الأحرف غير المسموحة
        text = text.replace(" ", "_").replace("'", "").replace('"', "")
        return text
    
    def export_to_file(self, facts: List[Dict], rules: List[Dict], filepath: str):
        """تصدير لملف Turtle"""
        content = self.export(facts, rules)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)


class OWLExporter:
    """مصدّر OWL"""
    
    def export(self, concepts: List[str], relations: List[Dict[str, Any]]) -> str:
        """تصدير لـ OWL/XML"""
        lines = [
            '<?xml version="1.0"?>',
            '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"',
            '         xmlns:owl="http://www.w3.org/2002/07/owl#"',
            '         xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"',
            '         xmlns:bayan="http://bayan.ai/ontology#">',
            '',
            '  <owl:Ontology rdf:about="http://bayan.ai/ontology"/>',
            ''
        ]
        
        # Classes
        for concept in concepts:
            concept_id = concept.replace(" ", "_")
            lines.append(f'  <owl:Class rdf:about="http://bayan.ai/ontology#{concept_id}">')
            lines.append(f'    <rdfs:label>{concept}</rdfs:label>')
            lines.append('  </owl:Class>')
            lines.append('')
        
        # Object Properties
        for rel in relations:
            prop_name = rel.get('predicate', 'related_to').replace(" ", "_")
            lines.append(f'  <owl:ObjectProperty rdf:about="http://bayan.ai/ontology#{prop_name}">')
            lines.append(f'    <rdfs:label>{rel.get("predicate", "related_to")}</rdfs:label>')
            lines.append('  </owl:ObjectProperty>')
            lines.append('')
        
        lines.append('</rdf:RDF>')
        return "\n".join(lines)
    
    def export_to_file(self, concepts: List[str], relations: List[Dict], filepath: str):
        """تصدير لملف OWL"""
        content = self.export(concepts, relations)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)


class YAMLExporter:
    """مصدّر YAML"""
    
    def export(self, knowledge: Dict[str, Any]) -> str:
        """تصدير لـ YAML"""
        try:
            import yaml
            return yaml.dump(knowledge, allow_unicode=True, default_flow_style=False)
        except ImportError:
            # Fallback بسيط
            return self._simple_yaml(knowledge)
    
    def _simple_yaml(self, data: Any, indent: int = 0) -> str:
        """تحويل بسيط لـ YAML"""
        lines = []
        prefix = "  " * indent
        
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, (dict, list)):
                    lines.append(f"{prefix}{key}:")
                    lines.append(self._simple_yaml(value, indent + 1))
                else:
                    lines.append(f"{prefix}{key}: {value}")
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    lines.append(f"{prefix}-")
                    lines.append(self._simple_yaml(item, indent + 1))
                else:
                    lines.append(f"{prefix}- {item}")
        else:
            lines.append(f"{prefix}{data}")
        
        return "\n".join(lines)
    
    def export_to_file(self, knowledge: Dict[str, Any], filepath: str):
        """تصدير لملف YAML"""
        content = self.export(knowledge)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)


class MarkdownExporter:
    """مصدّر Markdown للتوثيق"""
    
    def export(self, knowledge: Dict[str, Any], title: str = "قاعدة المعرفة") -> str:
        """تصدير لـ Markdown"""
        lines = [
            f"# {title}",
            "",
            f"تاريخ التصدير: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "",
        ]
        
        # الحقائق
        facts = knowledge.get("facts", [])
        if facts:
            lines.append("## الحقائق")
            lines.append("")
            lines.append("| الموضوع | العلاقة | الكائن |")
            lines.append("|---------|---------|--------|")
            for fact in facts:
                subject = fact.get("subject", "-")
                predicate = fact.get("predicate", "-")
                obj = fact.get("object", "-")
                lines.append(f"| {subject} | {predicate} | {obj} |")
            lines.append("")
        
        # القواعد
        rules = knowledge.get("rules", [])
        if rules:
            lines.append("## القواعد")
            lines.append("")
            for i, rule in enumerate(rules, 1):
                condition = rule.get("condition", "شرط")
                conclusion = rule.get("conclusion", "استنتاج")
                confidence = rule.get("confidence", 0)
                lines.append(f"{i}. **إذا** {condition} **فإن** {conclusion}")
                lines.append(f"   - الثقة: {confidence:.2f}")
            lines.append("")
        
        # الإحصائيات
        stats = knowledge.get("stats", {})
        if stats:
            lines.append("## الإحصائيات")
            lines.append("")
            for key, value in stats.items():
                lines.append(f"- **{key}**: {value}")
        
        return "\n".join(lines)
    
    def export_to_file(self, knowledge: Dict[str, Any], filepath: str, title: str = "قاعدة المعرفة"):
        """تصدير لملف Markdown"""
        content = self.export(knowledge, title)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)


class KnowledgeExporter:
    """
    مصدّر المعرفة الموحد
    
    يجمع كل أنواع التصدير في واجهة واحدة.
    """
    
    def __init__(self, engine: Optional[IstinbatEngine] = None):
        self.engine = engine or IstinbatEngine()
        self.json_exporter = JSONExporter()
        self.rdf_exporter = RDFExporter()
        self.owl_exporter = OWLExporter()
        self.yaml_exporter = YAMLExporter()
        self.md_exporter = MarkdownExporter()
    
    def extract_knowledge(self) -> Dict[str, Any]:
        """استخراج المعرفة من المحرك"""
        knowledge = {
            "facts": [],
            "rules": [],
            "concepts": [],
            "relations": [],
            "stats": {},
            "metadata": {
                "exported_at": datetime.now().isoformat(),
                "engine_version": "1.0"
            }
        }
        
        # استخراج الحقائق
        try:
            kb = self.engine.logical_engine.knowledge_base
            for fact in kb.facts:
                fact_dict = {
                    "predicate": fact.predicate.name,
                    "subject": str(fact.predicate.args[0]) if fact.predicate.args else "",
                    "object": str(fact.predicate.args[1]) if len(fact.predicate.args) > 1 else None
                }
                knowledge["facts"].append(fact_dict)
                
                # إضافة للمفاهيم
                if fact_dict["subject"] and fact_dict["subject"] not in knowledge["concepts"]:
                    knowledge["concepts"].append(fact_dict["subject"])
                if fact_dict["object"] and fact_dict["object"] not in knowledge["concepts"]:
                    knowledge["concepts"].append(fact_dict["object"])
        except:
            pass
        
        # استخراج القواعد
        try:
            for rule in kb.rules:
                rule_dict = {
                    "condition": str(rule.body[0]) if rule.body else "",
                    "conclusion": str(rule.head),
                    "confidence": 0.8
                }
                knowledge["rules"].append(rule_dict)
        except:
            pass
        
        # الإحصائيات
        knowledge["stats"] = {
            "total_facts": len(knowledge["facts"]),
            "total_rules": len(knowledge["rules"]),
            "total_concepts": len(knowledge["concepts"])
        }
        
        return knowledge
    
    def export_json(self, filepath: str = None) -> str:
        """تصدير JSON"""
        knowledge = self.extract_knowledge()
        content = self.json_exporter.export(knowledge)
        if filepath:
            self.json_exporter.export_to_file(knowledge, filepath)
        return content
    
    def export_rdf(self, filepath: str = None) -> str:
        """تصدير RDF/Turtle"""
        knowledge = self.extract_knowledge()
        content = self.rdf_exporter.export(knowledge["facts"], knowledge["rules"])
        if filepath:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        return content
    
    def export_owl(self, filepath: str = None) -> str:
        """تصدير OWL"""
        knowledge = self.extract_knowledge()
        content = self.owl_exporter.export(knowledge["concepts"], knowledge["facts"])
        if filepath:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        return content
    
    def export_yaml(self, filepath: str = None) -> str:
        """تصدير YAML"""
        knowledge = self.extract_knowledge()
        content = self.yaml_exporter.export(knowledge)
        if filepath:
            self.yaml_exporter.export_to_file(knowledge, filepath)
        return content
    
    def export_markdown(self, filepath: str = None, title: str = "قاعدة المعرفة") -> str:
        """تصدير Markdown"""
        knowledge = self.extract_knowledge()
        content = self.md_exporter.export(knowledge, title)
        if filepath:
            self.md_exporter.export_to_file(knowledge, filepath, title)
        return content
    
    def export_all(self, base_path: str, base_name: str = "knowledge"):
        """تصدير بكل الصيغ"""
        self.export_json(f"{base_path}/{base_name}.json")
        self.export_rdf(f"{base_path}/{base_name}.ttl")
        self.export_owl(f"{base_path}/{base_name}.owl")
        self.export_yaml(f"{base_path}/{base_name}.yaml")
        self.export_markdown(f"{base_path}/{base_name}.md")
        
        return {
            "json": f"{base_path}/{base_name}.json",
            "rdf": f"{base_path}/{base_name}.ttl",
            "owl": f"{base_path}/{base_name}.owl",
            "yaml": f"{base_path}/{base_name}.yaml",
            "markdown": f"{base_path}/{base_name}.md"
        }


# ============ اختبار ============
if __name__ == "__main__":
    print("=" * 50)
    print("اختبار تصدير المعرفة")
    print("=" * 50)
    
    exporter = KnowledgeExporter()
    
    # إضافة بعض الحقائق للاختبار
    from bayan.bayan.logical_engine import Fact, Predicate, Term
    exporter.engine.logical_engine.add_fact(
        Fact(Predicate("is_a", [Term("الذكاء_الاصطناعي"), Term("علم")]))
    )
    exporter.engine.logical_engine.add_fact(
        Fact(Predicate("has_property", [Term("بايثون"), Term("سهولة")]))
    )
    
    # اختبار JSON
    print("\n1. تصدير JSON:")
    json_content = exporter.export_json()
    print(json_content[:200] + "...")
    
    # اختبار RDF
    print("\n2. تصدير RDF:")
    rdf_content = exporter.export_rdf()
    print(rdf_content[:300] + "...")
    
    # اختبار Markdown
    print("\n3. تصدير Markdown:")
    md_content = exporter.export_markdown()
    print(md_content[:300] + "...")
    
    print("\n✅ اكتمل الاختبار بنجاح!")
