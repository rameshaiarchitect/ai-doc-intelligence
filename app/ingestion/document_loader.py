from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from typing import List
import os


def load_pdfs_from_folder(folder_path: str) -> List[Document]:
    documents = []

    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            file_path = os.path.join(folder_path, file)
            loader = PyPDFLoader(file_path)
            docs = loader.load()

            for doc in docs:
                doc.page_content = clean_text(doc.page_content)

            documents.extend(docs)

    return documents

def clean_text(text: str) -> str:
    lines = text.split("\n")

    cleaned_lines = []
    for line in lines:
        line = line.strip()

        # remove empty / very short lines
        if len(line) < 30:
            continue

        # remove noise
        if "copyright" in line.lower():
            continue
        if "aws whitepaper" in line.lower():
            continue

        cleaned_lines.append(line)

    return "\n".join(cleaned_lines)