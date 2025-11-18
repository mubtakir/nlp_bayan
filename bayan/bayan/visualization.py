"""
Existential Model Visualization Tools
أدوات تصور النموذج الوجودي

This module provides visualization functions for the existential model:
- Environment visualization
- Relations graph visualization
- Beings in context visualization
- Domain overview visualization
"""

import json
from typing import Dict, List, Any, Optional


class ExistentialVisualizer:
    """Visualizer for existential model components"""
    
    def __init__(self, interpreter):
        """Initialize visualizer with interpreter instance"""
        self.interpreter = interpreter
        self.domains = getattr(interpreter, '_domains', {})
        self.environments = getattr(interpreter, '_environments', {})
        self.existential_beings = getattr(interpreter, '_existential_beings', {})
        self.domain_relations = getattr(interpreter, '_domain_relations', {})
        self.domain_actions = getattr(interpreter, '_domain_actions', {})
        self.domain_laws = getattr(interpreter, '_domain_laws', {})
    
    def visualize_environment(self, env_name: str) -> str:
        """
        Visualize an environment with its dimensions
        تصور بيئة مع أبعادها
        
        Returns Mermaid diagram code
        """
        if env_name not in self.environments:
            return f"Error: Environment '{env_name}' not found"

        env = self.environments[env_name]
        domain_name = env.get('_domain', env.get('domain', 'Unknown'))
        dimensions = env.get('أبعاد', env.get('dimensions', {}))
        
        # Build Mermaid diagram
        mermaid = ["graph TD"]
        mermaid.append(f'    ENV["{env_name}<br/>البيئة"]')
        mermaid.append(f'    DOMAIN["المجال: {domain_name}"]')
        mermaid.append('    ENV --> DOMAIN')
        
        # Add dimensions
        spatial = dimensions.get('spatial', dimensions.get('مكاني', {}))
        temporal = dimensions.get('temporal', dimensions.get('زماني', {}))
        domain_specific = dimensions.get('domain_specific', dimensions.get('مجالي', {}))
        
        if spatial:
            mermaid.append('    SPATIAL["🧭 أبعاد مكانية<br/>Spatial Dimensions"]')
            mermaid.append('    ENV --> SPATIAL')
            for key, value in spatial.items():
                safe_key = str(key).replace('"', "'")
                safe_value = str(value).replace('"', "'")
                mermaid.append(f'    SPATIAL --> S{hash(key) % 10000}["{safe_key}: {safe_value}"]')
        
        if temporal:
            mermaid.append('    TEMPORAL["⏰ أبعاد زمانية<br/>Temporal Dimensions"]')
            mermaid.append('    ENV --> TEMPORAL')
            for key, value in temporal.items():
                safe_key = str(key).replace('"', "'")
                safe_value = str(value).replace('"', "'")
                mermaid.append(f'    TEMPORAL --> T{hash(key) % 10000}["{safe_key}: {safe_value}"]')
        
        if domain_specific:
            mermaid.append('    DSPECIFIC["🔬 أبعاد مجالية<br/>Domain-Specific Dimensions"]')
            mermaid.append('    ENV --> DSPECIFIC')
            for key, value in domain_specific.items():
                safe_key = str(key).replace('"', "'")
                safe_value = str(value).replace('"', "'")
                mermaid.append(f'    DSPECIFIC --> D{hash(key) % 10000}["{safe_key}: {safe_value}"]')
        
        return '\n'.join(mermaid)
    
    def visualize_relations(self, domain_name: Optional[str] = None) -> str:
        """
        Visualize relations between beings as a graph
        تصور العلاقات بين الكائنات كرسم بياني
        
        Returns Mermaid diagram code
        """
        mermaid = ["graph LR"]
        
        # Filter beings by domain if specified
        beings_to_show = {}
        for being_name, being_config in self.existential_beings.items():
            being_domain = being_config.get('_domain', being_config.get('domain', being_config.get('مجال')))
            if domain_name is None or being_domain == domain_name:
                beings_to_show[being_name] = being_config
        
        if not beings_to_show:
            return f"Error: No beings found" + (f" in domain '{domain_name}'" if domain_name else "")
        
        # Add beings as nodes
        for being_name in beings_to_show:
            safe_name = being_name.replace('"', "'")
            mermaid.append(f'    {self._node_id(being_name)}["{safe_name}"]')
        
        # Add relations as edges
        for being_name, being_config in beings_to_show.items():
            relations = being_config.get('relations', being_config.get('علاقات', {}))
            for rel_type, targets in relations.items():
                if isinstance(targets, list):
                    for target in targets:
                        if target in beings_to_show:
                            safe_rel = str(rel_type).replace('"', "'")
                            mermaid.append(
                                f'    {self._node_id(being_name)} -->|"{safe_rel}"| {self._node_id(target)}'
                            )
        
        return '\n'.join(mermaid)
    
    def _node_id(self, name: str) -> str:
        """Generate a safe node ID from a name"""
        # Use hash to create a valid Mermaid node ID
        return f"N{abs(hash(name)) % 100000}"
    
    def visualize_being(self, being_name: str) -> str:
        """
        Visualize a being with its properties, relations, and environment
        تصور كائن مع خصائصه وعلاقاته وبيئته
        
        Returns Mermaid diagram code
        """
        if being_name not in self.existential_beings:
            return f"Error: Being '{being_name}' not found"
        
        being = self.existential_beings[being_name]
        
        mermaid = ["graph TD"]
        safe_name = being_name.replace('"', "'")
        mermaid.append(f'    BEING["🌟 {safe_name}<br/>الكائن الوجودي"]')
        
        # Add type
        being_type = being.get('_type', being.get('type', being.get('نوع', 'Unknown')))
        mermaid.append(f'    TYPE["النوع: {being_type}"]')
        mermaid.append('    BEING --> TYPE')

        # Add environment
        env_name = being.get('بيئة', being.get('environment', 'Unknown'))
        mermaid.append(f'    ENV["🌍 البيئة: {env_name}"]')
        mermaid.append('    BEING --> ENV')

        # Add domain
        domain_name = being.get('_domain', being.get('domain', being.get('مجال', 'Unknown')))
        mermaid.append(f'    DOMAIN["📚 المجال: {domain_name}"]')
        mermaid.append('    BEING --> DOMAIN')

        # Add intrinsic properties
        intrinsic_props = being.get('intrinsic_properties', being.get('خصائص_ذاتية', {}))
        if intrinsic_props:
            mermaid.append('    PROPS["⚙️ خصائص ذاتية<br/>Intrinsic Properties"]')
            mermaid.append('    BEING --> PROPS')
            for key, value in list(intrinsic_props.items())[:5]:  # Limit to 5 properties
                safe_key = str(key).replace('"', "'")
                safe_value = str(value).replace('"', "'")
                if len(safe_value) > 30:
                    safe_value = safe_value[:27] + "..."
                mermaid.append(f'    PROPS --> P{hash(key) % 10000}["{safe_key}: {safe_value}"]')

        # Add relations
        relations = being.get('relations', being.get('علاقات', {}))
        if relations:
            mermaid.append('    RELS["🔗 علاقات<br/>Relations"]')
            mermaid.append('    BEING --> RELS')
            for rel_type, targets in list(relations.items())[:5]:  # Limit to 5 relations
                safe_rel = str(rel_type).replace('"', "'")
                if isinstance(targets, list):
                    targets_str = ", ".join(str(t) for t in targets[:3])
                    if len(targets) > 3:
                        targets_str += "..."
                else:
                    targets_str = str(targets)
                mermaid.append(f'    RELS --> R{hash(rel_type) % 10000}["{safe_rel}: {targets_str}"]')

        # Add intrinsic meanings
        intrinsic_meanings = being.get('intrinsic_meanings', being.get('معانٍ_ذاتية', []))
        if intrinsic_meanings:
            mermaid.append('    MEANINGS["💡 معانٍ ذاتية<br/>Intrinsic Meanings"]')
            mermaid.append('    BEING --> MEANINGS')
            for meaning in intrinsic_meanings[:5]:  # Limit to 5 meanings
                safe_meaning = str(meaning).replace('"', "'")
                mermaid.append(f'    MEANINGS --> M{hash(meaning) % 10000}["{safe_meaning}"]')

        return '\n'.join(mermaid)

    def visualize_domain(self, domain_name: str) -> str:
        """
        Visualize entire domain with all beings, relations, and laws
        تصور المجال الكامل مع جميع الكائنات والعلاقات والقوانين

        Returns Mermaid diagram code
        """
        if domain_name not in self.domains:
            return f"Error: Domain '{domain_name}' not found"

        domain = self.domains[domain_name]

        mermaid = ["graph TD"]
        safe_domain = domain_name.replace('"', "'")
        mermaid.append(f'    DOMAIN["📚 {safe_domain}<br/>المجال"]')

        # Add basic entity
        basic_entity = domain.get('basic_entity', domain.get('كائن_أساسي', 'Unknown'))
        mermaid.append(f'    ENTITY["الكائن الأساسي: {basic_entity}"]')
        mermaid.append('    DOMAIN --> ENTITY')

        # Add environment
        env_name = domain.get('environment', domain.get('بيئة', 'Unknown'))
        mermaid.append(f'    ENV["البيئة: {env_name}"]')
        mermaid.append('    DOMAIN --> ENV')

        # Count beings in this domain
        beings_count = sum(
            1 for b in self.existential_beings.values()
            if b.get('_domain', b.get('domain', b.get('مجال'))) == domain_name
        )
        mermaid.append(f'    BEINGS["👥 كائنات: {beings_count}"]')
        mermaid.append('    DOMAIN --> BEINGS')

        # Count relations in this domain
        relations_count = sum(
            1 for r in self.domain_relations.values()
            if r.get('_domain', r.get('domain', r.get('مجال'))) == domain_name
        )
        mermaid.append(f'    RELATIONS["🔗 علاقات: {relations_count}"]')
        mermaid.append('    DOMAIN --> RELATIONS')

        # Count actions in this domain
        actions_count = sum(
            1 for a in self.domain_actions.values()
            if a.get('_domain', a.get('domain', a.get('مجال'))) == domain_name
        )
        mermaid.append(f'    ACTIONS["⚡ أفعال: {actions_count}"]')
        mermaid.append('    DOMAIN --> ACTIONS')

        # Count laws in this domain
        laws_count = sum(
            1 for l in self.domain_laws.values()
            if l.get('_domain', l.get('domain', l.get('مجال'))) == domain_name
        )
        mermaid.append(f'    LAWS["⚖️ قوانين: {laws_count}"]')
        mermaid.append('    DOMAIN --> LAWS')

        # Add basic meanings
        basic_meanings = domain.get('basic_meanings', domain.get('معانٍ_أساسية', []))
        if basic_meanings:
            mermaid.append('    MEANINGS["💡 معانٍ أساسية"]')
            mermaid.append('    DOMAIN --> MEANINGS')
            for meaning in basic_meanings[:5]:  # Limit to 5
                safe_meaning = str(meaning).replace('"', "'")
                mermaid.append(f'    MEANINGS --> M{hash(meaning) % 10000}["{safe_meaning}"]')

        return '\n'.join(mermaid)

    def generate_html(self, mermaid_code: str, title: str = "Existential Model Visualization") -> str:
        """
        Generate HTML page with Mermaid diagram
        إنشاء صفحة HTML مع رسم Mermaid
        """
        html = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 20px;
            min-height: 100vh;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        }}
        h1 {{
            text-align: center;
            color: #667eea;
            margin-bottom: 30px;
            font-size: 2.5em;
        }}
        .mermaid {{
            text-align: center;
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
        }}
        .footer {{
            text-align: center;
            margin-top: 30px;
            color: #666;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{title}</h1>
        <div class="mermaid">
{mermaid_code}
        </div>
        <div class="footer">
            <p>Generated by Bayan - لغة البيان</p>
            <p>The World's First Philosophical Programming Language</p>
        </div>
    </div>
    <script>
        mermaid.initialize({{ startOnLoad: true, theme: 'default' }});
    </script>
</body>
</html>"""
        return html

