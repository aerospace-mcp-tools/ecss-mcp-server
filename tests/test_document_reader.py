"""Unit tests for the document_reader module in ecss_mcp_server."""

# Import third-party libraries
import docx.document
import pytest

# Import local modules
import ecss_mcp_server.document_reader


def test_get_doc_ids():
    """Test the get_doc_ids function to ensure it returns a list of strings."""
    doc_ids = ecss_mcp_server.document_reader.get_doc_ids()
    # Assert that the returned value is a list
    assert isinstance(doc_ids, list)
    # Assert that all items in the list are strings
    assert all(isinstance(doc_id, str) for doc_id in doc_ids)

def test_load_document():
    """Test the load_document function to ensure it loads all documents in the document library correctly."""
    # Get the list of document IDs to test loading documents
    doc_ids = ecss_mcp_server.document_reader.get_doc_ids()
    # If there are no documents available, skip the test
    if not doc_ids:
        pytest.skip("No documents available to test load_document")
    for doc_id in doc_ids:
        doc = ecss_mcp_server.document_reader.load_document(doc_id)
        # Assert that the returned object is an instance of docx.document.Document
        assert isinstance(doc, docx.document.Document), (
            f"load_document('{doc_id}') did not return a docx.document.Document instance"
        )
        assert isinstance(doc.paragraphs, list), (
            f"Document '{doc_id}' has no accessible paragraphs attribute"
        )
        assert any(p.text.strip() for p in doc.paragraphs) or len(doc.tables) > 0, (
            f"Document '{doc_id}' appears to be empty, no text or tables found"
        )
