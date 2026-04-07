from src.loader import load_documents
from src.splitter import split_documents
from src.embeddings import get_embeddings
from src.vectorstore import create_vector_store, load_vector_store
from src.retriever import get_retriever
from src.rag_pipeline import generate_answer

# def setup_pipeline():
#     docs = load_documents("data/docs")
#     chunks = split_documents(docs)

#     embeddings = get_embeddings()
#     vectorstore = create_vector_store(chunks, embeddings)

#     retriever = get_retriever(vectorstore)
#     # qa_chain = build_rag_chain(retriever)

#     return qa_chain

def ask_question(retriever):
    while True:
        query = input("\nAsk your question (type 'exit' to quit): ")

        if query.lower() == "exit":
            break

        docs = retriever.invoke(query)

        # print("\n🔍 RETRIEVED DOCS:")
        # for d in docs:
        #     print(d.page_content[:200])

        # build context
        context = "\n\n".join(
            " ".join(doc.page_content.split()) for doc in docs
        )

        # generate answer
        answer = generate_answer(context, query)

        print("\nAnswer:\n", answer)

        print("\nSources:")
        for doc in docs:
            print("-", doc.metadata.get("source", "Unknown"))

if __name__ == "__main__":
    # qa_chain = setup_pipeline()
    retriever = get_retriever(load_vector_store(get_embeddings()))

    ask_question(retriever)