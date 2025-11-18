"""Core functionality for RenderSchema diagram generation."""

from typing import Any, Type, Union
from pathlib import Path

from .generators.base import BaseDiagramGenerator
from .generators.uml import UMLDiagramGenerator


def diagram(
    target: Union[Type, object, str, Path],
    diagram_type: str = "uml",
    **options: Any
) -> BaseDiagramGenerator:
    """
    Create a diagram generator for the specified target.

    Args:
        target: The Python class, object, module path, or project path to diagram.
        diagram_type: Type of diagram to generate. Options: 'uml', 'flowchart', 'class'.
        **options: Additional configuration options for the diagram generator.

    Returns:
        A diagram generator instance ready to export diagrams.

    Example:
        >>> from renderschema import diagram
        >>> generator = diagram(MyClass)
        >>> generator.export("output.svg")
    """
    from .generators.flowchart import FlowchartGenerator
    from .generators.class_diagram import ClassDiagramGenerator

    generators = {
        "uml": UMLDiagramGenerator,
        "flowchart": FlowchartGenerator,
        "class": ClassDiagramGenerator,
    }

    generator_class = generators.get(diagram_type.lower())
    if not generator_class:
        raise ValueError(
            f"Unknown diagram type: {diagram_type}. "
            f"Available types: {', '.join(generators.keys())}"
        )

    return generator_class(target, **options)
