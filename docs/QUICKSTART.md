# RenderSchema Quick Start Guide

## Installation

```bash
# Install the package
pip install renderschema

# For PNG/PDF export support
pip install renderschema[image]

# For development
pip install renderschema[dev]
```

## Basic Usage

### 1. Generate a UML Diagram

```python
from renderschema import diagram

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def greet(self) -> str:
        return f"Hello, I'm {self.name}!"

# Generate and export
diagram(Person).export("person.svg")
```

### 2. Create a Flowchart

```python
from renderschema import diagram

def calculate_tax(income: float) -> float:
    if income < 10000:
        return income * 0.1
    elif income < 50000:
        return income * 0.2
    else:
        return income * 0.3

diagram(calculate_tax, diagram_type="flowchart").export("tax_flow.svg")
```

### 3. Visualize Class Relationships

```python
from renderschema import diagram

class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

diagram([Animal, Dog, Cat], diagram_type="class").export("animals.svg")
```

## Export Formats

```python
from renderschema import diagram

# SVG (default, recommended)
diagram(MyClass).export("output.svg")

# PNG (requires cairosvg)
diagram(MyClass).export("output.png")

# PDF (requires cairosvg)
diagram(MyClass).export("output.pdf")

# Interactive HTML
diagram(MyClass).export("output.html")
```

## Themes

```python
# Light theme (default)
diagram(MyClass, theme="light").export("light.svg")

# Dark theme
diagram(MyClass, theme="dark").export("dark.svg")
```

## Advanced Usage

```python
# Get SVG as string
svg_content = diagram(MyClass).to_svg()

# Get interactive HTML as string
html_content = diagram(MyClass).to_html(interactive=True)

# Customize options
diagram(MyClass, theme="dark", color_scheme="tailwind").export("custom.svg")
```

## Running Examples

```bash
cd examples
python basic_uml.py
python flowchart_example.py
python class_relationships.py
```

## Next Steps

- Check out the `examples/` directory for more detailed examples
- Read the API documentation for advanced features
- Contribute to the project on GitHub!
