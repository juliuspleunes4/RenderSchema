"""Base diagram generator class providing common functionality."""

from abc import ABC, abstractmethod
from typing import Any, Union, Dict, Optional
from pathlib import Path


class BaseDiagramGenerator(ABC):
    """
    Abstract base class for all diagram generators.

    Provides common functionality for analyzing Python code and exporting diagrams
    in various formats.
    """

    def __init__(self, target: Any, **options: Any) -> None:
        """
        Initialize the diagram generator.

        Args:
            target: The target to generate a diagram for (class, module, path, etc.).
            **options: Configuration options for diagram generation.
        """
        self.target = target
        self.options = options
        self.theme = options.get("theme", "light")
        self.color_scheme = options.get("color_scheme", "tailwind")
        self._diagram_data: Optional[Dict[str, Any]] = None

    @abstractmethod
    def analyze(self) -> Dict[str, Any]:
        """
        Analyze the target and extract relevant information for diagram generation.

        Returns:
            Dictionary containing analyzed data about the target.
        """
        pass

    @abstractmethod
    def generate(self) -> str:
        """
        Generate the diagram representation.

        Returns:
            String representation of the diagram (e.g., SVG markup, DOT notation).
        """
        pass

    def export(
        self,
        output_path: Union[str, Path],
        format: Optional[str] = None
    ) -> None:
        """
        Export the diagram to a file.

        Args:
            output_path: Path where the diagram should be saved.
            format: Output format ('svg', 'png', 'pdf', 'html'). 
                   If None, inferred from file extension.

        Example:
            >>> generator.export("diagram.svg")
            >>> generator.export("diagram.png", format="png")
        """
        from ..exporters import get_exporter

        output_path = Path(output_path)
        if format is None:
            format = output_path.suffix.lstrip(".")

        if not format:
            raise ValueError(
                "Could not determine output format. "
                "Please specify format or use a file extension."
            )

        # Generate diagram if not already done
        if self._diagram_data is None:
            self._diagram_data = self.analyze()

        diagram_content = self.generate()
        
        exporter = get_exporter(format)
        exporter.export(diagram_content, output_path, theme=self.theme)

    def to_svg(self) -> str:
        """
        Generate and return the diagram as SVG string.

        Returns:
            SVG markup as a string.
        """
        if self._diagram_data is None:
            self._diagram_data = self.analyze()
        return self.generate()

    def to_html(self, interactive: bool = True) -> str:
        """
        Generate and return the diagram as HTML with optional interactivity.

        Args:
            interactive: Whether to include interactive features (zoom, pan, click).

        Returns:
            HTML markup as a string.
        """
        from ..exporters.html import HTMLExporter
        
        svg_content = self.to_svg()
        exporter = HTMLExporter()
        return exporter.to_string(svg_content, interactive=interactive, theme=self.theme)
