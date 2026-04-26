"""Helper functions for working with documents in the document library."""

# Import Python libraries
import logging
import re
import unicodedata
from pathlib import Path

# Import third-party libraries
import docx.document
from docx import Document

logger = logging.getLogger(__name__)

# Define classes

class TOCEntry:
    """Class for Table of Contents (TOC) entries."""

    def __init__(
        self,
        section_number: str | None = None,
        heading_text: str | None = None,
        page_number: int | None = None,
        style: str | None = None,
        paragraph_index: int | None = None,
    ) -> None:
        """Initialize an empty TOC entry."""
        self.section_number = section_number  # Section number
        self.heading_text = heading_text  # Heading text
        self.page_number = page_number  # Page number
        self.style = style  # Paragraph style
        self.paragraph_index = paragraph_index  # Paragraph index

class Fot:
    """Class for List of Figures or Tables entries."""

    def __init__(
        self,
        element: str | None = None,
        number: str | None = None,
        text: str | None = None,
        page: str | None = None,
        paragraph_i: int | None = None,
    ) -> None:
        """Initialize a List of Figures or Tables entry."""
        self.element = element
        self.number = number
        self.text = text
        self.page = page
        self.paragraph_i = paragraph_i

# Normalize text
def normalize_string(text: str) -> str:
    """
    Normalize a string in a standard way for comparison.

    Args:
        text (str): The string to normalize.

    Returns:
        str: The normalized string.

    """
    # 1. Unicode normalization (handles weird/hidden chars)
    text = unicodedata.normalize("NFKC", text)
    # 2. Case normalization (better than lower() for unicode)
    text = text.casefold()
    # 3. Remove control / non-printable characters
    text = "".join(ch for ch in text if unicodedata.category(ch)[0] != "C")
    # 4. Remove punctuation
    text = re.sub(r"[^\w\s]", "", text)
    # 5. Normalize whitespace (spaces, tabs, newlines → single space)
    return re.sub(r"\s+", " ", text).strip()

# Get list of document IDs from the document library
def get_doc_ids() -> list[str]:
    """
    Get a list of document IDs from the document library.

    Returns:
        list[str]: A list of all document IDs in the document library.

    """
    return [doc_file.stem for doc_file in Path("/app/documents").glob("*.docx")]

# Load document from document library using document ID
def load_document(doc_id: str) -> docx.document.Document:
    """
    Load a document from the document library using its document ID.

    Args:
        doc_id (str): The document ID of the document to load.

    Returns:
        docx.document.Document: The loaded document object.

    """
    doc_path = Path(f"/app/documents/{doc_id}.docx")
    if not doc_path.exists():
        msg = f"Document with ID {doc_id} not found in document folder."
        raise FileNotFoundError(msg)
    return Document(str(doc_path))

# Parse a line of the document Table of Contents and extract the section number, heading text and page number
def parse_toc_line(toc_line: str, style: str | None = None) -> TOCEntry:
    """
    Parse a TOC line and return a TOCEntry with section number, heading text and page number.

    Throws an error if the line does not match expected formats.

    Args:
        toc_line (str): A line of text from the Table of Contents to parse.
        style (str | None): The paragraph style of the TOC line.

    Returns:
        TOCEntry: A Table of Contents entry.

    """
    # Define regex patterns for expected types of TOC entries
    pattern_annex    = r'^(Annex\s+[A-Z]+)\s+(.+)\t(\d+)$'
    pattern_numeric  = r'^([A-Z](?:\.\d+)+|\d+(?:\.\d+)*)[\t ](.+)\t(\d+)$'
    pattern_no_page  = r'^([A-Z](?:\.\d+)+|\d+(?:\.\d+)*)\s{2,}(.+)$'
    pattern_none     = r'^(.+)\t(\d+)$'

    # Remove leading and trailing whitespace and convert to list of characters for parsing
    toc_line = toc_line.strip()

    # Strip any HYPERLINK field instruction prefix (older Word documents embed these literally)
    toc_line = re.sub(r'^HYPERLINK\s+\\l\s+"[^"]+"\s*', '', toc_line)

    # Check whether the TOC entry is an annex entry with a non-numeric section number (e.g. "Annex A")
    m = re.match(pattern_annex, toc_line)
    if m:
        return TOCEntry(
            section_number=m.group(1).strip(),
            heading_text=m.group(2).strip(),
            page_number=int(m.group(3).strip()),
            style=style
        )
    # Check whether the TOC entry has a numeric section number
    m = re.match(pattern_numeric, toc_line)
    if m:
        return TOCEntry(
            section_number=m.group(1).strip(),
            heading_text=m.group(2).strip(),
            page_number=int(m.group(3).strip()),
            style=style
        )
    # Check for TOC entries with no section number (e.g. "Bibliography")
    m = re.match(pattern_none, toc_line)
    if m:
        return TOCEntry(
            section_number=None,
            heading_text=m.group(1).strip(),
            page_number=int(m.group(2).strip()),
            style=style
        )
    # Check whether the TOC entry has a section number with spaces as separator and no page number
    m = re.match(pattern_no_page, toc_line)
    if m:
        return TOCEntry(
            section_number=m.group(1).strip(),
            heading_text=m.group(2).strip(),
            page_number=None,
            style=style
        )
    # Throw an error if the TOC entry does not match any expected patterns
    msg = f"TOC entry '{toc_line}' does not match expected formats."
    raise ValueError(msg)

