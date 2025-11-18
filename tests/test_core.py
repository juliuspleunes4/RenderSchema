"""Unit tests for the core diagram function."""

import pytest
from renderschema import diagram
from renderschema.generators.uml import UMLDiagramGenerator
from renderschema.generators.flowchart import FlowchartGenerator


class TestClass:
    """Test class."""
    pass


def test_function():
    """Test function."""
    pass


class TestDiagramFunction:
    """Test suite for the diagram() function."""

    def test_diagram_with_class_default_type(self):
        """Test diagram() with a class uses UML by default."""
        gen = diagram(TestClass)
        assert isinstance(gen, UMLDiagramGenerator)

    def test_diagram_with_uml_type(self):
        """Test diagram() with explicit UML type."""
        gen = diagram(TestClass, diagram_type="uml")
        assert isinstance(gen, UMLDiagramGenerator)

    def test_diagram_with_flowchart_type(self):
        """Test diagram() with flowchart type."""
        gen = diagram(test_function, diagram_type="flowchart")
        assert isinstance(gen, FlowchartGenerator)

    def test_diagram_with_invalid_type(self):
        """Test diagram() with invalid diagram type."""
        with pytest.raises(ValueError, match="Unknown diagram type"):
            diagram(TestClass, diagram_type="invalid")

    def test_diagram_with_options(self):
        """Test diagram() with custom options."""
        gen = diagram(TestClass, theme="dark", color_scheme="custom")
        assert gen.theme == "dark"
        assert gen.options["color_scheme"] == "custom"
