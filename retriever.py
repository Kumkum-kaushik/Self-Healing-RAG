import chromadb

client = chromadb.Client()

def get_collection():
    try:
        return client.get_collection("krishna_philosophy")
    except:
        return client.create_collection("krishna_philosophy")

def store_chunks(chunks, embeddings):
    collection = get_collection()
    ids = [str(i) for i in range(len(chunks))]
    collection.add(
        documents=chunks,
        embeddings=embeddings.tolist(),
        ids=ids
    )
    print(f"Stored {len(chunks)} chunks in ChromaDB")

def retrieve(query_embedding, n_results=3):
    collection = get_collection()
    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=n_results
    )
    return results['documents'][0]
