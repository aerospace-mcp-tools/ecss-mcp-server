"""FastMCP server exposing ECSS standards documents as MCP tools."""

# Import Python libraries
from pathlib import Path

# Import third-party libraries
from fastmcp import FastMCP

# Import local modules
from ecss_mcp_server.document_reader import extract_fots, extract_section, extract_toc, load_document

app = FastMCP("ecss-mcp-server")


@app.tool()
def get_doc_ids() -> list[str]:
    """
    Get a list of document IDs from the document library.

    Returns:
        list[str]: A list of all documents in the document library.

    """
    return [doc_file.stem for doc_file in Path("/app/documents").glob("*.docx")]

@app.tool()
def get_doc_summary(doc_id: str) -> str:
    """
    Get a summary of a document given its ID.

    Integration pattern: Only use this tool after using the get_doc_ids tool to get a list of document IDs in
    the document library, and only use it with those document IDs.

    Args:
        doc_id (str): The ECSS ID of the document to summarize.

    Returns:
        str: A summary of the document including document scope and table of contents.

    """
    doc = load_document(doc_id)
    tocs = extract_toc(doc)
    fots = extract_fots(doc)
    scope = extract_section(doc, "1", "Scope")
    summary = f"Document ID: {doc_id}\n\nSummary:\n"
    summary += f"Scope:\n{scope}\n\n"
    summary += "Table of Contents:\n"
    summary += "'section': 'heading'\n"
    for toc in tocs:
        summary += f"'{toc.section}': '{toc.heading}'\n"
    summary += "\nList of Figures and Tables:\n"
    summary += "'element': 'number' 'text'\n"
    for fot in fots:
        summary += f"'{fot.element}': '{fot.number}' '{fot.text}'\n"
    return summary

@app.tool()
def get_section_text(doc_id: str, section: str, heading: str) -> str:
    """
    Get the text of a specific section from a document given its section number and heading.

    Integration pattern: Only use this tool after using the get_doc_summary tool to get the table of contents
    for a document, and only use it with section numbers and headings that are present in the table of
    contents for that document.

    Args:
        doc_id (str): The ECSS ID of the document to extract the section from.
        section (str): The section number to extract as taken from table of contents (e.g. "5.5.3")
        heading (str): The heading text of the section to extract as taken from the table of contents
            (e.g. "Thermal Analysis").

    Returns:
        str: The text of the specified section.

    """
    doc = load_document(doc_id)
    return extract_section(doc, section, heading)

def main() -> None:
    """Entry point for the ecss-mcp-server script."""
    app.run()

if __name__ == "__main__":
    main()
