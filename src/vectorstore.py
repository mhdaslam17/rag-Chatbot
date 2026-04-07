from langchain_community.vectorstores import FAISS

def create_vector_store(chunks, embeddings):
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local("faiss_index")
    return vectorstore

def load_vector_store(embeddings):
    return FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True  # needed in latest versions
    )