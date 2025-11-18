"""Class diagram generator focused on relationships between multiple classes."""

from typing import Any, Dict, List, Type
import inspect

from .base import BaseDiagramGenerator


class ClassDiagramGenerator(BaseDiagramGenerator):
    """
    Generate class relationship diagrams showing inheritance and associations.

    Focuses on visualizing relationships between multiple classes rather than
    individual class details.
    """

    def analyze(self) -> Dict[str, Any]:
        """
        Analyze classes to extract relationships.

        Returns:
            Dictionary containing classes and their relationships.
        """
        if inspect.ismodule(self.target):
            return self._analyze_module_relationships(self.target)
        elif isinstance(self.target, (list, tuple)):
            return self._analyze_class_list(self.target)
        else:
            raise TypeError(
                "ClassDiagramGenerator requires a module or list of classes"
            )

    def _analyze_module_relationships(self, module: Any) -> Dict[str, Any]:
        """Analyze relationships between classes in a module."""
        classes = []
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and obj.__module__ == module.__name__:
                classes.append({
                    "name": obj.__name__,
                    "bases": [b.__name__ for b in obj.__bases__ if b != object],
                })

        return {
            "type": "module",
            "name": module.__name__,
            "classes": classes,
            "relationships": self._extract_relationships(classes),
        }

    def _analyze_class_list(self, classes: List[Type]) -> Dict[str, Any]:
        """Analyze relationships in a list of classes."""
        class_data = []
        for cls in classes:
            if inspect.isclass(cls):
                class_data.append({
                    "name": cls.__name__,
                    "bases": [b.__name__ for b in cls.__bases__ if b != object],
                })

        return {
            "type": "class_list",
            "classes": class_data,
            "relationships": self._extract_relationships(class_data),
        }

    def _extract_relationships(self, classes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Extract inheritance relationships between classes."""
        relationships = []
        class_names = {cls["name"] for cls in classes}

        for cls in classes:
            for base in cls["bases"]:
                if base in class_names:
                    relationships.append({
                        "type": "inheritance",
                        "from": cls["name"],
                        "to": base,
                    })

        return relationships

    def generate(self) -> str:
        """
        Generate SVG markup for the class relationship diagram.

        Returns:
            SVG string representing the class diagram.
        """
        if self._diagram_data is None:
            self._diagram_data = self.analyze()

        svg_parts = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">',
            self._generate_styles(),
        ]

        # Simple layout: vertical arrangement
        classes = self._diagram_data["classes"]
        y_offset = 50
        class_positions = {}

        for cls_data in classes:
            x = 200
            svg_parts.append(self._generate_class_box(cls_data, x, y_offset))
            class_positions[cls_data["name"]] = (x + 100, y_offset + 30)
            y_offset += 120

        # Draw relationships
        for rel in self._diagram_data["relationships"]:
            if rel["type"] == "inheritance":
                from_pos = class_positions.get(rel["from"])
                to_pos = class_positions.get(rel["to"])
                if from_pos and to_pos:
                    svg_parts.append(self._generate_inheritance_arrow(from_pos, to_pos))

        svg_parts.append("</svg>")
        return "\n".join(svg_parts)

    def _generate_styles(self) -> str:
        """Generate CSS styles for the class diagram."""
        if self.theme == "dark":
            return """
<defs>
    <style>
        .class-box { fill: #1f2937; stroke: #8b5cf6; stroke-width: 2; }
        .class-name { fill: #f9fafb; font-family: Arial, sans-serif; font-size: 14px; font-weight: bold; }
        .inheritance-line { stroke: #8b5cf6; stroke-width: 2; fill: none; marker-end: url(#triangle); }
    </style>
    <marker id="triangle" markerWidth="10" markerHeight="10" refX="10" refY="5" orient="auto">
        <polygon points="0 0, 10 5, 0 10" fill="#8b5cf6" />
    </marker>
</defs>"""
        else:
            return """
<defs>
    <style>
        .class-box { fill: #ffffff; stroke: #8b5cf6; stroke-width: 2; }
        .class-name { fill: #1f2937; font-family: Arial, sans-serif; font-size: 14px; font-weight: bold; }
        .inheritance-line { stroke: #8b5cf6; stroke-width: 2; fill: none; marker-end: url(#triangle); }
    </style>
    <marker id="triangle" markerWidth="10" markerHeight="10" refX="10" refY="5" orient="auto">
        <polygon points="0 0, 10 5, 0 10" fill="#8b5cf6" />
    </marker>
</defs>"""

    def _generate_class_box(self, cls_data: Dict[str, Any], x: int, y: int) -> str:
        """Generate a simple class box showing just the name."""
        width = 200
        height = 60
        return f'''<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="4" class="class-box"/>
<text x="{x + width/2}" y="{y + 35}" text-anchor="middle" class="class-name">{cls_data["name"]}</text>'''

    def _generate_inheritance_arrow(
        self, 
        from_pos: tuple, 
        to_pos: tuple
    ) -> str:
        """Generate an inheritance arrow between two classes."""
        x1, y1 = from_pos
        x2, y2 = to_pos
        return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="inheritance-line"/>'
