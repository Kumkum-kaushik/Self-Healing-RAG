import chromadb

client= chromadb.Client()
collection= client.create_collection("krishna_philosophy")

def store_chunks(chunks, embeddings):
    ids= [str(i) for i in range(len(chunks))]
    collection.add(
        documents= chunks,
        embeddings= embeddings.tolist(),
        ids= ids
    )
    print(f"Stored {len(chunks)} chunks in ChromaDB.")

def retrieve(query_embedding, n_results=3):
    results= collection.query(
        query_embeddings= query_embedding.tolist(),
        n_results= n_results
    )
    return results['documents'][0]