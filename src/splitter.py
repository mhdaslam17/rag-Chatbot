from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,   # smaller = better accuracy
        chunk_overlap=50
    )   
    return splitter.split_documents(documents)