"""HTML exporter for interactive diagram output."""

from pathlib import Path
from typing import Optional


class HTMLExporter:
    """Export diagrams as interactive HTML files."""

    def export(
        self,
        content: str,
        output_path: Path,
        theme: Optional[str] = "light",
        interactive: bool = True
    ) -> None:
        """
        Export SVG content as an interactive HTML file.

        Args:
            content: SVG markup as a string.
            output_path: Path where the HTML file should be saved.
            theme: Theme setting ('light' or 'dark').
            interactive: Whether to include interactive features.
        """
        html = self.to_string(content, interactive=interactive, theme=theme)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(html, encoding="utf-8")

    def to_string(
        self,
        svg_content: str,
        interactive: bool = True,
        theme: str = "light"
    ) -> str:
        """
        Convert SVG content to HTML string.

        Args:
            svg_content: SVG markup as a string.
            interactive: Whether to include interactive features.
            theme: Theme setting ('light' or 'dark').

        Returns:
            Complete HTML document as a string.
        """
        bg_color = "#0f172a" if theme == "dark" else "#f8fafc"
        
        interactive_script = ""
        if interactive:
            interactive_script = """
<script>
    const svg = document.querySelector('svg');
    let isPanning = false;
    let startPoint = { x: 0, y: 0 };
    let scale = 1;

    svg.addEventListener('mousedown', (e) => {
        isPanning = true;
        startPoint = { x: e.clientX, y: e.clientY };
    });

    document.addEventListener('mouseup', () => {
        isPanning = false;
    });

    svg.addEventListener('wheel', (e) => {
        e.preventDefault();
        const delta = e.deltaY > 0 ? 0.9 : 1.1;
        scale *= delta;
        svg.style.transform = `scale(${scale})`;
    });
</script>"""

        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RenderSchema Diagram</title>
    <style>
        body {{
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background-color: {bg_color};
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }}
        .container {{
            max-width: 100%;
            overflow: auto;
        }}
        svg {{
            max-width: 100%;
            height: auto;
            cursor: {'grab' if interactive else 'default'};
            transition: transform 0.1s ease;
        }}
        svg:active {{
            cursor: {'grabbing' if interactive else 'default'};
        }}
    </style>
</head>
<body>
    <div class="container">
        {svg_content}
    </div>
    {interactive_script}
</body>
</html>"""
