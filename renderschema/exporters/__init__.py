"""Export modules for different output formats."""

from .svg import SVGExporter
from .png import PNGExporter
from .pdf import PDFExporter
from .html import HTMLExporter


def get_exporter(format: str):
    """
    Get the appropriate exporter for the specified format.

    Args:
        format: Output format ('svg', 'png', 'pdf', 'html').

    Returns:
        Exporter instance for the specified format.

    Raises:
        ValueError: If the format is not supported.
    """
    exporters = {
        "svg": SVGExporter,
        "png": PNGExporter,
        "pdf": PDFExporter,
        "html": HTMLExporter,
    }

    exporter_class = exporters.get(format.lower())
    if not exporter_class:
        raise ValueError(
            f"Unsupported export format: {format}. "
            f"Supported formats: {', '.join(exporters.keys())}"
        )

    return exporter_class()


__all__ = [
    "SVGExporter",
    "PNGExporter",
    "PDFExporter",
    "HTMLExporter",
    "get_exporter",
]
