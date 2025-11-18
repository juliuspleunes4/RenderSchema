# RenderSchema Examples

This directory contains example scripts demonstrating how to use RenderSchema.

## Running Examples

Each example can be run independently:

```bash
# Basic UML diagram generation
python basic_uml.py

# Flowchart from function
python flowchart_example.py

# Class relationship diagrams
python class_relationships.py
```

## Examples Overview

### `basic_uml.py`
Demonstrates generating UML class diagrams from Python classes with light/dark themes and HTML export.

### `flowchart_example.py`
Shows how to create flowcharts from Python functions to visualize control flow.

### `class_relationships.py`
Illustrates generating class relationship diagrams showing inheritance hierarchies.

## Output

All examples generate diagram files in the current directory:
- `.svg` - Vector graphics (scalable, recommended)
- `.html` - Interactive HTML with zoom/pan capabilities

## Next Steps

After running these examples, try:
- Generating diagrams for your own classes
- Experimenting with different themes
- Exporting to PNG/PDF (requires `cairosvg`)
