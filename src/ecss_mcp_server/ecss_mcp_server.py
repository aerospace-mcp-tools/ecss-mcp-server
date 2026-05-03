"""FastMCP server exposing ECSS standards documents as MCP tools."""

# Import third-party libraries
from fastmcp import FastMCP

# Import local modules
from ecss_mcp_server import document_reader
from ecss_mcp_server.document_reader import WordDocument

app = FastMCP("ecss-mcp-server")

@app.tool()
def get_doc_ids() -> list[str]:
    """
    Get a list of ECSS doc_id in the document library.

    Returns:
        list[str]: A list of all doc_id in the document library.

    """
    return document_reader.get_doc_ids()

@app.tool()
def get_doc_summary(doc_id: str) -> str:
    """
    Get a summary of a ECSS document given its doc_id.

    Integration pattern: Only use this tool after using the get_doc_ids tool to get a list of doc_id in
    the document library, and only use it with those doc_id.

    Args:
        doc_id (str): The ECSS doc_id of the document to summarize.

    Returns:
        str: A summary of the document including document scope and table of contents.

    """
    doc = WordDocument(doc_id)
    # Get the scope if available
    try:
        scope = doc.get_section("1 Scope")
    except ValueError:
        scope = "Scope section not found."
    summary = f"Document ID: {doc_id}\n\nSummary:\n"
    summary += f"Scope:\n{scope}\n\n"
    summary += "Headings:\n"
    summary += doc.pretty_headings
    #TODO: Add table of figures and tables to summary
    return summary

@app.tool()
def get_section(doc_id: str, heading_text: str) -> str:
    """
    Get the text of a specific section from a document given its heading.

    Integration pattern: Only use this tool after using the get_doc_summary tool to get the table of contents
    for a document, and only use it with headings that are present in the table of contents for that document.

    Args:
        doc_id (str): The ECSS ID of the document to extract the section from.
        heading_text (str): The heading text of the section to extract as taken from the table of contents.

    Returns:
        str: The text of the specified section.

    """
    doc = WordDocument(doc_id)
    return doc.get_section(heading_text)

def main() -> None:
    """Entry point for the ecss-mcp-server script."""
    app.run()

if __name__ == "__main__":
    main()
