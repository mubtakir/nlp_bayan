"""
Tests for Existential Model Visualization
اختبارات تصور النموذج الوجودي
"""

import pytest
import os
from bayan.bayan.lexer import HybridLexer
from bayan.bayan.parser import HybridParser
from bayan.bayan.traditional_interpreter import TraditionalInterpreter


@pytest.fixture
def interpreter():
    """Create interpreter with sample domain and beings"""
    # Define a simple domain
    code = '''
مجال "test_domain":
{
    "كائن_أساسي": "entity",
    "بيئة": "environment",
    "معانٍ_أساسية": ["meaning1", "meaning2"],
    "علاقات": ["relates_to"],
    "خصائص": ["property1", "property2"]
}

بيئة "test_env" في_مجال "test_domain":
{
    "أبعاد": {
        "مكاني": {"x": 10, "y": 20},
        "زماني": {"time": "now"},
        "مجالي": {"custom": "value"}
    }
}

كائن_وجودي "entity1" من_نوع "entity" في_مجال "test_domain":
{
    "بيئة": "test_env",
    "خصائص_ذاتية": {"property1": "value1", "property2": 42},
    "معانٍ_ذاتية": ["meaning1"],
    "علاقات": {"relates_to": ["entity2"]}
}

كائن_وجودي "entity2" من_نوع "entity" في_مجال "test_domain":
{
    "بيئة": "test_env",
    "خصائص_ذاتية": {"property1": "value2", "property2": 24},
    "معانٍ_ذاتية": ["meaning2"],
    "علاقات": {"relates_to": ["entity1"]}
}
'''

    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()
    interp = TraditionalInterpreter()
    interp.interpret(ast)

    return interp


def test_visualize_environment(interpreter):
    """Test environment visualization"""
    # Visualize environment
    diagram = interpreter.visualize_environment("test_env")
    
    # Check that diagram is generated
    assert diagram is not None
    assert isinstance(diagram, str)
    assert len(diagram) > 0
    
    # Check for Mermaid syntax
    assert "graph TD" in diagram or "graph LR" in diagram
    
    # Check for environment name
    assert "test_env" in diagram
    
    # Check for dimensions
    assert "مكاني" in diagram or "Spatial" in diagram
    assert "زماني" in diagram or "Temporal" in diagram
    assert "مجالي" in diagram or "Domain" in diagram
    
    print(f"\n✅ Environment visualization test passed")
    print(f"Diagram length: {len(diagram)} characters")


def test_visualize_relations(interpreter):
    """Test relations visualization"""
    # Visualize relations
    diagram = interpreter.visualize_relations("test_domain")
    
    # Check that diagram is generated
    assert diagram is not None
    assert isinstance(diagram, str)
    assert len(diagram) > 0
    
    # Check for Mermaid syntax
    assert "graph" in diagram
    
    # Check for entities (node IDs will be hashed)
    # Just check that there are nodes and edges
    assert "-->" in diagram or "---" in diagram
    
    print(f"\n✅ Relations visualization test passed")
    print(f"Diagram length: {len(diagram)} characters")


def test_visualize_being(interpreter):
    """Test being visualization"""
    # Visualize being
    diagram = interpreter.visualize_being("entity1")
    
    # Check that diagram is generated
    assert diagram is not None
    assert isinstance(diagram, str)
    assert len(diagram) > 0
    
    # Check for Mermaid syntax
    assert "graph TD" in diagram or "graph LR" in diagram
    
    # Check for being name
    assert "entity1" in diagram
    
    # Check for components
    assert "النوع" in diagram or "TYPE" in diagram
    assert "البيئة" in diagram or "ENV" in diagram
    assert "المجال" in diagram or "DOMAIN" in diagram
    
    print(f"\n✅ Being visualization test passed")
    print(f"Diagram length: {len(diagram)} characters")


def test_visualize_domain(interpreter):
    """Test domain visualization"""
    # Visualize domain
    diagram = interpreter.visualize_domain("test_domain")
    
    # Check that diagram is generated
    assert diagram is not None
    assert isinstance(diagram, str)
    assert len(diagram) > 0
    
    # Check for Mermaid syntax
    assert "graph TD" in diagram or "graph LR" in diagram
    
    # Check for domain name
    assert "test_domain" in diagram
    
    # Check for domain components
    assert "كائنات" in diagram or "BEINGS" in diagram
    assert "علاقات" in diagram or "RELATIONS" in diagram
    
    print(f"\n✅ Domain visualization test passed")
    print(f"Diagram length: {len(diagram)} characters")


def test_save_visualization(interpreter, tmp_path):
    """Test saving visualization as HTML"""
    # Generate a diagram
    diagram = interpreter.visualize_domain("test_domain")

    # Save to temporary file
    output_file = tmp_path / "test_viz.html"
    result = interpreter.save_visualization(diagram, str(output_file), "Test Visualization")

    # Check that file was created
    assert os.path.exists(output_file)
    assert result == str(output_file)

    # Read and check content
    with open(output_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Check for HTML structure
    assert "<!DOCTYPE html>" in html_content
    assert "<html" in html_content
    assert "mermaid" in html_content.lower()
    assert "Test Visualization" in html_content

    # Check that diagram is embedded
    assert diagram in html_content

    print(f"\n✅ Save visualization test passed")
    print(f"HTML file size: {len(html_content)} characters")


def test_visualize_nonexistent_environment(interpreter):
    """Test visualization of non-existent environment"""
    # Try to visualize non-existent environment
    diagram = interpreter.visualize_environment("nonexistent")

    # Should return error message
    assert "Error" in diagram or "not found" in diagram

    print(f"\n✅ Non-existent environment test passed")


def test_visualize_nonexistent_being(interpreter):
    """Test visualization of non-existent being"""
    # Try to visualize non-existent being
    diagram = interpreter.visualize_being("nonexistent")

    # Should return error message
    assert "Error" in diagram or "not found" in diagram

    print(f"\n✅ Non-existent being test passed")


def test_visualize_nonexistent_domain(interpreter):
    """Test visualization of non-existent domain"""
    # Try to visualize non-existent domain
    diagram = interpreter.visualize_domain("nonexistent")

    # Should return error message
    assert "Error" in diagram or "not found" in diagram

    print(f"\n✅ Non-existent domain test passed")


def test_visualize_relations_all_domains(interpreter):
    """Test visualizing relations across all domains"""
    # Visualize relations without specifying domain
    diagram = interpreter.visualize_relations(None)

    # Check that diagram is generated
    assert diagram is not None
    assert isinstance(diagram, str)
    assert len(diagram) > 0

    # Check for Mermaid syntax
    assert "graph" in diagram

    print(f"\n✅ All domains relations visualization test passed")
    print(f"Diagram length: {len(diagram)} characters")


if __name__ == "__main__":
    print("Running visualization tests...")
    pytest.main([__file__, "-v"])

