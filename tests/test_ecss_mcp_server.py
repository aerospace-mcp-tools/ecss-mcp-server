"""Unit tests for the ecss_mcp_server module in ecss_mcp_server."""

# Import Python libraries
import logging

# Import third-party libraries
import pytest

# Import local modules
import ecss_mcp_server.document_reader
import ecss_mcp_server.ecss_mcp_server

logger = logging.getLogger(__name__)


def test_get_doc_summary(subtests):
    """Test the get_doc_summary function for all documents in the document library."""
    doc_ids = ecss_mcp_server.document_reader.get_doc_ids()
    if not doc_ids:
        pytest.skip("No documents available to test get_doc_summary")
    for i, doc_id in enumerate(doc_ids):
        logger.info("Testing get_doc_summary on document '%s'", doc_id)
        with subtests.test(doc_id=doc_id, index=i):
            summary = ecss_mcp_server.ecss_mcp_server.get_doc_summary(doc_id)
            # Assert the summary is a non-empty string
            assert isinstance(summary, str)
            assert len(summary) > 0
            # Assert the summary contains the document ID
            assert doc_id in summary

