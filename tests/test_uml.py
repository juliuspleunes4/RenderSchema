"""Unit tests for the UML diagram generator."""

import pytest
from renderschema.generators.uml import UMLDiagramGenerator


class SampleClass:
    """A sample class for testing."""
    
    def __init__(self, name: str, value: int) -> None:
        self.name = name
        self.value = value
    
    def get_name(self) -> str:
        """Get the name."""
        return self.name
    
    def _private_method(self) -> None:
        """A private method."""
        pass


class TestUMLDiagramGenerator:
    """Test suite for UMLDiagramGenerator."""

    def test_initialization(self):
        """Test generator initialization."""
        generator = UMLDiagramGenerator(SampleClass)
        assert generator.target == SampleClass
        assert generator.theme == "light"

    def test_analyze_class(self):
        """Test class analysis."""
        generator = UMLDiagramGenerator(SampleClass)
        data = generator.analyze()
        
        assert data["name"] == "SampleClass"
        assert data["module"] == "__main__"
        assert isinstance(data["attributes"], list)
        assert isinstance(data["methods"], list)

    def test_generate_svg(self):
        """Test SVG generation."""
        generator = UMLDiagramGenerator(SampleClass)
        svg = generator.generate()
        
        assert svg.startswith('<?xml version="1.0"')
        assert "<svg" in svg
        assert "SampleClass" in svg
        assert "</svg>" in svg

    def test_dark_theme(self):
        """Test dark theme generation."""
        generator = UMLDiagramGenerator(SampleClass, theme="dark")
        svg = generator.generate()
        
        assert "#1f2937" in svg  # Dark theme color

    def test_invalid_target(self):
        """Test error handling for invalid target."""
        with pytest.raises(TypeError):
            generator = UMLDiagramGenerator("not a class")
            generator.analyze()
