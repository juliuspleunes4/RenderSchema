"""
Basic example: Generate a UML diagram from a Python class.
"""

from renderschema import diagram


class Person:
    """A simple Person class."""
    
    def __init__(self, name: str, age: int) -> None:
        """Initialize a person with name and age."""
        self.name = name
        self.age = age
    
    def greet(self) -> str:
        """Return a greeting message."""
        return f"Hello, I'm {self.name}!"
    
    def celebrate_birthday(self) -> None:
        """Increment age by one."""
        self.age += 1


class Employee(Person):
    """An Employee is a Person with a job title."""
    
    def __init__(self, name: str, age: int, title: str) -> None:
        """Initialize an employee."""
        super().__init__(name, age)
        self.title = title
    
    def work(self) -> str:
        """Return a work message."""
        return f"{self.name} is working as {self.title}"


if __name__ == "__main__":
    # Generate UML diagram for a single class
    print("Generating UML diagram for Person class...")
    diagram(Person).export("person_uml.svg")
    print("✓ Saved to person_uml.svg")
    
    # Generate with dark theme
    print("\nGenerating dark theme UML diagram...")
    diagram(Employee, theme="dark").export("employee_uml_dark.svg")
    print("✓ Saved to employee_uml_dark.svg")
    
    # Export to HTML (interactive)
    print("\nGenerating interactive HTML diagram...")
    diagram(Person).export("person_diagram.html")
    print("✓ Saved to person_diagram.html")
