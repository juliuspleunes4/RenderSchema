# Frequently Asked Questions (FAQ)

## General Questions

### What is RenderSchema?

RenderSchema is a Python library that automatically generates beautiful, readable documentation diagrams from your Python code. It converts classes, modules, and project structures into clean UML diagrams, flowcharts, and class relationship visualizations.

### Why use RenderSchema over other diagramming tools?

- **Zero Manual Work**: Diagrams are generated automatically from code
- **Always Up-to-Date**: Regenerate diagrams anytime code changes
- **Beautiful Output**: Modern, clean design with light/dark themes
- **Multiple Formats**: Export to SVG, PNG, PDF, or interactive HTML
- **Developer-Friendly**: Simple API, integrates with documentation tools

### Is RenderSchema free?

Yes! RenderSchema is open-source under the MIT License. You can use it freely in personal and commercial projects.

## Installation & Setup

### How do I install RenderSchema?

```bash
pip install renderschema
```

For PNG/PDF export support:
```bash
pip install renderschema[export]
```

### What Python versions are supported?

Python 3.8 and higher.

### Do I need to install any system dependencies?

Only if you want PNG/PDF export. In that case, you'll need:

- **Linux**: `sudo apt-get install libcairo2-dev`
- **macOS**: `brew install cairo`
- **Windows**: Cairo is bundled with cairosvg

### Can I use RenderSchema without installing optional dependencies?

Yes! SVG and HTML exports work without any additional dependencies. Only PNG and PDF require `cairosvg`.

## Usage

### How do I generate my first diagram?

```python
from renderschema import diagram

# Analyze a class
class MyClass:
    def __init__(self):
        self.value = 42
    
    def method(self):
        pass

diag = diagram(MyClass)
diag.export("output.svg")
```

### What can I pass to the `diagram()` function?

- Python classes
- Python modules
- File paths (`.py` files)
- Directory paths (analyzes all Python files)
- Lists of classes

### How do I generate different diagram types?

```python
# UML class diagram (default)
diagram(MyClass, diagram_type="uml")

# Flowchart
diagram(my_function, diagram_type="flowchart")

# Class relationships
diagram([Class1, Class2], diagram_type="class")
```

### How do I switch between light and dark themes?

```python
# Dark theme (default)
diagram(MyClass, theme="dark").export("dark.svg")

# Light theme
diagram(MyClass, theme="light").export("light.svg")
```

### Can I customize colors and styles?

Currently, RenderSchema uses predefined Tailwind-inspired color schemes. Custom theme support is planned for version 0.3.0. See [ROADMAP.md](ROADMAP.md).

## Export Formats

### What formats can I export to?

- **SVG**: Vector graphics (no dependencies)
- **PNG**: Raster image (requires cairosvg)
- **PDF**: Portable document (requires cairosvg)
- **HTML**: Interactive diagram with zoom/pan (no dependencies)

### How do I export to multiple formats?

```python
diag = diagram(MyClass)
diag.export("output.svg")  # SVG
diag.export("output.png")  # PNG
diag.export("output.pdf")  # PDF
diag.export("output.html") # HTML
```

### Why do HTML exports include the full SVG?

For portability! HTML exports are self-contained files with embedded SVG and JavaScript. No external files needed.

### Can I get just the SVG string without saving to a file?

```python
svg_string = diagram(MyClass).to_svg()
```

### How do I control export quality for PNG?

PNG export resolution is determined by the SVG dimensions. For higher quality, you can scale the SVG before converting (this will be added as a feature in 0.2.0).

## Diagram Types

### What information is shown in UML diagrams?

- Class name
- Attributes with types
- Methods with parameters and return types
- Access modifiers (public: +, private: -)
- Inheritance relationships

### Why doesn't my flowchart show all control flow?

The current flowchart implementation (v0.1.x) is basic. Full control flow analysis (if/else, loops, try/except) is planned for version 0.3.0. See [ROADMAP.md](ROADMAP.md).

### Can I generate ER diagrams for databases?

Not yet. Entity-Relationship diagrams are planned for version 0.2.0.

### How do I visualize module structure?

```python
import mypackage
diagram(mypackage, diagram_type="uml")
```

This analyzes all classes in the module and shows their relationships.

## Integration

### Can I use RenderSchema with Sphinx?

Yes! You can use RenderSchema in custom Sphinx extensions. Native Sphinx directive support is planned for version 0.4.0.

