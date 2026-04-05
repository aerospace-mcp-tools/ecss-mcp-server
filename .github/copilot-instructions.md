# ecss-mcp-server

FastMCP-based MCP server that provides agentic access to ECSS (European Cooperation for Space Standardization) standards documents. Containerized with Docker; runs as a stdio MCP server.

## Architecture

| Path | Purpose |
|------|---------|
| `src/ecss_mcp/main.py` | FastMCP server — defines the three MCP tools (`get_doc_ids`, `get_doc_summary`, `get_section_text`) |
| `doc_processing.py` | Shared document-processing helpers (ToC extraction, section extraction) used locally and in tests |
| `document_cleanup.py` | Build-time script: converts `.doc` → `.docx`, simplifies filenames to ECSS IDs |
| `documents/` | Place `.doc`/`.docx` ECSS standards files here before building |
| `Dockerfile` | Builds image with Python 3.14, installs deps via UV, runs cleanup, starts server |
| `pyproject.toml` | UV-managed project manifest; also configures ruff, pytest, mypy, tox |

## Build & Test

```bash
# Local dev (no Docker needed)
make install        # uv sync + stamps deps
make lint           # ruff + mypy
make test           # uv run pytest (configured in pyproject.toml)
make all            # install + lint + test

# Docker build and smoke-test
docker build -t ecss-mcp-server .
docker run -it --name test ecss-mcp-server   # verify tool count in banner
docker stop test && docker rm test

# After rebuilding the image, restart VS Code to reload the MCP client
```

See [CONTRIBUTING.md](../CONTRIBUTING.md) for full dev setup details.

## Conventions

- **Adding tools**: Use the `@app.tool()` FastMCP decorator in `src/ecss_mcp/main.py`. No new files needed for new tools.
- **Document path inside container**: `/app/documents/{doc_id}.docx`
- **ECSS document ID format**: `ECSS-[A-Z]-[A-Z]{2}-\d{2}[A-Z]?` (e.g. `ECSS-E-ST-32C`) or `ECSS-[A-Z]-[A-Z]{2}-\d{2}-\d{2}[A-Z]?` for sub-numbered docs. The `document_cleanup.py` regex handles both patterns.
- **Agentic tool call order**: `get_doc_ids` → `get_doc_summary` → `get_section_text`. Always call `get_doc_summary` before `get_section_text` to obtain valid section numbers and headings.
- **Package manager**: UV (`uv sync`, `uv run`). Do not use `pip` directly.
- **Linter**: Ruff with `lint.select = ["ALL"]`; line length 120. Run `uv run ruff . --fix`.
- **Searching ECSS documents**: Use the `searching-ecss` skill (`.github/skills/searching-ecss/SKILL.md`) for structured document research workflows.

## Pitfalls

- Documents are **not committed** to the repo — they must be downloaded separately from [ecss.nl](https://ecss.nl/standards/active-standards/) and placed in `documents/` before build.
- Corporate network / Zscaler users must supply `zscaler-root-ca.crt` in the repo root before building. See [SECURITY.md](../SECURITY.md).
- `spire-doc` (`.doc` → `.docx` conversion) requires `libicu-dev`, `libfontconfig1`, and `libfreetype6` — these are installed in the Dockerfile; do not remove them.
- After rebuilding the image, **restart VS Code** to reload the MCP client.
