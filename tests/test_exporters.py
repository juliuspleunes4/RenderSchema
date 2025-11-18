"""Unit tests for SVG exporter."""

import pytest
from pathlib import Path
from renderschema.exporters.svg import SVGExporter


class TestSVGExporter:
    """Test suite for SVGExporter."""

    def test_export_creates_file(self, tmp_path):
        """Test that export creates an SVG file."""
        exporter = SVGExporter()
        output_file = tmp_path / "test.svg"
        svg_content = '<svg><rect x="0" y="0" width="100" height="100"/></svg>'
        
        exporter.export(svg_content, output_file)
        
        assert output_file.exists()
        assert output_file.read_text() == svg_content

    def test_export_creates_directories(self, tmp_path):
        """Test that export creates parent directories."""
        exporter = SVGExporter()
        output_file = tmp_path / "subdir" / "test.svg"
        svg_content = "<svg></svg>"
        
        exporter.export(svg_content, output_file)
        
        assert output_file.exists()
        assert output_file.parent.exists()
