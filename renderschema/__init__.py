"""
RenderSchema: Automatically generate beautiful documentation diagrams from Python code.

This library converts Python classes, modules, and project structures into clean
UML diagrams, flowcharts, class relationships, and architectural visualizations.
"""

from .core import diagram
from .generators import UMLDiagramGenerator, FlowchartGenerator
from .exporters import SVGExporter, PNGExporter, PDFExporter, HTMLExporter

__version__ = "0.1.0"
__all__ = [
    "diagram",
    "UMLDiagramGenerator",
    "FlowchartGenerator",
    "SVGExporter",
    "PNGExporter",
    "PDFExporter",
    "HTMLExporter",
]