# Extract the Table of Contents from the document
def extract_toc(document: docx.document.Document) -> list[TOCEntry]:
    """
    Extract the Table of Contents from a document.

    Args:
        document (docx.document.Document): The document object to extract the ToC from.

    Returns:
        list[TOCEntry]: A list of table of contents entries, each containing the section number,
            heading text, page number and paragraph index.

    """
    # Find and parse lines of the document table of contents
    toc_styles = {'toc 1', 'toc 2', 'toc 3'}
    toc_paragraphs = [p for p in document.paragraphs if p.style.name.lower() in toc_styles]
    tocs = []
    for p in toc_paragraphs:
        try:
            toc_entry = parse_toc_line(p.text, style=p.style.name)
        except ValueError:
            logger.warning("Skipping unparseable TOC line (style '%s'): %r", p.style.name, p.text.strip())
            continue
        tocs.append(toc_entry)

    # Find the corresponding paragraph index for each TOC entry by matching the heading text to the document body
    heading_styles = {'heading 0', 'heading 1', 'heading 2', 'heading 3', 'heading 4', 'heading 5',
                      'annex1', 'annex2', 'annex3'}
    for i, p in enumerate(document.paragraphs):
        if p.style.name.lower() in heading_styles:
            heading_text = normalize_string(p.text)
            # Match the heading text with the next unmatched TOC entry
            for toc in tocs:
                if normalize_string(toc.heading_text) == heading_text and toc.paragraph_index is None:
                    toc.paragraph_index = i
                    break
    return tocs

# Extract the List of Figures or Tables from the document
def extract_fots(document: docx.document.Document) -> list[Fot]:
    """
    Extract the List of Figures or Tables from a document.

    Args:
        document (docx.document.Document): The document object to extract the List of Figures or Tables from.

    Returns:
        list[Fot]: A list of figures or tables, each containing the type (figure or table), number, text, and
        page number.

    """
    # List of figures and tables
    list_styles = {'table of figures'}
    list_paragraphs = [p for p in document.paragraphs if p.style.name.lower() in list_styles]

    fots = []

    for p in list_paragraphs:
        list_line = list(p.text.strip())
        element = ''
        number = []
        page = []
        # Determine if it's a figure or table
        if p.text.strip().startswith('Figure'):
            element = 'Figure'
            text = list_line[6:]  # Remove 'Figure' from text
        elif p.text.strip().startswith('Table'):
            element = 'Table'
            text = list_line[5:]  # Remove 'Table' from text
        else:
            continue  # Skip if it doesn't start with Figure or Table

        # Extract figure number from the start
        # Strip leading spaces
        text = ''.join(text).strip()
        text = list(text)
        for i, char in enumerate(text):
            if char != ' ':
                number.append(char)
            else:
                text = text[i:]
                break

        # Extract page number from the end
        for i, char in enumerate(reversed(text)):
            if char.isdigit():
                page.append(char)
            else:
                if i > 0:
                    text = text[:-i]  # Remove page number from text
                page.reverse()
                break
        page = ''.join(page).strip()
        text = ''.join(text).strip()
        number = ''.join(number).strip()
        fot_entry = Fot(element, number, text, page)
        fots.append(fot_entry)
    return fots

def extract_section(document: docx.document.Document, section_number: str, heading_text: str) -> str:
    """
    Extract the text of a specific section from a document.

    Args:
        document (docx.document.Document): The document object to extract the section from.
        section_number (str): The section number to extract as taken from table of contents (i.e. 1.2)
        heading_text (str): The heading text of the section to extract as taken from the
            table of contents (e.g. "Thermal Analysis").

    Returns:
        str: The text of the specified section.

    """
    toc = extract_toc(document)
    # Match the ToC entry to the section number and heading
    matched_toc_entry = next(
        (toc_entry for toc_entry in toc
         if toc_entry.section_number == section_number and toc_entry.heading_text == heading_text),
        None,
    )
    if matched_toc_entry is None:
        msg = "Section not found in table of contents"
        raise ValueError(msg)
    if matched_toc_entry.paragraph_index is None:
        msg = "Section could not be located in the document body"
        raise ValueError(msg)
    # Find next ToC entry at the same level as this, if not default to end of document
    next_toc_entry = toc[-1]
    for toc_entry in toc:
        if (
            toc_entry.style == matched_toc_entry.style
            and toc_entry.paragraph_index is not None
            and toc_entry.paragraph_index > matched_toc_entry.paragraph_index
        ):
            next_toc_entry = toc_entry
            break
    # Iterate between paragraphs from the matched ToC entry to the next ToC entry at the same level and extract text
    section_text = ""
    for p in document.paragraphs[matched_toc_entry.paragraph_index : next_toc_entry.paragraph_index]:
        section_text += p.text + "\n"
    return section_text
