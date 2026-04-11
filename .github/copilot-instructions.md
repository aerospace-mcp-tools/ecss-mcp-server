# ecss-mcp-server

FastMCP-based MCP server that provides agentic access to ECSS (European Cooperation for Space Standardization) standards documents. Containerized with Docker; runs as a stdio MCP server.

## Architecture

| Path | Purpose |
|------|---------|
| `src/ecss_mcp_server/ecss_mcp_server.py` | FastMCP server entry — defines the three MCP tools (`get_doc_ids`, `get_doc_summary`, `get_section_text`) via `@app.tool()` (entry point: `ecss-mcp-server`) |
| `src/ecss_mcp_server/document_reader.py` | Core document parsing — `load_document()`, `extract_toc()`, `extract_fots()`, `extract_section()`; defines `TocEntry` and `Fot` data classes |
| `src/ecss_mcp_server/document_parser.py` | Build-time script: converts `.doc` → `.docx`, simplifies filenames to ECSS IDs (entry point: `ecss-parser`) |
| `documents/` | Place `.doc`/`.docx` ECSS standards files here before building |
| `Dockerfile` | Builds image with Python 3.14, installs deps via UV, runs cleanup, starts server |
| `pyproject.toml` | UV-managed project manifest; also configures ruff, pytest, mypy, tox |

## Build & Test

Development is to be done in a dev container environment specified by `.devcontainer/devcontainer.json` which mounts the repo and provides a consistent environment. The production image can be built locally with Docker.

```bash
# To only be done in a development container environment specified by .devcontainer/devcontainer.json; not needed for production image build
make install        # uv sync + stamps deps
make lint           # ruff (configured in pyproject.toml)
make test           # uv run pytest (configured in pyproject.toml)
make all            # install + lint + test

# Docker build and smoke-test done locally
docker build -t ecss-mcp-server .
docker run -it --name test ecss-mcp-server   # verify tool count in banner
docker stop test && docker rm test

# After rebuilding the image, restart VS Code to reload the MCP client
```

See [CONTRIBUTING.md](../CONTRIBUTING.md) for full dev setup details.

## Conventions

- **Adding tools**: Use the `@app.tool()` FastMCP decorator in `src/ecss_mcp_server/ecss_mcp_server.py`. No new files needed for new tools.
- **Document path inside container**: `/app/documents/{doc_id}.docx`
- **ECSS document ID format**: `ECSS-[A-Z]-[A-Z]{2}-\d{2}[A-Z]?` (e.g. `ECSS-E-ST-32C`) or `ECSS-[A-Z]-[A-Z]{2}-\d{2}-\d{2}[A-Z]?` for sub-numbered docs. The `src/ecss_mcp_server/document_parser.py` regex handles both patterns.
- **Agentic tool call order**: `get_doc_ids` → `get_doc_summary` → `get_section_text`. Always call `get_doc_summary` before `get_section_text` to obtain valid section numbers and headings.
- **Package manager**: UV (`uv sync`, `uv run`). Do not use `pip` directly.
- **Linter**: Ruff run via `make lint` (configured in `pyproject.toml`). Follow ruff rules for code style and quality.
- **Testing**: Pytest run via `make test` (configured in `pyproject.toml`). Write tests in `tests/` and follow existing test patterns.
- **Searching ECSS documents**: Use the `searching-ecss` skill (`.github/skills/searching-ecss/SKILL.md`) for structured document research workflows.

## Pitfalls

- Documents are **not committed** to the repo — they must be downloaded separately from [ecss.nl](https://ecss.nl/standards/active-standards/) and placed in `documents/` before build.
- Corporate network / Zscaler users must supply `zscaler-root-ca.crt` in the repo root before building. See [SECURITY.md](../SECURITY.md).
- `spire-doc` (`.doc` → `.docx` conversion) requires `libicu-dev`, `libfontconfig1`, and `libfreetype6` — these are installed in the Dockerfile; do not remove them.
- After rebuilding the image, **restart VS Code** to reload the MCP client.
