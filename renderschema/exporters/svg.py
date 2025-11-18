"""SVG exporter for diagram output."""

from pathlib import Path
from typing import Optional


class SVGExporter:
    """Export diagrams as SVG files."""

    def export(
        self,
        content: str,
        output_path: Path,
        theme: Optional[str] = None
    ) -> None:
        """
        Export SVG content to a file.

        Args:
            content: SVG markup as a string.
            output_path: Path where the SVG file should be saved.
            theme: Theme setting (not used for SVG, preserved in content).
        """
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content, encoding="utf-8")
