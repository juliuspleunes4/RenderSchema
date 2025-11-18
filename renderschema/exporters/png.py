"""PNG exporter for diagram output."""

from pathlib import Path
from typing import Optional


class PNGExporter:
    """Export diagrams as PNG files."""

    def export(
        self,
        content: str,
        output_path: Path,
        theme: Optional[str] = None
    ) -> None:
        """
        Export SVG content as PNG.

        Args:
            content: SVG markup as a string.
            output_path: Path where the PNG file should be saved.
            theme: Theme setting for rendering.

        Note:
            Requires cairosvg or similar library for SVG to PNG conversion.
        """
        try:
            import cairosvg
            
            output_path.parent.mkdir(parents=True, exist_ok=True)
            cairosvg.svg2png(
                bytestring=content.encode("utf-8"),
                write_to=str(output_path)
            )
        except ImportError:
            raise ImportError(
                "PNG export requires 'cairosvg'. "
                "Install it with: pip install cairosvg"
            )
