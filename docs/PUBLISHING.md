# Publishing to PyPI

## Prerequisites

1. **Create PyPI account**: https://pypi.org/account/register/
2. **Create TestPyPI account** (for testing): https://test.pypi.org/account/register/
3. **Generate API tokens** for both PyPI and TestPyPI

## Setup API Token

Store your PyPI token in `~/.pypirc`:

```ini
[pypi]
username = __token__
password = pypi-YOUR-API-TOKEN-HERE

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YOUR-TEST-API-TOKEN-HERE
```

## Pre-Publication Checklist

- [ ] All tests pass: `pytest`
- [ ] Code is properly formatted: `black .`
- [ ] Linting passes: `ruff check .`
- [ ] Type checking passes: `mypy renderschema/`
- [ ] Version number updated in `pyproject.toml`
- [ ] CHANGELOG.md updated with version and release date
- [ ] README.md is up to date
- [ ] All examples work correctly
- [ ] Git tag created: `git tag v0.1.0`

## Build the Package

```bash
# Clean previous builds
rm -rf dist/ build/ *.egg-info

# Build source distribution and wheel
python -m build
```

## Test on TestPyPI (Optional but Recommended)

```bash
# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Test installation from TestPyPI
pip install --index-url https://test.pypi.org/simple/ --no-deps renderschema
```

## Publish to PyPI

```bash
# Upload to PyPI
twine upload dist/*

# Verify installation
pip install renderschema
```

## Post-Publication

1. Push git tag: `git push origin v0.1.0`
2. Create GitHub release with changelog
3. Announce on social media / relevant communities
4. Update documentation links if needed

## Updating the Package

When releasing a new version:

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md` with new version section
3. Commit changes: `git commit -m "chore: bump version to X.Y.Z"`
4. Create tag: `git tag vX.Y.Z`
5. Build and upload: `python -m build && twine upload dist/*`
6. Push changes and tag: `git push && git push --tags`

## Versioning Guidelines

Follow [Semantic Versioning](https://semver.org/):

- **MAJOR** (1.0.0): Incompatible API changes
- **MINOR** (0.1.0): Add functionality in a backward compatible manner
- **PATCH** (0.0.1): Backward compatible bug fixes

## Troubleshooting

### Package name already taken
- Check if name is available on PyPI
- Consider alternative names with prefixes/suffixes

### Upload fails
- Ensure version number is unique (not previously uploaded)
- Check API token is valid and has correct permissions
- Verify build artifacts are in `dist/` directory

### Installation issues
- Check package dependencies are correct
- Test in a fresh virtual environment
- Verify README renders correctly on PyPI
