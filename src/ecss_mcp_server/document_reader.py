"""Helper functions for working with documents in the document library."""

# Import Python libraries
import logging
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import docx.document

# Import third-party libraries
import numpy as np
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph

logger = logging.getLogger(__name__)

# Define dataclasses
class Heading(Paragraph):
    """A heading paragraph item extracted from a Word document."""

    def __init__(self, p: Any, parent: Any, *, level: int, annex: bool, index: int) -> None:
        """Initialize a heading with its level, annex flag, and content index."""
        super().__init__(p, parent)
        self.level = level
        self.annex = annex
        self.index = index # The index of this heading in the document content list, used for section extraction
        self.pretty_heading = None  # Human readable heading for content searching and llm response formatting

@dataclass
class Content:
    """Full content of a Word document, preserving paragraph/table order."""

    items: list[Paragraph | Table | Heading] = field(default_factory=list)

# Normalize style
def normalize_style(style: str) -> str:
    """
    Normalize a style name in a standard way for comparison.

    Args:
        style (str): The style name to normalize.

    Returns:
        str: The normalized style name.

    """
    # 1. Unicode normalization (handles weird/hidden chars)
    style = unicodedata.normalize("NFKC", style)
    # 2. Case normalization (better than lower() for unicode)
    style = style.casefold()
    # 3. Remove control / non-printable characters
    style = "".join(ch for ch in style if unicodedata.category(ch)[0] != "C")
    # 4. Remove punctuation
    style = re.sub(r"[^\w\s]", "", style)
    # 5. Remove whitespace (spaces, tabs, newlines)
    return re.sub(r"\s+", "", style)

# Normalize heading
def normalize_heading(heading: str) -> str:
    """
    Normalize a heading string in a standard way for comparison.

    Args:
        heading (str): The heading string to normalize.

    Returns:
        str: The normalized heading string.

    """
    # 1. Unicode normalization (handles weird/hidden chars)
    heading = unicodedata.normalize("NFKC", heading)
    # 2. Remove control / non-printable characters (but keep whitespace so step 3 can collapse it)
    heading = "".join(ch for ch in heading if unicodedata.category(ch)[0] != "C" or ch.isspace())
    # 3. Remove whitespace (spaces, tabs, newlines)
    return re.sub(r"\s+", " ", heading).strip()

# Get list of document IDs from the document library
def get_doc_ids() -> list[str]:
    """
    Get a list of document IDs from the document library.

    Returns:
        list[str]: A list of all document IDs in the document library.

    """
    return [doc_file.stem for doc_file in Path("/app/documents").glob("*.docx")]

# Define classes

class WordDocument:
    """Class for loading and working with Word documents."""

    def __init__(self, doc_id: str) -> None:
        """Load a Word document from the document library using its document ID."""
        # Initialize variables
        self.doc_id = doc_id
        self.document: docx.document.Document | None = None
        self.content: Content | None = None
        self.headings: list[Heading] = []
        self.pretty_headings: str | None = None
        # Initialize dicts
        self.ANNEX_STYLES = {
            'annex1': 1,
            'annex2': 2,
            'annex3': 3
        }
        self.HEADING_STYLES = {
            'heading0': 0,
            'heading1': 1,
            'heading2': 2,
            'heading3': 3
        }
        self.load_document()
        self.parse_headings()
        self.get_pretty_headings()

    def load_document(self) -> None:
        """
        Load a document from the document library using its document ID.

        Populates self.document (raw docx Document) and self.content (Content)
        with all paragraphs and tables in document order.
        """
        # Load the document using the provided document ID
        doc_path = Path(f"/app/documents/{self.doc_id}.docx")
        if not doc_path.exists():
            msg = f"Document with ID {self.doc_id} not found in document folder."
            raise FileNotFoundError(msg)
        self.document = Document(str(doc_path))
        # Extract the content of the document
        self.content = Content()
        for item in self.document.iter_inner_content():
            if isinstance(item, (Paragraph, Table)):
                self.content.items.append(item)

    def parse_headings(self) -> None:
        """Parse document content items and classify heading paragraphs by style."""
        for index, item in enumerate(self.content.items):
            if isinstance(item, Paragraph):
                # Check to see if paragraph contains content, if not skip
                if not item.text.strip():
                    continue
                # Check to see if paragraph is a heading and assign level
                level = self.HEADING_STYLES.get(normalize_style(item.style.name))
                if level is not None:
                    heading = Heading(item._p, item._parent, level=level, annex=False, index=index)
                    self.headings.append(heading)
                    # Replace paragraph with heading for section extraction
                    self.content.items[index] = heading
                    continue
                # Check to see if paragraph is an annex heading and assign level
                level = self.ANNEX_STYLES.get(normalize_style(item.style.name))
                if level is not None:
                    heading = Heading(item._p, item._parent, level=level, annex=True, index=index)
                    self.headings.append(heading)
                    # Replace paragraph with heading for section extraction
                    self.content.items[index] = heading
                    continue

    def get_pretty_headings(self) -> None:
        """
        Get plain, newline-delineated, pretty-formatted headings.

        For content searching and returning to the client.
        """
        section_number = np.zeros(6, dtype=int)
        annex_number = np.zeros(6, dtype=int)
        self.pretty_headings = ""
        # For each heading, derive the section number and create a pretty string with section number and text
        for heading in self.headings:
            if heading.annex:
                # Format annex headings using letters
                annex_number[heading.level] += 1
                annex_number[heading.level + 1:] = 0
                if heading.level == 1:
                    heading.pretty_heading = f"Annex {chr(64 + annex_number[1])} {normalize_heading(heading.text)}"
                else:
                    suffix = ".".join(str(num) for num in annex_number[2 : heading.level + 1] if num > 0)
                    heading.pretty_heading = f"{chr(64 + annex_number[1])}.{suffix} {normalize_heading(heading.text)}"
            else:
                # Format regular headings using numbers
                section_number[heading.level] += 1
                section_number[heading.level + 1:] = 0
                if heading.level == 0:
                    heading.pretty_heading = f"{normalize_heading(heading.text)}"
                else:
                    nums = ".".join(str(num) for num in section_number[1 : heading.level + 1] if num > 0)
                    heading.pretty_heading = f"{nums} {normalize_heading(heading.text)}"
            self.pretty_headings += heading.pretty_heading + "\n"

    def get_section(self, pretty_heading: str) -> str:
        """Get the text of a section of the document based on its pretty heading."""
        # Find the start and end index of the section in the document content based on the pretty heading
        start_index = None # Initialize start index to None to check if heading is found
        end_index = len(self.content.items) # Default to end of document if no next heading is found
        for heading in self.headings:
            # If this heading matches the pretty heading, set the start index to this heading's index
            if heading.pretty_heading == pretty_heading:
                matched_heading = heading
                start_index = heading.index
                continue
            # Find the start of the next section
            if start_index is not None and heading.level <= matched_heading.level:
                end_index = heading.index
                break
        if start_index is None:
            msg = "Section not found in document headings"
            raise ValueError(msg)
        # Extract the section text based on the start and end index
        section_text = ""
        for item in self.content.items[start_index:end_index]:
            if isinstance(item, Heading):
                section_text += item.pretty_heading + "\n"
            elif isinstance(item, Paragraph):
                section_text += item.text + "\n"
            # TODO: Handle tables
        return section_text
