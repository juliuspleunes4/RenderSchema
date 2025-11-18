# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-11-18

### Added
- Initial project structure and package setup
- Copilot instructions for development guidelines with strict documentation rules
- Core `diagram()` function for easy diagram generation
- `BaseDiagramGenerator` abstract class for extensible diagram types
- `UMLDiagramGenerator` for generating UML class diagrams from Python classes
- `FlowchartGenerator` for creating flowcharts from Python functions
- `ClassDiagramGenerator` for visualizing class relationships and inheritance
- Export support for SVG, PNG, PDF, and HTML formats
- Interactive HTML export with zoom and pan capabilities
- Light and dark theme support with Tailwind-inspired colors
- Comprehensive test suite using pytest with fixtures
- Example scripts demonstrating UML, flowchart, and class relationship diagrams
- Quick start guide in `docs/QUICKSTART.md`
- Contributing guidelines in `CONTRIBUTING.md`
- MIT License with proper author attribution
- `pyproject.toml` with modern Python packaging configuration and author credentials
- Development tools configuration (pytest, black, ruff, mypy)
- `.gitignore` configured to exclude generated diagrams and build artifacts

### Changed
- Updated project URLs in `pyproject.toml` to point to actual GitHub repository
- Added author email to package metadata
- Created comprehensive README.md with badges, features, usage examples, and roadmap
- Fixed license format in `pyproject.toml` to use SPDX expression (removing deprecation warnings)
- Removed deprecated license classifier from package metadata

### Documentation
- Added `MANIFEST.in` for proper package distribution
- Created `docs/PUBLISHING.md` with complete PyPI publishing guide
- Package successfully builds with no warnings or errors
