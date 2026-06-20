from rag.retriever import retrieve_documents


results = retrieve_documents(
    "What courses are available?"
)

for doc in results:

    print("\n====================\n")

    print(doc.page_content)