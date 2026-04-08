FROM python:3.14-slim-trixie

# Install ca-certificates, libicu (required by spire.doc/.NET runtime),
# and libfontconfig1/libfreetype6 (required by SkiaSharp for image rendering)
RUN apt-get update && \
 apt-get install -y ca-certificates libicu-dev libfontconfig1 libfreetype6 make

 # Copy Zscaler root certificate if it exists (for corporate networks)
COPY zscaler-root-ca.crt* /usr/local/share/ca-certificates/zscaler-root-ca.crt
# Install Zscaler cerificate if it is populated
RUN if [ -s /usr/local/share/ca-certificates/zscaler-root-ca.crt ]; then \
        update-ca-certificates && \
        echo "Zscaler certificate installed successfully"; \
    else \
        echo "No Zscaler certificate found - skipping"; \
    fi

# Set environment variables for Python/pip to use system certificates
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
ENV SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
ENV CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

# Install UV from Astral SH's prebuilt image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the project into the image
ADD . /app

# Sync the project into a new environment, asserting the lockfile is up to date
WORKDIR /app
RUN uv sync

# Run document cleanup
RUN uv run ecss-parser
# Run MCP server
CMD ["uv", "run", "ecss-mcp-server"]