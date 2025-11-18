"""UML diagram generator for Python classes and modules."""

import inspect
from typing import Any, Dict, List, Type
from pathlib import Path

from .base import BaseDiagramGenerator


class UMLDiagramGenerator(BaseDiagramGenerator):
    """
    Generate UML class diagrams from Python classes and modules.

    Analyzes Python classes to extract attributes, methods, inheritance,
    and relationships, then generates clean UML diagrams.
    """

    def analyze(self) -> Dict[str, Any]:
        """
        Analyze the target class or module to extract UML information.

        Returns:
            Dictionary containing classes, attributes, methods, and relationships.
        """
        if inspect.isclass(self.target):
            return self._analyze_class(self.target)
        elif inspect.ismodule(self.target):
            return self._analyze_module(self.target)
        elif isinstance(self.target, (str, Path)):
            return self._analyze_path(Path(self.target))
        else:
            raise TypeError(
                f"Unsupported target type: {type(self.target)}. "
                "Expected class, module, or path."
            )

    def _analyze_class(self, cls: Type) -> Dict[str, Any]:
        """Analyze a single Python class."""
        attributes = []
        methods = []

        for name, obj in inspect.getmembers(cls):
            if name.startswith("_") and not name.startswith("__"):
                continue  # Skip private members unless dunder

            if inspect.ismethod(obj) or inspect.isfunction(obj):
                sig = inspect.signature(obj)
                methods.append({
                    "name": name,
                    "parameters": list(sig.parameters.keys()),
                    "return_type": self._get_type_name(sig.return_annotation),
                    "visibility": self._get_visibility(name),
                })
            elif not callable(obj) or name.startswith("__"):
                # Class attributes or dunder methods
                type_hint = self._get_type_hint(cls, name)
                if not inspect.ismethod(obj) and not inspect.isfunction(obj):
                    attributes.append({
                        "name": name,
                        "type": type_hint,
                        "visibility": self._get_visibility(name),
                    })

        return {
            "name": cls.__name__,
            "module": cls.__module__,
            "bases": [base.__name__ for base in cls.__bases__ if base != object],
            "attributes": attributes,
            "methods": methods,
            "docstring": inspect.getdoc(cls),
        }

    def _analyze_module(self, module: Any) -> Dict[str, Any]:
        """Analyze a Python module to find all classes."""
        classes = []
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and obj.__module__ == module.__name__:
                classes.append(self._analyze_class(obj))

        return {
            "type": "module",
            "name": module.__name__,
            "classes": classes,
        }

    def _analyze_path(self, path: Path) -> Dict[str, Any]:
        """Analyze a file or directory path."""
        # Placeholder for future implementation
        return {
            "type": "path",
            "path": str(path),
            "classes": [],
        }

    def _get_visibility(self, name: str) -> str:
        """Determine visibility modifier based on naming convention."""
        if name.startswith("__") and not name.endswith("__"):
            return "private"
        elif name.startswith("_"):
            return "protected"
        else:
            return "public"

    def _get_type_hint(self, cls: Type, attr_name: str) -> str:
        """Extract type hint for a class attribute."""
        hints = getattr(cls, "__annotations__", {})
        if attr_name in hints:
            return self._get_type_name(hints[attr_name])
        return "Any"

    def _get_type_name(self, type_annotation: Any) -> str:
        """Convert type annotation to readable string."""
        if type_annotation == inspect.Parameter.empty:
            return ""
        if hasattr(type_annotation, "__name__"):
            return type_annotation.__name__
        return str(type_annotation).replace("typing.", "")

    def generate(self) -> str:
        """
        Generate SVG markup for the UML diagram.

        Returns:
            SVG string representing the UML diagram.
        """
        if self._diagram_data is None:
            self._diagram_data = self.analyze()

        # Start building SVG
        svg_parts = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">',
        ]

        # Add styles based on theme
        svg_parts.append(self._generate_styles())

        # Generate class boxes
        if "classes" in self._diagram_data:
            # Module with multiple classes
            y_offset = 50
            for cls_data in self._diagram_data["classes"]:
                svg_parts.append(self._generate_class_box(cls_data, 50, y_offset))
                y_offset += 200
        else:
            # Single class
            svg_parts.append(self._generate_class_box(self._diagram_data, 50, 50))

        svg_parts.append("</svg>")
        return "\n".join(svg_parts)

    def _generate_styles(self) -> str:
        """Generate CSS styles for the SVG based on theme."""
        if self.theme == "dark":
            return """
<defs>
    <style>
        .class-box { fill: #1f2937; stroke: #4b5563; stroke-width: 2; }
        .class-name { fill: #f9fafb; font-family: Arial, sans-serif; font-size: 16px; font-weight: bold; }
        .class-text { fill: #d1d5db; font-family: 'Courier New', monospace; font-size: 12px; }
        .section-line { stroke: #4b5563; stroke-width: 1; }
    </style>
</defs>"""
        else:
            return """
<defs>
    <style>
        .class-box { fill: #ffffff; stroke: #3b82f6; stroke-width: 2; }
        .class-name { fill: #1f2937; font-family: Arial, sans-serif; font-size: 16px; font-weight: bold; }
        .class-text { fill: #374151; font-family: 'Courier New', monospace; font-size: 12px; }
        .section-line { stroke: #e5e7eb; stroke-width: 1; }
    </style>
</defs>"""

    def _generate_class_box(self, cls_data: Dict[str, Any], x: int, y: int) -> str:
        """Generate SVG markup for a single class box."""
        box_width = 300
        header_height = 40
        line_height = 20

        # Calculate box height
        attr_count = len(cls_data.get("attributes", []))
        method_count = len(cls_data.get("methods", []))
        box_height = header_height + (attr_count + method_count + 2) * line_height

        parts = [
            # Main box
            f'<rect x="{x}" y="{y}" width="{box_width}" height="{box_height}" class="class-box" rx="4"/>',
            # Class name
            f'<text x="{x + box_width/2}" y="{y + 25}" text-anchor="middle" class="class-name">{cls_data["name"]}</text>',
            # Separator line
            f'<line x1="{x}" y1="{y + header_height}" x2="{x + box_width}" y2="{y + header_height}" class="section-line"/>',
        ]

        current_y = y + header_height + line_height

        # Attributes
        for attr in cls_data.get("attributes", []):
            visibility = {"public": "+", "protected": "#", "private": "-"}.get(attr["visibility"], "+")
            text = f'{visibility} {attr["name"]}: {attr["type"]}'
            parts.append(f'<text x="{x + 10}" y="{current_y}" class="class-text">{text}</text>')
            current_y += line_height

        if cls_data.get("methods"):
            # Separator before methods
            parts.append(f'<line x1="{x}" y1="{current_y}" x2="{x + box_width}" y2="{current_y}" class="section-line"/>')
            current_y += line_height

            # Methods
            for method in cls_data.get("methods", []):
                visibility = {"public": "+", "protected": "#", "private": "-"}.get(method["visibility"], "+")
                params = ", ".join(method["parameters"][1:]) if len(method["parameters"]) > 1 else ""
                text = f'{visibility} {method["name"]}({params})'
                if method["return_type"]:
                    text += f': {method["return_type"]}'
                parts.append(f'<text x="{x + 10}" y="{current_y}" class="class-text">{text}</text>')
                current_y += line_height

        return "\n".join(parts)
