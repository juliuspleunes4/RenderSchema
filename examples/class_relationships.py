"""
Class relationship example: Generate diagrams showing inheritance.
"""

from renderschema import diagram


class Animal:
    """Base animal class."""
    
    def __init__(self, name: str) -> None:
        self.name = name
    
    def make_sound(self) -> str:
        """Make a sound."""
        return "<generic animal sound>"


class Dog(Animal):
    """A dog is an animal."""
    
    def make_sound(self) -> str:
        """Dogs bark."""
        return "Woof!"


class Cat(Animal):
    """A cat is an animal."""
    
    def make_sound(self) -> str:
        """Cats meow."""
        return "Meow!"


class Bird(Animal):
    """A bird is an animal."""
    
    def make_sound(self) -> str:
        """Birds chirp."""
        return "Chirp!"


if __name__ == "__main__":
    # Generate class relationship diagram for multiple classes
    print("Generating class relationship diagram...")
    diagram(
        [Animal, Dog, Cat, Bird],
        diagram_type="class"
    ).export("animals_class_diagram.svg")
    print("✓ Saved to animals_class_diagram.svg")
    
    # With dark theme
    print("\nGenerating dark theme class diagram...")
    diagram(
        [Animal, Dog, Cat, Bird],
        diagram_type="class",
        theme="dark"
    ).export("animals_class_diagram_dark.svg")
    print("✓ Saved to animals_class_diagram_dark.svg")
