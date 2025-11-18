# 🎨 RenderSchema

<div align="center">

**Automatically generate beautiful documentation diagrams from Python code**

[![PyPI version](https://img.shields.io/pypi/v/renderschema.svg)](https://pypi.org/project/renderschema/)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

</div>

---

## ✨ Features

- 🚀 **Zero-Config Diagram Generation** - Turn Python classes into UML diagrams with one line of code
- 🎨 **Beautiful by Default** - Clean, modern diagrams with Tailwind-inspired color schemes
- 🌓 **Light & Dark Themes** - Perfect for documentation in any style
- 📊 **Multiple Diagram Types** - UML class diagrams, flowcharts, and class relationships
- 🖼️ **Multiple Export Formats** - SVG, PNG, PDF, and interactive HTML
- 🔍 **Interactive HTML** - Zoomable, pannable diagrams for web documentation
- 🎯 **Type-Safe** - Full type hints for excellent IDE support
- 📦 **Framework Integration** - Works seamlessly with Sphinx, MkDocs, and more

## 🎯 Why RenderSchema?

Developers **love** diagrams but **hate** making them. RenderSchema solves this by automatically generating clean, professional diagrams from your Python code. No more manual diagramming tools or outdated documentation!

## 📦 Installation

```bash
# Basic installation
pip install renderschema

# With PNG/PDF export support
pip install renderschema[image]

# Full installation (all features)
pip install renderschema[all]
```

## 🚀 Quick Start

### Generate a UML Diagram

```python
from renderschema import diagram

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def greet(self) -> str:
        return f"Hello, I'm {self.name}!"

# Generate diagram - it's that simple!
diagram(Person).export("person.svg")
```

### Create a Flowchart

```python
from renderschema import diagram

def calculate_discount(price: float, customer_type: str) -> float:
    if customer_type == "vip":
        return price * 0.8
    elif customer_type == "premium":
        return price * 0.9
    else:
        return price

diagram(calculate_discount, diagram_type="flowchart").export("discount.svg")
```

### Visualize Class Relationships

```python
from renderschema import diagram

class Animal:
    pass

class Dog(Animal):
    def bark(self): pass

class Cat(Animal):
    def meow(self): pass

diagram([Animal, Dog, Cat], diagram_type="class").export("animals.svg")
```

## 🎨 Themes

RenderSchema supports both light and dark themes:

```python
# Light theme (default)
diagram(MyClass, theme="light").export("light.svg")

# Dark theme - perfect for dark mode documentation
diagram(MyClass, theme="dark").export("dark.svg")
```

## 📤 Export Formats

Export to multiple formats based on your needs:

```python
# SVG - vector graphics, perfect for web and scaling
diagram(MyClass).export("output.svg")

# PNG - raster image (requires cairosvg)
diagram(MyClass).export("output.png")

# PDF - for print documentation (requires cairosvg)
diagram(MyClass).export("output.pdf")

# Interactive HTML - zoomable and pannable
diagram(MyClass).export("output.html")
```

## 💡 Advanced Usage

### Get Diagrams as Strings

```python
# Get SVG markup as string
svg_content = diagram(MyClass).to_svg()

# Get interactive HTML as string
html_content = diagram(MyClass).to_html(interactive=True)
```

### Analyze Before Generating

```python
generator = diagram(MyClass)
data = generator.analyze()  # Get structured data about the class
svg = generator.generate()   # Generate the diagram
```

### Custom Options

```python
# Customize diagram generation
diagram(
    MyClass,
    theme="dark",
    color_scheme="tailwind"
).export("custom.svg")
```

## 📚 Documentation

- **[Quick Start Guide](docs/QUICKSTART.md)** - Get up and running in minutes
- **[Contributing Guide](CONTRIBUTING.md)** - Help make RenderSchema better
- **[Changelog](docs/CHANGELOG.md)** - See what's new
- **[Examples](examples/)** - Explore more detailed examples

## 🛠️ Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/juliuspleunes4/RenderSchema.git
cd RenderSchema

# Install with development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black renderschema/ tests/

# Lint code
ruff check renderschema/ tests/

# Type check
mypy renderschema/
```

### Running Examples

```bash
cd examples
python basic_uml.py
python flowchart_example.py
python class_relationships.py
```

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

**Important**: All changes must be documented in [`docs/CHANGELOG.md`](docs/CHANGELOG.md). Never create separate `.md` files to explain changes.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Roadmap

- [ ] More diagram types (sequence diagrams, state machines)
- [ ] Custom styling and color schemes
- [ ] Advanced layout algorithms
- [ ] Integration with popular documentation tools
- [ ] Module and package-level diagrams
- [ ] Real-time diagram preview in editors

## 🙏 Acknowledgments

Built with ❤️ by [Julius Pleunes](https://github.com/juliuspleunes4)

Inspired by the need for effortless, beautiful diagram generation for Python developers.

---

<div align="center">

**[⬆ back to top](#-renderschema)**

Made with ❤️ for the Python community

</div>