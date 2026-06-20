import os

from rag.pdf_loader import load_and_split_pdf
from rag.vector_store import create_vector_store


all_chunks = []

documents_path = "documents"

for file in os.listdir(documents_path):

    if file.endswith(".pdf"):

        file_path = os.path.join(
            documents_path,
            file
        )

        print(f"Ingesting: {file}")

        chunks = load_and_split_pdf(
            file_path
        )

        all_chunks.extend(chunks)


vector_db = create_vector_store(all_chunks)

print("All PDFs successfully ingested into ChromaDB")