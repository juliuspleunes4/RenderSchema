# Security Policy

## Supported Versions

We release patches for security vulnerabilities. Currently supported versions:

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability within RenderSchema, please send an email to Julius Pleunes at **jjgpleunes@gmail.com**. All security vulnerabilities will be promptly addressed.

**Please do not report security vulnerabilities through public GitHub issues.**

### What to Include

When reporting a vulnerability, please include:

- Type of issue (e.g., buffer overflow, SQL injection, cross-site scripting, etc.)
- Full paths of source file(s) related to the manifestation of the issue
- The location of the affected source code (tag/branch/commit or direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit it

### Response Timeline

- **Initial Response**: Within 48 hours
- **Status Updates**: Every 72 hours until resolution
- **Fix Timeline**: Critical vulnerabilities will be patched within 7 days
- **Public Disclosure**: After a fix is available and users have had time to update

## Security Best Practices

When using RenderSchema:

1. **Keep Dependencies Updated**: Regularly update RenderSchema and its dependencies
2. **Validate Input**: Always validate and sanitize any user-provided input before passing to diagram generators
3. **File Permissions**: Be cautious when exporting diagrams to ensure proper file permissions
4. **Code Execution**: Be aware that analyzing code involves importing/inspecting modules - only analyze trusted code
5. **Resource Limits**: When processing large codebases, consider implementing timeouts or resource limits

## Known Security Considerations

### Code Analysis

RenderSchema analyzes Python code using `inspect` and `ast` modules. When analyzing untrusted code:

- Code is not executed during analysis (AST parsing only)
- However, importing modules for inspection may trigger module-level code execution
- Always review code before analysis if the source is untrusted

### File Output

When exporting diagrams:

- Ensure output paths are validated to prevent path traversal attacks
- Be cautious with file permissions in multi-user environments
- HTML exports contain embedded SVG - sanitize if accepting user input for diagram content

### Dependencies

RenderSchema has minimal required dependencies, but optional exporters require:

- `cairosvg`: For PNG/PDF export (depends on Cairo library)

Keep all dependencies updated to receive security patches.

## Acknowledgments

We appreciate the security research community's efforts in responsibly disclosing vulnerabilities. Contributors who report valid security issues will be acknowledged in release notes (unless they prefer to remain anonymous).
