# Security Policy

## Supported Versions

As a small, single-developer project, only the latest release on the `main` branch is actively supported.

| Version | Supported          |
| ------- | ------------------ |
| main    | :white_check_mark: |
| older   | :x:                |

## Reporting a Vulnerability

**For security issues, please do NOT open a public GitHub issue.**

Instead:
1. Open a [Security Advisory](https://github.com/aerospace-mcp-tools/ecss-mcp-server/security/advisories/new) on GitHub, or
2. Contact the maintainer through GitHub's private messaging

**What to include:**
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Any suggested fixes (optional)

**Response timeline:**
- Initial response: Within 1 week
- Fix timeline: Depends on severity and complexity

## Security Considerations

### Zscaler setup

This container is configured to work with Zscaler. This is done by installing your organizations root certificate into the root directory of this project and configuring it when the Docker image is built. For more information please see [Using Docker with Zscaler](https://docs.docker.com/guides/zscaler/).

### Docker Security

- Container runs with default (non-root) user
- No privileged access required
- Only stdio transport used (no network ports exposed)
- `--rm` flag recommended for auto-cleanup after runs

### Data Privacy

- **No user data collected**: All processing is local
- **No telemetry**: No analytics or tracking
- **Public data only**: ECSS system documents are publically available
- **No credentials**: No authentication or secrets required

### Dependencies

Dependencies are managed via `uv` and pinned in `uv.lock`:
- `fastmcp`: MCP server framework
- `pandas`: Data manipulation
- `python-docx`: Reading word documents
- `spire-doc`: Converting between doc and docx file types

## Security Updates

Security patches will be applied to the `main` branch as needed. Watch the repository or enable notifications for security advisories.

---

*Last updated: April 01, 2026*
