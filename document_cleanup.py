"""Build-time script: converts .doc to .docx and simplifies filenames to ECSS IDs."""

# Import Python libraries
import logging
import re
from pathlib import Path

# Import third-party libraries
from spire.doc import Document, FileFormat

logger = logging.getLogger(__name__)


# Convert from .doc to .docx format
def convert_doc_to_docx(doc_file: Path, docx_file: Path) -> None:
    """
    Convert a .doc file to .docx format using Spire.Doc library.

    Args:
        doc_file (Path): The file path of the .doc file to convert.
        docx_file (Path): The file path to save the converted .docx file.

    """
    # Open the .doc file
    document = Document()
    document.LoadFromFile(str(doc_file))

    # Save the .doc file to a .docx file
    document.SaveToFile(str(docx_file), FileFormat.Docx2016)
    document.Close()

def convert_all_doc_to_docx(doc_folder: Path) -> None:
    """
    Convert all .doc files in a folder to .docx format.

    Args:
        doc_folder (Path): The folder path containing the .doc files to convert.

    """
    for doc_file in doc_folder.glob("*.doc"):
        docx_file = doc_file.with_suffix(".docx")
        convert_doc_to_docx(doc_file, docx_file)
        logger.info("Converted %s to %s", doc_file, docx_file)

def simplify_filenames(doc_folder: Path) -> None:
    """
    Simplify filenames in a folder by reducing them to just the ECSS document ID.

    Removes date stamps, revision indicators, and corrigendum references.
    Annex suffixes (e.g. _Annex A) are preserved to keep filenames unique.

    Args:
        doc_folder (Path): The folder path containing the files to simplify.

    """
    for filepath in doc_folder.glob("*.docx"):
        stem = filepath.stem
        ext = filepath.suffix
        simplified = ""

        # Use regex to extract the ECSS document ID (e.g. ECSS-Q-ST-70-01C)
        match = re.search(r'ECSS-[A-Z]-[A-Z]{2}-\d{2}-\d{2}[A-Z]?', stem)
        if not match:
            match = re.search(r'ECSS-[A-Z]-[A-Z]{2}-\d{2}[A-Z]?', stem)
        if not match:
            logger.warning("Could not extract ECSS document ID from filename: %s", filepath.name)
            continue
        simplified += match.group(0)

        # Use regex to extract any annex suffix (e.g. _Annex A)
        annex_match = re.search(r'(_Annex [A-Z])', stem)
        simplified += annex_match.group(0) if annex_match else ""

        new_filename = simplified + ext
        new_filepath = doc_folder / new_filename

        if filepath.name != new_filename:
            filepath.rename(new_filepath)
            logger.info("Renamed: %s -> %s", filepath.name, new_filename)


def main() -> None:
    """Run the document cleanup pipeline."""
    doc_folder = Path("/app/documents")
    convert_all_doc_to_docx(doc_folder)
    simplify_filenames(doc_folder)

if __name__ == "__main__":
    main()
