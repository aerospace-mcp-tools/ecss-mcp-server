# Python script for simplifying document filenames and converting doc to docx

# Import Python libraries
import os
import re
import glob

# Import third-party libraries 
from spire.doc import Document
from spire.doc import FileFormat

# Convert from .doc to .docx format
def convert_doc_to_docx(doc_file, docx_file):
    """
    Convert a .doc file to .docx format using Spire.Doc library.
    Args:
        doc_file (str): The file path of the .doc file to convert.
        docx_file (str): The file path to save the converted .docx file.
    """
    
    # Open the .doc file
    document = Document()
    document.LoadFromFile(doc_file)

    # Save the .doc file to a .docx file
    document.SaveToFile(docx_file, FileFormat.Docx2016)
    document.Close()
    
def convert_all_doc_to_docx(doc_folder):
    """
    Convert all .doc files in a folder to .docx format.
    Args:
        doc_folder (str): The folder path containing the .doc files to convert.
    """
    for doc_file in glob.glob(os.path.join(doc_folder, "*.doc")):
        docx_file = os.path.splitext(doc_file)[0] + ".docx"
        convert_doc_to_docx(doc_file, docx_file)
        print(f"Converted {doc_file} to {docx_file}")
        
def simplify_filenames(doc_folder):
    """
    Simplify filenames in a folder by reducing them to just the ECSS document ID.
    Removes date stamps, revision indicators, and corrigendum references.
    Annex suffixes (e.g. _Annex A) are preserved to keep filenames unique.
    Args:
        doc_folder (str): The folder path containing the files to simplify.
    """
    for filepath in glob.glob(os.path.join(doc_folder, "*.docx")):
        filename = os.path.basename(filepath)
        stem, ext = os.path.splitext(filename)
        simplified = ""

        # Use regex to extract the ECSS document ID (e.g. ECSS-Q-ST-70-01C)
        match = None
        match = re.search(r'ECSS-[A-Z]-[A-Z]{2}-\d{2}-\d{2}[A-Z]?', stem)
        if not match:
            match = re.search(r'ECSS-[A-Z]-[A-Z]{2}-\d{2}[A-Z]?', stem)
        if not match:
            print(f"Could not extract ECSS document ID from filename: {filename}")
            continue
        simplified += match.group(0)
        
        # Use regex to extract any annex suffix (e.g. _Annex A)
        match = None
        match = re.search(r'(_Annex [A-Z])', stem)
        simplified += match.group(0) if match else ""

        new_filename = simplified + ext
        new_filepath = os.path.join(doc_folder, new_filename)

        if filename != new_filename:
            os.rename(filepath, new_filepath)
            print(f"Renamed: {filename} -> {new_filename}")

    
def main(): 
    doc_folder = "/app/documents"
    convert_all_doc_to_docx(doc_folder)
    simplify_filenames(doc_folder)
    
if __name__ == "__main__":
    main()