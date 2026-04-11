# ecss-mcp-server

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.14+](https://img.shields.io/badge/python-3.14+-blue.svg)](https://www.python.org/downloads/)
[![MCP](https://img.shields.io/badge/MCP-FastMCP-green.svg)](https://gofastmcp.com)
[![Docker](https://img.shields.io/badge/docker-required-blue.svg)](https://www.docker.com/)

European Cooperation for Space Standardization (ECSS) MCP server for easy access of ECSS documents.

## Overview

This MCP server is built with [FastMCP](https://gofastmcp.com) and containerized with Docker. It provides three tools for retrieving information from ECSS system documents.

## Features

- **Document Lookup**: Retrieve a list of all ECSS document IDs available in the document library, along with their scope and full table of contents.
- **Agentic Search**: Extract text from specific sections of any ECSS document by section number and heading, enabling LLMs to navigate and query standards content iteratively.

## Tools

### 1. `get_doc_ids`

Get a list of all document IDs available in the document library.

**Parameters:** None

**Returns:** List of document ID strings for all `.docx` files in the document library

**Example usage in Copilot Chat:**

```text
What ECSS documents are available in the ecss-mcp-server?
```

### 2. `get_doc_summary`

Get a summary of a document including its scope and table of contents.

**Integration pattern:** Call `get_doc_ids` first to find valid document IDs before using this tool.

**Parameters:**

- `doc_id` (string): The ECSS document ID (e.g. `ECSS-E-ST-32`)

**Returns:** String containing the document scope, table of contents (section numbers and headings), and list of figures and tables

**Example usage in Copilot Chat:**

```text
Give me a summary of ECSS-E-ST-32 using the ecss-mcp-server.
```

### 3. `get_section_text`

Extract the full text of a specific section from a document.

**Integration pattern:** Call `get_doc_summary` first to get the table of contents, then use section numbers and headings exactly as they appear there.

**Parameters:**

- `doc_id` (string): The ECSS document ID (e.g. `ECSS-E-ST-32`)
- `section` (string): The section number as it appears in the table of contents (e.g. `"5.5.3"`)
- `heading` (string): The section heading as it appears in the table of contents (e.g. `"Thermal Analysis"`)

**Returns:** String containing all paragraph text in the specified section

**Example usage in Copilot Chat:**

```text
Get the requirements from section 5.3 of ECSS-E-ST-32 using the ecss-mcp-server.
```

## Prerequisites

- **Docker**: Ensure Docker is installed and running on your system
- **VS Code**: Latest version with GitHub Copilot extension enabled

## Installation & Setup

### 1. Clone the repository locally

Navigate to the location you wish to store the repository and clone it:

```bash
git clone https://github.com/aerospace-mcp-tools/ecss-mcp-server.git
```

### 2. Certificate Setup (Corporate Networks Only)

If you're behind a corporate firewall using Zscaler or similar proxy:

1. Obtain your organization's root certificate
2. Copy the certificate file to the repository root
3. Rename it to `zscaler-root-ca.crt`

See [SECURITY.md](SECURITY.md) for using Docker with Zscaler

### 3. Download ECSS documents

Download the ECSS system documents to the documents folder. If looking for all the standards they can be found here: [ECSS Website](https://ecss.nl/standards/active-standards/)

Documents can be saved in either `.doc` or `.docx` format — the server will automatically convert `.doc` files to `.docx` at build time and simplify filenames to the ECSS document ID (e.g. `ECSS-E-ST-32C.docx`).

### 4. Build the Docker Image

Navigate to the repository directory and build the Docker image:

```bash
docker build -t ecss-mcp-server .
```

This command:

- Downloads Python 3.14 base image
- Installs required dependencies using UV package manager
- Configures Docker for Zscaler
- Sets up the FastMCP server environment

### 5. Verify Installation

Test that the server builds and runs correctly:

```bash
docker run -it --name test ecss-mcp-server
```

You should see the FastMCP startup banner:

Stop the test container and clean up:

```bash
docker stop test
docker rm test
```

## VS Code Integration

This MCP server works with any MCP-compatible client that supports stdio transport. Each client will have its own configuration file location and JSON structure, but all use the same Docker container and command. The example given below shows integration with Github Copilot on VS Code.

### Method 1: Using VS Code Command Palette (Recommended)

1. Open VS Code and press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS)
2. Type and select **"MCP: Add Server"**
3. Choose **"Command (stdio)"** as the transport type
4. Enter the Docker command:

   ```bash
   docker run --rm -i --network host ecss-mcp-server
   ```

5. Name the server: `ecss-mcp-server`
6. The server will be automatically added to your MCP configuration

### Method 2: Manual Configuration

Alternatively, you can manually edit your MCP configuration file:

**Location**: `%APPDATA%\Code\User\mcp.json` (Windows) or `~/.config/Code/User/mcp.json` (Linux/macOS)

Add the following configuration:

```json
{
  "servers": {
    "ecss-mcp-server": {
      "type": "stdio",
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "--network",
        "host",
        "ecss-mcp-server"
      ]
    }
  }
}
```

### Verification

1. Restart VS Code after configuration
2. Open GitHub Copilot Chat
3. Test the mcp server with an example from above!

## Data Source

- **Standards**: Standards can be downloaded from the [ECSS Website](https://ecss.nl/standards/active-standards/)

## Configuration Details

### Docker Run Parameters Explained

- `--rm`: Automatically remove container when it exits (prevents container buildup)
- `-i`: Keep STDIN open for interactive communication with MCP protocol
- `--network host`: Use host networking for seamless VS Code stdio communication
- `ecss-mcp-server`: The Docker image name built in earlier steps

## Development & Contributing

Interested in contributing to this project? Please see [CONTRIBUTING.md](CONTRIBUTING.md) for:

- Development setup instructions
- Testing procedures
- Code guidelines
- How to submit changes

### Project Structure

```text
ecss-mcp-server/
├── src/
│   └── ecss_mcp_server/
│       ├── __init__.py
│       ├── document_parser.py    # Document name formatting and file type conversion at build time
│       ├── document_reader.py    # Document reading functions
│       └── ecss_mcp_server.py    # FastMCP server entry - defines MCP tools
├── tests/
│   ├── conftest.py               # Shared test fixtures
│   ├── test_document_parser.py
│   ├── test_document_reader.py
│   └── test_ecss_mcp_server.py
├── documents/                    # Folder for ECSS .doc/.docx files (user-supplied)
├── Dockerfile                    # Multi-stage build with cert and system lib support
├── Makefile                      # Developer workflow targets (install, lint, test)
├── pyproject.toml                # Dependencies and tool configuration (UV, ruff, pytest, mypy)
├── README.md                     # This file
├── CONTRIBUTING.md               # Contribution guidelines
├── SECURITY.md                   # Security policy and considerations
├── CODE_OF_CONDUCT.md            # Community guidelines
├── LICENSE                       # Apache 2.0 License
└── .github/
    ├── copilot-instructions.md   # Copilot agent instructions
    ├── skills/                   # Custom Copilot skill definitions
    └── workflows/                # CI/CD GitHub Actions workflows
```

## Troubleshooting

### Container Issues

**Container fails to start:**

- Verify Docker is running: `docker --version`
- Check image exists: `docker images | grep ecss-mcp-server`
- Review build logs for errors during image creation
- Test manually: `docker run -it --name test ecss-mcp-server`

### VS Code Integration Issues

**VS Code doesn't detect the server:**

- Confirm `mcp.json` configuration syntax is valid JSON
- Verify file location: `%APPDATA%\Code\User\mcp.json` (Windows)
- Restart VS Code after configuration changes
- Check VS Code Developer Console (`Help > Toggle Developer Tools`) for MCP-related errors
- Ensure Docker Desktop is running before starting VS Code

**Server appears but tools don't work:**

- Rebuild the Docker image to ensure latest code
- Check that FastMCP banner shows on startup
- Test tools manually: `docker run -it --name test ecss-mcp-server`

## Technical Details

### Dependencies

- **Python**: 3.14 (slim-trixie base image)
- **FastMCP**: ≥3.1.1 (MCP protocol implementation)
- **python-docx**: ≥1.2.0 (reading `.docx` document content)
- **spire-doc**: ≥14.1.6 (converting `.doc` files to `.docx` at build time)
- **pandas**: ≥3.0.1 (data processing)

### Security Considerations

For detailed security information, including vulnerability reporting, and privacy considerations, please see [SECURITY.md](SECURITY.md).

## Support & Resources

- **FastMCP Documentation**: <https://gofastmcp.com>
- **MCP Protocol Specification**: <https://modelcontextprotocol.io>
- **Docker Documentation**: <https://docs.docker.com>

## Project Documentation

- [CONTRIBUTING.md](CONTRIBUTING.md) - How to contribute to this project
- [SECURITY.md](SECURITY.md) - Security policy and vulnerability reporting
- [LICENSE](LICENSE) - Apache 2.0 License details
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - Community guidelines

## Acknowledgments

- **Data Source**: ECSS Initiative
- **Framework**: FastMCP by the FastMCP team
- **Protocol**: Model Context Protocol (MCP) specification
