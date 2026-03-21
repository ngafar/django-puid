# Release Process

1. Bump the version in `pyproject.toml`
2. Commit and push to `main`
3. Create a GitHub Release with a version tag (e.g. `v0.2.0`)

Creating the release triggers the publish workflow, which builds and uploads the package to PyPI automatically.

## Notes

- Use [semantic versioning](https://semver.org): `MAJOR.MINOR.PATCH`
- The publish workflow uses PyPI trusted publishing — no API token required, but the PyPI project must have the GitHub repo configured as a trusted publisher
