from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    UnstructuredHTMLLoader
)
import os

def load_documents(folder_path):
    documents = []

    for file in os.listdir(folder_path):
        path = os.path.join(folder_path, file)

        try:
            if file.endswith(".pdf"):
                loader = PyPDFLoader(path)
            elif file.endswith(".txt"):
                loader = TextLoader(path, encoding="utf-8")
            elif file.endswith(".html"):
                loader = UnstructuredHTMLLoader(path)
            else:
                continue

            docs = loader.load()

            # Add source metadata (VERY IMPORTANT for citations)
            for doc in docs:
                doc.metadata["source"] = file

            documents.extend(docs)

        except Exception as e:
            print(f"Error loading {file}: {e}")

    return documents