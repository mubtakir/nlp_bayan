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

    def export_d3_graph(self) -> Dict[str, Any]:
        """
        Export knowledge base as D3.js compatible JSON graph.
        Returns:
            {
                'nodes': [{'id': '...', 'group': 1, 'label': '...', 'type': 'concept'}],
                'links': [{'source': '...', 'target': '...', 'value': 1, 'relationship': '...'}]
            }
        """
        from .logical_engine import Fact, Rule
        
        nodes = {}
        links = []
        
        # Access the logical engine from the interpreter
        # Depending on interpreter type (Hybrid/Traditional), access path might vary
        logical_engine = getattr(self.interpreter, 'logical', None)
        if not logical_engine and hasattr(self.interpreter, 'logical_engine'):
            logical_engine = self.interpreter.logical_engine
            
        if not logical_engine:
            return {'nodes': [], 'links': []}
            
        # Iterate over all facts in the knowledge base
        for pred_name, items in logical_engine.knowledge_base.items():
            for item in items:
                if isinstance(item, Fact):
                    pred = item.predicate
                    args = pred.args
                    
                    # Heuristic: Binary predicates are links, Unary are properties/types
                    if len(args) == 2:
                        source = str(args[0])
                        target = str(args[1])
                        rel = pred.name
                        
                        # Add nodes
                        if source not in nodes:
                            nodes[source] = {'id': source, 'group': 1, 'label': source, 'type': 'concept'}
                        if target not in nodes:
                            nodes[target] = {'id': target, 'group': 1, 'label': target, 'type': 'concept'}
                            
                        # Add link
                        links.append({
                            'source': source,
                            'target': target,
                            'value': 1,
                            'relationship': rel,
                            'probability': item.probability
                        })
                        
                    elif len(args) == 1:
                        # Unary predicate: type(entity) or property(entity)
                        entity = str(args[0])
                        prop = pred.name
                        
                        if entity not in nodes:
                            nodes[entity] = {'id': entity, 'group': 1, 'label': entity, 'type': 'concept'}
                            
                        # We can represent this as a self-loop or just implicit property
                        # For visualization, maybe add a 'value' node?
                        # Let's add a value node for the property
                        val_id = f"{entity}_{prop}"
                        if val_id not in nodes:
                            nodes[val_id] = {'id': val_id, 'group': 3, 'label': prop, 'type': 'value'}
                        
                        links.append({
                            'source': entity,
                            'target': val_id,
                            'value': 1,
                            'relationship': 'is',
                            'probability': item.probability
                        })
                        
                    elif len(args) > 2:
                        # N-ary predicate: Create a central event node
                        # event_id = pred_name + "_" + hash(args)
                        event_id = f"{pred_name}_{abs(hash(str(args))) % 10000}"
                        if event_id not in nodes:
                            nodes[event_id] = {'id': event_id, 'group': 2, 'label': pred_name, 'type': 'logic'}
                            
                        for i, arg in enumerate(args):
                            arg_str = str(arg)
                            if arg_str not in nodes:
                                nodes[arg_str] = {'id': arg_str, 'group': 1, 'label': arg_str, 'type': 'concept'}
                                
                            links.append({
                                'relationship': f"arg{i+1}",
                                'probability': item.probability
                            })

                elif isinstance(item, Rule):
                    # Visualize Rule as a causal node
                    # Rule: head :- body
                    # We link body predicates (causes) to the rule node, and rule node to head predicate (effect)
                    
                    rule_id = f"rule_{pred_name}_{abs(hash(str(item))) % 10000}"
                    if rule_id not in nodes:
                        nodes[rule_id] = {'id': rule_id, 'group': 4, 'label': 'IMPLIES', 'type': 'rule'}
                        
                    # Head
                    head_pred = item.head.name
                    # Create a value node for the head predicate if it doesn't exist
                    head_val_id = f"val_{head_pred}"
                    if head_val_id not in nodes:
                        nodes[head_val_id] = {'id': head_val_id, 'group': 3, 'label': head_pred, 'type': 'value'}
                        
                    # Link Rule -> Head
                    links.append({
                        'source': rule_id,
                        'target': head_val_id,
                        'value': 1,
                        'relationship': 'causes'
                    })
                    
                    # Body
                    for goal in item.body:
                        goal_pred = goal.name
                        # Create value node for body predicate
                        body_val_id = f"val_{goal_pred}"
                        if body_val_id not in nodes:
                            nodes[body_val_id] = {'id': body_val_id, 'group': 3, 'label': goal_pred, 'type': 'value'}
                            
                        # Link Body -> Rule
                        links.append({
                            'source': body_val_id,
                            'target': rule_id,
                            'value': 1,
                            'relationship': 'condition'
                        })

        return {
            'nodes': list(nodes.values()),
            'links': links
        }

    def export_procedural_graph(self) -> Dict[str, Any]:
        """
        Export procedural functions and their calls as D3 graph
        تصدير الدوال الإجرائية واستدعاءاتها كرسم بياني
        """
        nodes = {}
        links = []
        
        # Get functions from global environment
        if hasattr(self.interpreter, 'traditional'):
            env = self.interpreter.traditional.global_env
            
            for name, value in env.items():
                # Check if it's a function (callable and has __name__)
                if callable(value) and hasattr(value, '__name__'):
                    # Skip built-in functions and special names
                    if name.startswith('_') or name in ['print', 'len', 'str', 'int', 'float']:
                        continue
                    
                    func_id = f"func_{name}"
                    nodes[func_id] = {
                        'id': func_id,
                        'label': name,
                        'group': 5,  # Yellow for functions
                        'type': 'function'
                    }
        
        return {'nodes': list(nodes.values()), 'links': links}

    def export_oop_graph(self) -> Dict[str, Any]:
        """
        Export OOP classes, inheritance, and objects as D3 graph
        تصدير الفئات والوراثة والكائنات كرسم بياني
        """
        nodes = {}
        links = []
        
        # Get classes from class system
        if hasattr(self.interpreter, 'traditional') and hasattr(self.interpreter.traditional, 'class_system'):
            class_system = self.interpreter.traditional.class_system
            
            # Add class nodes
            for class_name, class_def in class_system.classes.items():
                class_id = f"class_{class_name}"
                nodes[class_id] = {
                    'id': class_id,
                    'label': class_name,
                    'group': 6,  # Red for classes
                    'type': 'class'
                }
                
                # Add inheritance links
                if hasattr(class_def, 'base_classes') and class_def.base_classes:
                    for base in class_def.base_classes:
                        base_id = f"class_{base}"
                        # Ensure base class node exists
                        if base_id not in nodes and base in class_system.classes:
                            nodes[base_id] = {
                                'id': base_id,
                                'label': base,
                                'group': 6,
                                'type': 'class'
                            }
                        
                        links.append({
                            'source': class_id,
                            'target': base_id,
                            'value': 1,
                            'relationship': 'extends'
                        })
                elif hasattr(class_def, 'base_class') and class_def.base_class:
                    # Fallback to single base_class
                    base_id = f"class_{class_def.base_class}"
                    if base_id not in nodes and class_def.base_class in class_system.classes:
                        nodes[base_id] = {
                            'id': base_id,
                            'label': class_def.base_class,
                            'group': 6,
                            'type': 'class'
                        }
                    
                    links.append({
                        'source': class_id,
                        'target': base_id,
                        'value': 1,
                        'relationship': 'extends'
                    })
        
        return {'nodes': list(nodes.values()), 'links': links}

    def export_entity_graph(self) -> Dict[str, Any]:
        """
        Export existential entities and their relationships as D3 graph
        تصدير الكيانات الوجودية وعلاقاتها كرسم بياني
        """
        nodes = {}
        links = []
        
        # Add existential beings
        for being_name, being_config in self.existential_beings.items():
            being_id = f"entity_{being_name}"
            being_type = being_config.get('_type', being_config.get('type', being_config.get('نوع', 'Unknown')))
            
            nodes[being_id] = {
                'id': being_id,
                'label': being_name,
                'group': 7,  # Brown for entities
                'type': 'entity',
                'entity_type': being_type
            }
            
            # Add relations
            relations = being_config.get('relations', being_config.get('علاقات', {}))
            for rel_type, targets in relations.items():
                if isinstance(targets, list):
                    for target in targets:
                        target_id = f"entity_{target}"
                        # Ensure target node exists
                        if target_id not in nodes:
                            nodes[target_id] = {
                                'id': target_id,
                                'label': target,
                                'group': 7,
                                'type': 'entity'
                            }
                        
                        links.append({
                            'source': being_id,
                            'target': target_id,
                            'value': 1,
                            'relationship': rel_type
                        })
        
        return {'nodes': list(nodes.values()), 'links': links}

    def export_unified_graph(self) -> Dict[str, Any]:
        """
        Export all paradigms in one unified graph with layers
        تصدير جميع النماذج البرمجية في رسم بياني موحد مع طبقات
        """
        # Get all individual graphs
        logic_graph = self.export_d3_graph()
        procedural_graph = self.export_procedural_graph()
        oop_graph = self.export_oop_graph()
        entity_graph = self.export_entity_graph()
        
        # Merge all nodes (using dict to avoid duplicates)
        all_nodes = {}
        all_links = []
        
        # Track which nodes belong to which layer
        layers = {
            'logic': [],
            'procedural': [],
            'oop': [],
            'entity': []
        }
        
        # Add logic nodes
        for node in logic_graph['nodes']:
            all_nodes[node['id']] = node
            layers['logic'].append(node['id'])
        all_links.extend(logic_graph['links'])
        
        # Add procedural nodes
        for node in procedural_graph['nodes']:
            all_nodes[node['id']] = node
            layers['procedural'].append(node['id'])
        all_links.extend(procedural_graph['links'])
        
        # Add OOP nodes
        for node in oop_graph['nodes']:
            all_nodes[node['id']] = node
            layers['oop'].append(node['id'])
        all_links.extend(oop_graph['links'])
        
        # Add entity nodes
        for node in entity_graph['nodes']:
            all_nodes[node['id']] = node
            layers['entity'].append(node['id'])
        all_links.extend(entity_graph['links'])
        
        return {
            'nodes': list(all_nodes.values()),
            'links': all_links,
            'layers': layers,
            'stats': {
                'total_nodes': len(all_nodes),
                'total_links': len(all_links),
                'logic_nodes': len(layers['logic']),
                'procedural_nodes': len(layers['procedural']),
                'oop_nodes': len(layers['oop']),
                'entity_nodes': len(layers['entity'])
            }
        }

