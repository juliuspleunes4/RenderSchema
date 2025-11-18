"""Flowchart diagram generator for Python functions and control flow."""

from typing import Any, Dict
import ast
import inspect

from .base import BaseDiagramGenerator


class FlowchartGenerator(BaseDiagramGenerator):
    """
    Generate flowcharts from Python functions showing control flow.

    Analyzes function code to extract control flow structures (if/else, loops, etc.)
    and generates visual flowcharts.
    """

    def analyze(self) -> Dict[str, Any]:
        """
        Analyze the target function to extract control flow.

        Returns:
            Dictionary containing control flow nodes and edges.
        """
        if inspect.isfunction(self.target) or inspect.ismethod(self.target):
            return self._analyze_function(self.target)
        else:
            raise TypeError(
                f"FlowchartGenerator requires a function or method, got {type(self.target)}"
            )

    def _analyze_function(self, func: Any) -> Dict[str, Any]:
        """Analyze a Python function's control flow."""
        source = inspect.getsource(func)
        tree = ast.parse(source)
        
        return {
            "name": func.__name__,
            "module": func.__module__,
            "nodes": self._extract_nodes(tree),
            "docstring": inspect.getdoc(func),
        }

    def _extract_nodes(self, tree: ast.AST) -> list:
        """Extract control flow nodes from AST."""
        # Placeholder for AST traversal logic
        nodes = [
            {"type": "start", "label": "Start"},
            {"type": "process", "label": "<function_logic>"},
            {"type": "end", "label": "End"},
        ]
        return nodes

    def generate(self) -> str:
        """
        Generate SVG markup for the flowchart.

        Returns:
            SVG string representing the flowchart.
        """
        if self._diagram_data is None:
            self._diagram_data = self.analyze()

        svg_parts = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400">',
            self._generate_styles(),
        ]

        # Generate flowchart nodes
        y_offset = 50
        for node in self._diagram_data["nodes"]:
            svg_parts.append(self._generate_node(node, 250, y_offset))
            y_offset += 100

        svg_parts.append("</svg>")
        return "\n".join(svg_parts)

    def _generate_styles(self) -> str:
        """Generate CSS styles for flowchart."""
        if self.theme == "dark":
            return """
<defs>
    <style>
        .flow-node { fill: #1f2937; stroke: #10b981; stroke-width: 2; }
        .flow-text { fill: #f9fafb; font-family: Arial, sans-serif; font-size: 14px; }
        .flow-arrow { stroke: #10b981; stroke-width: 2; fill: none; marker-end: url(#arrowhead); }
    </style>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
        <polygon points="0 0, 10 3, 0 6" fill="#10b981" />
    </marker>
</defs>"""
        else:
            return """
<defs>
    <style>
        .flow-node { fill: #ffffff; stroke: #10b981; stroke-width: 2; }
        .flow-text { fill: #1f2937; font-family: Arial, sans-serif; font-size: 14px; }
        .flow-arrow { stroke: #10b981; stroke-width: 2; fill: none; marker-end: url(#arrowhead); }
    </style>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
        <polygon points="0 0, 10 3, 0 6" fill="#10b981" />
    </marker>
</defs>"""

    def _generate_node(self, node: Dict[str, Any], x: int, y: int) -> str:
        """Generate SVG markup for a flowchart node."""
        node_type = node["type"]
        label = node["label"]

        if node_type in ("start", "end"):
            # Rounded rectangle for start/end
            return f'''<rect x="{x - 60}" y="{y}" width="120" height="40" rx="20" class="flow-node"/>
<text x="{x}" y="{y + 25}" text-anchor="middle" class="flow-text">{label}</text>'''
        else:
            # Rectangle for process
            return f'''<rect x="{x - 80}" y="{y}" width="160" height="50" rx="4" class="flow-node"/>
<text x="{x}" y="{y + 30}" text-anchor="middle" class="flow-text">{label}</text>'''
