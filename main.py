from app.ingestion.document_loader import load_pdfs_from_folder
from app.ingestion.text_splitter import get_text_splitter
import random
from app.embeddings.embedder import get_embedding_model
from app.retrieval.vector_store import create_vector_store
from app.llm.llm import get_llm



if __name__ == "__main__":
    docs = load_pdfs_from_folder("data/raw")
    
    splitter = get_text_splitter()
    chunks = splitter.split_documents(docs)

    print(f"Total chunks: {len(chunks)}")    

    print("\n--- RANDOM CHUNKS ---\n")

    for i in range(3):
        chunk = random.choice(chunks)
        #print(f"\nChunk {i+1}:\n")
        #print(chunk.page_content[:300])
        #print("\n-------------------")

    embedding_model = get_embedding_model()

    vector_store = create_vector_store(chunks, embedding_model)

    #print("Vector store created successfully")
    
    query = "What is AWS pricing model?"

    results = vector_store.similarity_search(query, k=5)

    print("\n--- RETRIEVED CHUNKS ---\n")

    for i, doc in enumerate(results):
        print(f"\nResult {i+1}:\n")
        print(doc.page_content[:300])
        print("\n-------------------")
        
    llm = get_llm()

    context = "\n\n".join([doc.page_content for doc in results])

    prompt = f"""
    Answer the question based only on the context below.

    Context:
    {context}

    Question:
    {query}

    Answer:
    """
    
    response = llm.invoke(prompt)

    print("\n--- FINAL ANSWER ---\n")
    print(response.content)