Current workaround:
```python
# In conf.py or custom extension
from renderschema import diagram
import myproject

# Generate during build
diagram(myproject).export("_static/architecture.svg")
```

### Does RenderSchema work with MkDocs?

Yes! Generate diagrams in a pre-build script and reference them in your Markdown:

```python
# generate_diagrams.py
from renderschema import diagram
import myproject

diagram(myproject).export("docs/diagrams/architecture.svg")
```

```markdown
<!-- In your .md file -->
![Architecture](diagrams/architecture.svg)
```

Native MkDocs plugin support is planned for version 0.4.0.

### Can I use RenderSchema in Jupyter notebooks?

Yes! For now, export to a file and display:

```python
from renderschema import diagram
from IPython.display import SVG

diagram(MyClass).export("diagram.svg")
SVG("diagram.svg")
```

Native IPython display support is planned for version 0.4.0.

## Troubleshooting

### Why is my diagram empty?

- **Check that your target has content**: Empty modules produce empty diagrams
- **Verify imports**: Make sure modules are importable
- **Check file paths**: Use absolute paths or ensure files are in Python path

### Why are some classes missing from my diagram?

- **Private classes**: Classes starting with `_` are excluded by default
- **Import errors**: Classes that fail to import are skipped
- **File discovery**: Only `.py` files in analyzed directories are included

### I get "ModuleNotFoundError" when analyzing my project

Make sure your project is installed or in `PYTHONPATH`:

```python
import sys
sys.path.insert(0, '/path/to/your/project')

from renderschema import diagram
diagram('/path/to/your/project').export("output.svg")
```

### PNG/PDF export fails with "Cairo not found"

Install Cairo library:

- **Linux**: `sudo apt-get install libcairo2-dev`
- **macOS**: `brew install cairo`
- **Windows**: Should work automatically with `pip install renderschema[export]`

If issues persist, stick with SVG or HTML export.

### My diagram is too large/small

SVG sizing is automatic based on content. For custom sizing:

- **SVG**: Edit the `width` and `height` attributes in the SVG file
- **HTML**: Use browser zoom or modify the viewport in the HTML file
- **PNG/PDF**: Resolution control is coming in version 0.2.0

## Performance

### How long does it take to generate diagrams?

- **Small projects** (< 10 classes): < 1 second
- **Medium projects** (10-100 classes): 1-5 seconds
- **Large projects** (100+ classes): 5-30 seconds

Performance optimization is planned for version 0.4.0.

### Can I speed up diagram generation?

Tips:
- Analyze specific modules instead of entire projects
- Use file-level analysis instead of importing (avoids executing module code)
- Cache results and only regenerate when code changes (caching coming in 0.4.0)

### Is there a size limit for projects?

No hard limit, but very large projects (1000+ classes) may be slow and produce cluttered diagrams. Consider generating multiple focused diagrams instead of one huge diagram.

## Contributing

### How can I contribute?

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines. Quick options:

- Report bugs
- Suggest features
- Improve documentation
- Submit pull requests
- Help others in discussions

### I found a bug. What should I include in the report?

- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Python version and OS
- RenderSchema version
- Minimal code example

See [SUPPORT.md](SUPPORT.md) for details.

### Can I add support for other programming languages?

Yes! Multi-language support is planned for version 0.3.0. If you want to contribute language support earlier, check the [ROADMAP.md](ROADMAP.md) and open an issue to discuss the approach.

## License & Legal

### What license is RenderSchema under?

MIT License - see [LICENSE](../LICENSE) file for details.

### Can I use RenderSchema in commercial projects?

Yes! The MIT License allows commercial use.

### Do I need to credit RenderSchema in my documentation?

Not required by the license, but appreciated! A simple mention or link to the project helps others discover it.

### Can I modify RenderSchema for my needs?

Yes! You can fork and modify it under the MIT License terms.

## Getting Help

Still have questions?

- 📚 Check the [documentation](../README.md)
- 🐛 [Report bugs](https://github.com/juliuspleunes4/RenderSchema/issues)
- 💡 [Request features](https://github.com/juliuspleunes4/RenderSchema/issues)
- 💬 [Start a discussion](https://github.com/juliuspleunes4/RenderSchema/discussions)
- 📧 Email: jjgpleunes@gmail.com (security issues only)

See [SUPPORT.md](SUPPORT.md) for more details.
