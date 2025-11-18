# GitHub Copilot Instructions for RenderSchema

## Project Overview

**RenderSchema** is a Python library that automatically generates beautiful, readable documentation diagrams from Python code. It converts Python classes, modules, and project structures into clean UML diagrams, flowcharts, class relationships, and architectural visualizations.

### Core Purpose
- Auto-render UML diagrams, flowcharts, and class relationships
- Generate hyper-clean, modern diagrams with light/dark mode support
- Export to multiple formats (SVG, PNG, PDF, clickable HTML)
- Integrate seamlessly with Sphinx and Markdown documentation
- Make diagram generation effortless for developers who hate manual diagramming

### Example Usage
```python
from renderschema import diagram
diagram(MyProject).export("architecture.svg")
```

---

## Development Guidelines

### 1. Code Quality Standards

#### ✅ DO:
- Follow PEP 8 style guidelines strictly
- Use type hints for all function signatures and class attributes
- Write comprehensive docstrings (Google or NumPy style)
- Implement proper error handling with descriptive exception messages
- Create unit tests for all new features and bug fixes
- Use meaningful variable and function names that are self-documenting
- Keep functions focused and modular (single responsibility principle)
- Add inline comments for complex logic or algorithms

#### ❌ DON'T:
- Never implement mock data in production code
- Use placeholders where test data is needed temporarily
- Avoid hardcoded values; use configuration or constants
- Don't commit commented-out code blocks
- Never skip error handling or validation

### 2. Data Handling

**CRITICAL**: When examples or test data are needed:
- ✅ Use **placeholders** (e.g., `"<class_name>"`, `"<module_path>"`)
- ✅ Use **minimal, realistic examples** that demonstrate functionality
- ❌ **NEVER** create elaborate mock data structures
- ❌ **NEVER** use fake/dummy production-like data

### 3. Documentation Requirements

#### Change Documentation
**CRITICAL RULE**: All changes must be documented in `docs/CHANGELOG.md`. 

**NEVER**:
- ❌ Create new `.md` files to explain changes
- ❌ Create separate summary files
- ❌ Create `CHANGES.md`, `UPDATES.md`, or similar files
- ❌ Document changes in comments within code files (except inline docs)

**ALWAYS**:
- ✅ Add all changes to `docs/CHANGELOG.md` following the format:
  ```markdown
  ## [Unreleased]
  
  ### Added
  - New feature descriptions
  
  ### Changed
  - Modified functionality
  
  ### Fixed
  - Bug fixes
  
  ### Removed
  - Deprecated features
  ```

#### Code Documentation
- Maintain comprehensive `README.md` with usage examples
- Update API documentation in docstrings
- Keep inline comments focused on "why" not "what"

### 4. Open Source Best Practices

This is an open-source project. Always adhere to:

- **Licensing**: Respect the project license in all contributions
- **Community standards**: Write code that others can easily understand and maintain
- **Transparency**: Document breaking changes clearly
- **Versioning**: Follow semantic versioning principles (MAJOR.MINOR.PATCH)
- **Contribution-friendly**: Keep code modular and well-tested for contributors
- **Professional commits**: Use clear, descriptive commit messages
- **Issue tracking**: Reference relevant issues in commit messages and CHANGELOG

### 5. Testing Strategy

- Write unit tests using `pytest`
- Aim for high code coverage (>80%)
- Include edge cases and error conditions
- Test all export formats (SVG, PNG, PDF, HTML)
- Test light/dark mode rendering
- Create integration tests for end-to-end workflows

### 6. Architecture Principles

- **Modularity**: Keep diagram generators separate by type (UML, flowchart, etc.)
- **Extensibility**: Design for easy addition of new diagram types
- **Performance**: Optimize for large codebases
- **Configurability**: Allow customization of colors, styles, and layouts
- **Integration**: Build with Sphinx, MkDocs, and other doc tools in mind

### 7. Dependencies

- Minimize external dependencies
- Use well-maintained, popular libraries
- Pin dependency versions for stability
- Document all required and optional dependencies

### 8. Visual Design Standards

- Use Tailwind-inspired color palettes
- Support both light and dark themes
- Ensure accessibility (readable colors, proper contrast)
- Create clean, minimalist diagrams
- Use consistent spacing and alignment

---

## Quick Reference

### When adding a new feature:
1. Implement the feature with proper type hints and docstrings
2. Write comprehensive tests
3. Update `README.md` if it affects user-facing API
4. **Document in `docs/CHANGELOG.md` under `[Unreleased]` → `### Added`**
5. Never create separate documentation files

### When fixing a bug:
1. Write a test that reproduces the bug
2. Fix the issue
3. Verify the test passes
4. **Document in `docs/CHANGELOG.md` under `[Unreleased]` → `### Fixed`**

### When refactoring:
1. Ensure all existing tests still pass
2. Add tests for any new edge cases
3. Update docstrings if behavior changes
4. **Document in `docs/CHANGELOG.md` under `[Unreleased]` → `### Changed`**

---

## About Me

I am Julius Pleunes.
GitHub: juliuspleunes4
This repo: https://github.com/juliuspleunes4/RenderSchema.git
Email: jjgpleunes@gmail.com

---

## About Me

I am Julius Pleunes.
GitHub: juliuspleunes4
This repo: https://github.com/juliuspleunes4/RenderSchema.git
Email: jjgpleunes@gmail.com

---

## About Me

I am Julius Pleunes.
GitHub: juliuspleunes4
This repo: https://github.com/juliuspleunes4/RenderSchema.git
Email: jjgpleunes@gmail.com

---

## Remember

🚫 **NEVER create new `.md` files to explain changes**  
✅ **ALWAYS document everything in `docs/CHANGELOG.md`**  
🎯 **Focus on making diagram generation effortless and beautiful**  
🧪 **Test thoroughly — developers will rely on accurate diagrams**  
📦 **Think open-source — write for the community**

> MAKE SURE THAT ALL EXPORTS ARE CLEAN IN THE PRODUCTION.
>
> Example of clean looking export: `from renderschema import diagram`
> Example of non-clean looking export: `from renderschema import renderschema; renderschema.diagram(...)`
