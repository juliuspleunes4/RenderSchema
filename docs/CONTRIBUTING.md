# Contributing to RenderSchema

Thank you for your interest in contributing to RenderSchema! This document provides guidelines for contributing to the project.

## Development Setup

1. Clone the repository
2. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

## Code Standards

- Follow PEP 8 style guidelines
- Use type hints for all functions
- Write comprehensive docstrings
- Maintain test coverage above 80%

## Testing

Run tests with pytest:
```bash
pytest
```

Run with coverage:
```bash
pytest --cov=renderschema --cov-report=html
```

## Code Quality Tools

Format code with black:
```bash
black renderschema/ tests/
```

Lint with ruff:
```bash
ruff check renderschema/ tests/
```

Type check with mypy:
```bash
mypy renderschema/
```

## Documentation

- **CRITICAL**: All changes must be documented in `docs/CHANGELOG.md`
- Never create separate `.md` files to explain changes
- Update docstrings when modifying function signatures
- Add examples for new features

## Pull Request Process

1. Create a feature branch from `main`
2. Make your changes following the code standards
3. Add tests for new functionality
4. Update `docs/CHANGELOG.md` under `[Unreleased]`
5. Ensure all tests pass
6. Submit a pull request with a clear description

## Commit Messages

Use clear, descriptive commit messages:
- `feat: add support for custom color schemes`
- `fix: resolve SVG export encoding issue`
- `docs: update API documentation`
- `test: add tests for flowchart generator`

## Questions?

Open an issue for questions or discussion about potential contributions.
