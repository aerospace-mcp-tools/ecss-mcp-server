"""Unit tests for the document_reader module in ecss_mcp_server."""

# Import Python libraries
import logging

# Import third-party libraries
import pytest

# Import local modules
import ecss_mcp_server.document_reader
from ecss_mcp_server.document_reader import WordDocument

logger = logging.getLogger(__name__)

def test_get_doc_ids():
    """Test the get_doc_ids function to ensure it returns a list of strings."""
    doc_ids = ecss_mcp_server.document_reader.get_doc_ids()
    # Assert that the returned value is a list
    assert isinstance(doc_ids, list)
    # Assert that all items in the list are strings
    assert all(isinstance(doc_id, str) for doc_id in doc_ids)

def test_word_document_initialization(subtests):
    """Test the initialization of the WordDocument class."""
    doc_ids = ecss_mcp_server.document_reader.get_doc_ids()
    if not doc_ids:
        pytest.skip("No documents found in the document library.")
    for i, doc_id in enumerate(doc_ids):
        logger.info("Testing extract_toc on document '%s'", doc_id)
        with subtests.test(doc_id=doc_id, index=i):
            doc = WordDocument(doc_id)
            assert doc.doc_id == doc_id
            assert doc.document is not None
            assert doc.content is not None
            assert len(doc.headings) != 0
            assert doc.pretty_headings is not None
