# API Reference

Complete reference for all RenderSchema features and APIs.

---

## Table of Contents

- [Core Function](#core-function)
- [Diagram Generators](#diagram-generators)
  - [UML Diagram Generator](#uml-diagram-generator)
  - [Flowchart Generator](#flowchart-generator)
  - [Class Diagram Generator](#class-diagram-generator)
- [Exporters](#exporters)
- [Themes and Styling](#themes-and-styling)
- [Advanced Usage](#advanced-usage)

---

## Core Function

### `diagram()`

The main entry point for creating diagrams.

```python
from renderschema import diagram

generator = diagram(
    target,
    diagram_type="uml",
    theme="light",
    color_scheme="tailwind",
    **options
)
```

#### Parameters

- **`target`** (Type, object, str, Path) - Required
  - Python class to diagram
  - Python function (for flowcharts)
  - Module object
  - List of classes (for relationship diagrams)
  - Path to file or directory (string or Path object)

- **`diagram_type`** (str) - Optional, default: `"uml"`
  - `"uml"` - UML class diagram
  - `"flowchart"` - Function flowchart
  - `"class"` - Class relationship diagram

- **`theme`** (str) - Optional, default: `"light"`
  - `"light"` - Light theme with bright backgrounds
  - `"dark"` - Dark theme for dark mode documentation

- **`color_scheme`** (str) - Optional, default: `"tailwind"`
  - `"tailwind"` - Tailwind CSS inspired colors

- **`**options`** - Additional generator-specific options

#### Returns

Returns a diagram generator instance (subclass of `BaseDiagramGenerator`).

#### Example

```python
from renderschema import diagram

class MyClass:
    def __init__(self, name: str):
        self.name = name

# Create a UML diagram generator
gen = diagram(MyClass, theme="dark")
gen.export("output.svg")
```

---

## Diagram Generators

### UML Diagram Generator

Generates UML class diagrams showing class structure, attributes, methods, and visibility.

#### Usage

```python
from renderschema import diagram

class Person:
    """A person with a name and age."""
    
    name: str
    age: int
    
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    def greet(self) -> str:
        """Return a greeting."""
        return f"Hello, I'm {self.name}!"
    
    def _private_method(self) -> None:
        """Private helper method."""
        pass

# Generate UML diagram
diagram(Person).export("person.svg")
```

#### Features

- **Automatic Detection**:
  - Class name and module
  - Public, protected, and private members
  - Method signatures with parameters
  - Return type annotations
  - Type hints for attributes
  - Inheritance (base classes)

- **Visibility Indicators**:
  - `+` Public members
  - `#` Protected members (prefix `_`)
  - `-` Private members (prefix `__`)

- **Supports**:
  - Single classes
  - Modules (analyzes all classes in module)
  - File paths (future feature)

#### Methods

**`analyze()`** - Analyze the target and extract UML information

```python
generator = diagram(MyClass)
data = generator.analyze()
# Returns: {
#     "name": "MyClass",
#     "module": "__main__",
#     "bases": ["BaseClass"],
#     "attributes": [...],
#     "methods": [...],
#     "docstring": "..."
# }
```

**`generate()`** - Generate SVG markup

```python
svg_content = generator.generate()
```

**`export(output_path, format=None)`** - Export to file

```python
generator.export("diagram.svg")
generator.export("diagram.png")  # Format auto-detected from extension
generator.export("output", format="png")  # Explicit format when no extension
```

---

### Flowchart Generator

Generates flowcharts from Python functions showing control flow.

#### Usage

```python
from renderschema import diagram

def calculate_discount(price: float, customer_type: str) -> float:
    """Calculate price with discount."""
    if customer_type == "vip":
        discount = 0.20
    elif customer_type == "premium":
        discount = 0.10
    else:
        discount = 0.0
    
    final_price = price * (1 - discount)
    
    if final_price < 10:
        final_price = 10
    
    return final_price

# Generate flowchart
diagram(calculate_discount, diagram_type="flowchart").export("flow.svg")
```

#### Features

- Extracts control flow from function AST
- Visualizes conditional branches (if/elif/else)
- Shows loops (for, while)
- Start and end nodes
- Process nodes for operations

#### Methods

Same as UML Generator: `analyze()`, `generate()`, `export()`

#### Current Limitations

- Basic control flow extraction (placeholders for complex logic)
- Future versions will support more advanced AST analysis

---

### Class Diagram Generator

Generates class relationship diagrams focusing on inheritance and associations.

#### Usage

```python
from renderschema import diagram

class Animal:
    def make_sound(self) -> str:
        return "<sound>"

class Dog(Animal):
    def make_sound(self) -> str:
        return "Woof!"

class Cat(Animal):
    def make_sound(self) -> str:
        return "Meow!"

# Generate class relationship diagram
diagram([Animal, Dog, Cat], diagram_type="class").export("animals.svg")
```

#### Features

- Inheritance relationships with arrows
- Multiple class visualization
- Simple, clean layout
- Focus on relationships, not details

#### Accepts

- **List of classes**: `[ClassA, ClassB, ClassC]`
- **Module**: All classes from module

#### Methods

Same as other generators: `analyze()`, `generate()`, `export()`

---

## Exporters

### Export Methods

All diagram generators support the following export formats:

#### SVG Export

Vector graphics format, perfect for web and scaling.

```python
from renderschema import diagram

# Default SVG export
diagram(MyClass).export("output.svg")

# Explicit format
diagram(MyClass).export("output.svg", format="svg")
```

**Features**:
- Scalable without quality loss
- Small file size
- Editable in vector graphics editors
- Embeddable in HTML

---

#### PNG Export

Raster image format. Requires `cairosvg` library.

```python
# Install cairosvg first
# pip install renderschema[image]

diagram(MyClass).export("output.png")
```

**Features**:
- Fixed resolution
- Widely supported
- Good for documentation tools that need raster images

**Requirements**: `pip install cairosvg`

---

#### PDF Export

Portable document format. Requires `cairosvg` library.

```python
# Install cairosvg first
# pip install renderschema[image]

diagram(MyClass).export("output.pdf")
```

**Features**:
- Print-ready
- Embeddable in PDF documents
- Professional documentation

**Requirements**: `pip install cairosvg`

---

#### HTML Export

Interactive HTML with zoom and pan capabilities.

```python
diagram(MyClass).export("output.html")

# Note: HTML exports are always interactive by default
# Use to_html() method for non-interactive HTML
```

**Features**:
- Interactive viewing (zoom and pan enabled by default)
- Standalone HTML file
- Responsive design
- No external dependencies

---

### Direct Output Methods

#### `to_svg()`

Get SVG markup as a string.

```python
generator = diagram(MyClass)
svg_content = generator.to_svg()
print(svg_content)  # Raw SVG markup
```

**Use cases**:
- Embed in web applications
- Process SVG programmatically
- Custom rendering pipelines

---

#### `to_html()`

Get interactive HTML as a string.

```python
generator = diagram(MyClass)
html_content = generator.to_html(interactive=True)

# Save manually
with open("diagram.html", "w") as f:
    f.write(html_content)
```

**Parameters**:
- `interactive` (bool) - Default: `True`. Enable zoom/pan.

**Use cases**:
- Embed in documentation generators
- Custom web applications
- Dynamic report generation

---

## Themes and Styling

### Light Theme

Default theme with bright backgrounds and dark text.

```python
diagram(MyClass, theme="light").export("output.svg")
```

**Colors** (Tailwind-inspired):
- Background: `#ffffff` (white)
- Borders: `#3b82f6` (blue-500)
- Text: `#1f2937` (gray-800)
- Secondary text: `#374151` (gray-700)

---

### Dark Theme

Dark mode theme for modern documentation.

```python
diagram(MyClass, theme="dark").export("output.svg")
```

**Colors** (Tailwind-inspired):
- Background: `#1f2937` (gray-800)
- Borders: `#4b5563` (gray-600)
- Text: `#f9fafb` (gray-50)
- Secondary text: `#d1d5db` (gray-300)

---

### Theme Usage Examples

```python
# Light theme (default)
diagram(MyClass).export("light.svg")

# Dark theme
diagram(MyClass, theme="dark").export("dark.svg")

# Both themes for the same class
gen_light = diagram(MyClass, theme="light")
gen_dark = diagram(MyClass, theme="dark")

gen_light.export("light.svg")
gen_dark.export("dark.svg")
```

---

## Advanced Usage

### Analyzing Before Generation

Inspect the analyzed data before generating diagrams.

```python
from renderschema import diagram

class Example:
    value: int = 0
    
    def method(self) -> str:
        return "result"

generator = diagram(Example)

# Get analyzed data
data = generator.analyze()
print(data["name"])        # "Example"
print(data["attributes"])  # List of attributes
print(data["methods"])     # List of methods

# Generate diagram using analyzed data
svg = generator.generate()
```

---

### Working with Modules

Generate diagrams for all classes in a module.

```python
import my_module

# Analyze entire module
diagram(my_module).export("module_diagram.svg")

# This will create UML diagrams for all classes in my_module
```

---

### Custom Export Paths

All export methods support flexible path handling.

```python
from pathlib import Path

# String paths
diagram(MyClass).export("output.svg")

# Path objects
output_path = Path("diagrams/output.svg")
diagram(MyClass).export(output_path)

# Creates parent directories automatically
diagram(MyClass).export("deep/nested/path/diagram.svg")
```

---

### Batch Generation

Generate multiple diagrams efficiently.

```python
classes = [ClassA, ClassB, ClassC]

for cls in classes:
    filename = f"{cls.__name__.lower()}.svg"
    diagram(cls, theme="dark").export(filename)

# Or as a relationship diagram
diagram(classes, diagram_type="class").export("relationships.svg")
```

---

### Integration with Documentation Tools

#### Sphinx

```python
# In your Sphinx conf.py or documentation script
from renderschema import diagram
import my_project

# Generate diagrams during doc build
for cls in [ClassA, ClassB, ClassC]:
    svg_path = f"_static/diagrams/{cls.__name__}.svg"
    diagram(cls).export(svg_path)
```

Then reference in RST:

```rst
.. image:: _static/diagrams/ClassA.svg
   :alt: ClassA UML Diagram
```

#### MkDocs

```python
# In a docs generation script
from renderschema import diagram

diagram(MyClass).export("docs/images/myclass.svg")
```

Then reference in Markdown:

```markdown
![MyClass Diagram](images/myclass.svg)
```

---

### Error Handling

Handle errors gracefully when generating diagrams.

```python
from renderschema import diagram

try:
    diagram("invalid_target").export("output.svg")
except TypeError as e:
    print(f"Invalid target type: {e}")

try:
    diagram(MyClass).export("output.xyz")
except ValueError as e:
    print(f"Unsupported format: {e}")

# Check if format is supported before exporting
supported_formats = ["svg", "png", "pdf", "html"]
format = "svg"

if format in supported_formats:
    diagram(MyClass).export(f"output.{format}")
```

---

### Performance Considerations

For large codebases or many diagrams:

```python
# Reuse generators when possible
generator = diagram(MyClass, theme="dark")

# Export to multiple formats without re-analyzing
generator.export("output.svg")
generator.export("output.png")
generator.export("output.html")

# Get string representations without file I/O
svg_content = generator.to_svg()
html_content = generator.to_html()
```

---

## Complete Example

Putting it all together:

```python
from renderschema import diagram
from pathlib import Path

# Define classes
class Animal:
    """Base animal class."""
    name: str
    
    def __init__(self, name: str):
        self.name = name
    
    def make_sound(self) -> str:
        return "<sound>"

class Dog(Animal):
    """A dog."""
    breed: str
    
    def __init__(self, name: str, breed: str):
        super().__init__(name)
        self.breed = breed
    
    def make_sound(self) -> str:
        return "Woof!"

# Create output directory
output_dir = Path("diagrams")
output_dir.mkdir(exist_ok=True)

# Generate various diagrams
themes = ["light", "dark"]

for theme in themes:
    # Individual class diagrams
    for cls in [Animal, Dog]:
        filename = f"{cls.__name__.lower()}_{theme}.svg"
        diagram(cls, theme=theme).export(output_dir / filename)
    
    # Class relationship diagram
    diagram([Animal, Dog], diagram_type="class", theme=theme).export(
        output_dir / f"relationships_{theme}.svg"
    )

# Generate interactive HTML
diagram(Dog, theme="dark").export(output_dir / "dog_interactive.html")

# Get SVG as string for embedding
svg_content = diagram(Animal).to_svg()
print(f"Generated SVG: {len(svg_content)} characters")

print(f"✓ Generated {len(themes) * 3} diagrams in {output_dir}/")
```

---

## API Summary

### Functions

| Function | Description |
|----------|-------------|
| `diagram(target, diagram_type, theme, **options)` | Create diagram generator |

### Classes

| Class | Purpose |
|-------|---------|
| `BaseDiagramGenerator` | Abstract base for all generators |
| `UMLDiagramGenerator` | UML class diagrams |
| `FlowchartGenerator` | Function flowcharts |
| `ClassDiagramGenerator` | Class relationships |
| `SVGExporter` | Export to SVG |
| `PNGExporter` | Export to PNG |
| `PDFExporter` | Export to PDF |
| `HTMLExporter` | Export to HTML |

### Methods (All Generators)

| Method | Returns | Description |
|--------|---------|-------------|
| `.analyze()` | dict | Extract structure from target |
| `.generate()` | str | Generate SVG markup |
| `.export(path, format)` | None | Save diagram to file |
| `.to_svg()` | str | Get SVG as string |
| `.to_html(interactive)` | str | Get HTML as string |

### Supported Formats

| Format | Extension | Requirements | Use Case |
|--------|-----------|--------------|----------|
| SVG | `.svg` | None | Web, scalable graphics |
| PNG | `.png` | `cairosvg` | Raster images |
| PDF | `.pdf` | `cairosvg` | Print, documents |
| HTML | `.html` | None | Interactive viewing |

---

## Next Steps

- See [Quick Start Guide](QUICKSTART.md) for getting started
- Check [Examples](../examples/) for more code samples
- Read [Contributing Guide](../CONTRIBUTING.md) to help improve RenderSchema
