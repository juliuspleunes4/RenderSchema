"""Test configuration and fixtures for pytest."""

import pytest


@pytest.fixture
def sample_svg():
    """Fixture providing sample SVG content."""
    return """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300">
    <rect x="50" y="50" width="300" height="200" fill="#ffffff" stroke="#000000"/>
    <text x="200" y="150" text-anchor="middle">Test Diagram</text>
</svg>"""


@pytest.fixture
def sample_class():
    """Fixture providing a sample class for testing."""
    class TestClass:
        """A test class with various members."""
        
        class_attr: str = "value"
        
        def __init__(self, name: str) -> None:
            self.name = name
        
        def public_method(self) -> str:
            """Public method."""
            return self.name
        
        def _protected_method(self) -> None:
            """Protected method."""
            pass
        
        def __private_method(self) -> None:
            """Private method."""
            pass
    
    return TestClass
