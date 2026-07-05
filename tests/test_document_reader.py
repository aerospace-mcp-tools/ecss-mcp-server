"""Unit tests for the document_reader module in ecss_mcp_server."""

# Import Python libraries
import logging

# Import third-party libraries
import pytest

# Import local modules
import ecss_mcp_server.document_reader
from ecss_mcp_server.document_reader import MAX_LINE_LENGTH, WordDocument, wrap_paragraph

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

def test_wrap_paragraph_short_text_unchanged():
    """Test that short text below MAX_LINE_LENGTH is returned unchanged."""
    short_text = "The system shall comply with this requirement."
    assert wrap_paragraph(short_text) == short_text

def test_wrap_paragraph_long_text_split_below_max():
    """Test that text longer than MAX_LINE_LENGTH is wrapped into shorter lines."""
    # Build a paragraph longer than MAX_LINE_LENGTH using repeated words
    long_text = ("The system shall verify the requirement. " * 60).rstrip()
    assert len(long_text) > MAX_LINE_LENGTH
    wrapped = wrap_paragraph(long_text)
    for line in wrapped.splitlines():
        assert len(line) <= MAX_LINE_LENGTH, f"Line exceeds MAX_LINE_LENGTH: {len(line)} chars"

def test_wrap_paragraph_preserves_content():
    """Test that wrapping preserves all words in the text."""
    long_text = ("Word " * 500).rstrip()
    wrapped = wrap_paragraph(long_text)
    # Collapsed whitespace in wrapped output should equal the original collapsed whitespace
    assert " ".join(wrapped.split()) == " ".join(long_text.split())

def test_wrap_paragraph_vscode_limit():
    """Test that wrapped lines are within VSCode's 2000-character MCP output limit."""
    # Simulate a long ECSS requirement paragraph
    requirement_text = (
        "The launch vehicle structural subsystem shall demonstrate compliance with all specified "
        "load cases including but not limited to quasi-static, dynamic, acoustic, shock, thermal, "
        "and pressure load cases as defined in the applicable load specification document. " * 10
    ).rstrip()
    assert len(requirement_text) > 2000
    wrapped = wrap_paragraph(requirement_text)
    for line in wrapped.splitlines():
        assert len(line) < 2000, f"Line would be truncated by VSCode: {len(line)} chars"  # noqa: PLR2004
