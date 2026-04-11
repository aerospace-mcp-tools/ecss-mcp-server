# Contributing to the ECSS MCP Server

Thanks for your interest in contributing! This is a small project maintained by a single developer in their free time, so contributions are welcome but please be patient with response times.

## How to Contribute

1. **Fork the repository** and create a branch for your changes
2. **Make your changes** following the patterns in the existing code
3. **Test thoroughly** test code changes after editing (see manual testing details below)
4. **Submit a pull request** with a clear description of what you've changed and why

## Development Setup

### Prerequisites

- Docker installed and running
- VS Code with the [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension
- (Optional) Corporate certificate if behind a proxy (see [SECURITY.md](SECURITY.md))

### Dev Container

The recommended way to develop is inside the dev container defined in [`.devcontainer/devcontainer.json`](.devcontainer/devcontainer.json). It builds from the same `Dockerfile` as the production image, so your environment exactly matches what runs in production.

1. Open the repo in VS Code
2. When prompted, click **Reopen in Container** — or run **Dev Containers: Reopen in Container** from the Command Palette
3. VS Code will build the image and attach to the container; this may take a few minutes on first run

Once inside the container, install dependencies and verify the environment:

```bash
make install    # uv sync + stamps deps
make all        # install + lint + test
```

### Testing

Run the full suite from inside the dev container:

```bash
make install    # first time only — installs dependencies
make lint       # ruff check --fix
make test       # uv run pytest (with coverage; output in tests/reports/)
make all        # install + lint + test in one step
```

To verify the production image after making changes:

```bash
# Run outside the dev container (on your host machine)
docker build -t ecss-mcp-server .
docker run -it --name test ecss-mcp-server  # Verify tool count in banner
docker stop test && docker rm test
# Restart VS Code to reload the MCP client
```

## Code Guidelines

- **Use FastMCP patterns**: Follow existing decorator structure for new tools

## What to Contribute

### Welcome Contributions

- Bug fixes
- Performance improvements
- Documentation improvements
- Test coverage

### Please Discuss First (Open an Issue)

- Major architectural changes
- New dependencies
- Breaking changes to existing tools
- Alternative data sources

## Questions?

Open an issue! Response times may vary, but all questions are welcome.

## License

By contributing, you agree that your contributions will be licensed under the project license.
