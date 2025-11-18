# RenderSchema Roadmap

This document outlines the planned features and improvements for RenderSchema. Items are subject to change based on community feedback and priorities.

## Version 0.2.0 (Q1 2026)

### Enhanced Diagram Types
- [ ] **Sequence Diagrams**: Visualize message flows between objects
- [ ] **Entity-Relationship Diagrams**: Database schema visualization
- [ ] **Package Diagrams**: Module and package structure visualization
- [ ] **Dependency Graphs**: Import dependency visualization with circular dependency detection

### Interactive Features
- [ ] **Collapsible Nodes**: Expand/collapse classes and modules in HTML export
- [ ] **Search/Filter**: Search functionality in interactive diagrams
- [ ] **Zoom Controls**: Enhanced zoom UI in HTML exports
- [ ] **Tooltips**: Hover information for classes, methods, and attributes

### Improved Analysis
- [ ] **Type Hint Resolution**: Better handling of complex type hints (Union, Optional, Generic)
- [ ] **Decorator Analysis**: Show decorators on classes and methods
- [ ] **Property Detection**: Distinguish properties from regular methods
- [ ] **Abstract Method Indicators**: Visual markers for abstract methods/classes

## Version 0.3.0 (Q2 2026)

### Multi-Language Support
- [ ] **JavaScript/TypeScript**: Basic class diagram support
- [ ] **Java**: Class and package diagram support
- [ ] **C#**: Class and namespace visualization
- [ ] **Go**: Struct and interface diagrams

### Advanced Flowcharts
- [ ] **Complete Control Flow**: Full if/else, loops, try/except visualization
- [ ] **Call Graph Integration**: Show function call relationships in flowcharts
- [ ] **Async Flow Visualization**: Highlight async/await patterns
- [ ] **Exception Flow**: Visualize exception propagation paths

### Customization
- [ ] **Custom Themes**: User-defined color schemes and styles
- [ ] **Layout Algorithms**: Multiple layout options (hierarchical, circular, force-directed)
- [ ] **CSS Styling**: Custom CSS for SVG/HTML exports
- [ ] **Template System**: Customizable diagram templates

## Version 0.4.0 (Q3 2026)

### Documentation Integration
- [ ] **Sphinx Extension**: Native Sphinx directive for diagram generation
- [ ] **MkDocs Plugin**: Seamless MkDocs integration
- [ ] **Jupyter Support**: IPython display integration for notebooks
- [ ] **VS Code Extension**: Preview diagrams directly in VS Code

### Performance & Scalability
- [ ] **Incremental Analysis**: Only re-analyze changed files
- [ ] **Caching**: Cache analysis results for large projects
- [ ] **Parallel Processing**: Multi-threaded diagram generation
- [ ] **Memory Optimization**: Handle very large codebases efficiently

### Quality of Life
- [ ] **CLI Tool**: Command-line interface for batch processing
- [ ] **Configuration Files**: Project-level configuration (`.renderschema.yml`)
- [ ] **Filtering Options**: Include/exclude patterns for files and classes
- [ ] **Diagram Comparison**: Visual diff between two versions of code

## Version 1.0.0 (Q4 2026)

### Enterprise Features
- [ ] **Architecture Diagrams**: High-level system architecture visualization
- [ ] **Component Diagrams**: Component and connector views
- [ ] **Deployment Diagrams**: Infrastructure and deployment visualization
- [ ] **C4 Model Support**: Context, Container, Component, and Code diagrams

### Advanced Exports
- [ ] **Mermaid Format**: Export to Mermaid.js syntax
- [ ] **PlantUML Format**: Export to PlantUML syntax
- [ ] **GraphML**: Export for yEd and other graph tools
- [ ] **DOT Format**: Graphviz compatibility

### Integration & Automation
- [ ] **CI/CD Integration**: GitHub Actions workflow examples
- [ ] **Pre-commit Hooks**: Auto-generate diagrams on commit
- [ ] **Documentation Sync**: Auto-update diagrams when code changes
- [ ] **API Documentation**: REST API for diagram generation service

## Future Considerations

### Community Requests
- Custom node shapes and icons
- Stereotype support (UML stereotypes)
- Note/comment annotations on diagrams
- Diagram versioning and history
- Collaborative diagram editing

### Experimental Features
- AI-powered layout optimization
- Automatic architecture pattern detection
- Code smell visualization
- Complexity metrics overlay
- Real-time collaboration features

## Contributing to the Roadmap

Have ideas for RenderSchema? We'd love to hear them!

- 💡 **Suggest Features**: [Open an issue](https://github.com/juliuspleunes4/RenderSchema/issues/new) with the `enhancement` label
- 👍 **Vote on Features**: React to existing issues to show support
- 🛠️ **Implement Features**: Check [CONTRIBUTING.md](CONTRIBUTING.md) to get started
- 💬 **Join Discussions**: Share your thoughts in [GitHub Discussions](https://github.com/juliuspleunes4/RenderSchema/discussions)

## Priority System

Features are prioritized based on:

1. **Community Interest**: Number of upvotes and comments on issues
2. **Impact**: How many users will benefit
3. **Complexity**: Development effort required
4. **Dependencies**: Prerequisites and technical constraints
5. **Strategic Value**: Alignment with project vision

## Version History

- **v0.1.1** (Nov 2025): Bug fixes for missing exports
- **v0.1.0** (Nov 2025): Initial release with UML, flowchart, and class diagram support

---

**Note**: This roadmap is aspirational and dates are estimates. Actual releases may vary based on contributor availability and community needs.

Last updated: November 18, 2025
