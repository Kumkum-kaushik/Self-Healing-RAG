
def is_retrieval_good(query, chunks):
    query_words= set(query.lower().split())
    common_words= {"what", "is", "the", "of", "a", "an", "are", "how", "why", "who"}
    query_words= query_words - common_words
    for chunk in chunks:
        chunk_lower= chunk.lower()
        for word in query_words:
            if word in chunk_lower:
                return True
    return False

def heal(query, chunks, query_embedding, retrieve_fn, generate_fn):
    print("Checking retrieval quality...")
    if is_retrieval_good(query, chunks):
        print("Retrieval is good. Generating answer...")
        return generate_fn(query, chunks)
    print("Retrieval is poor. Attempting to heal by retrieving more relevant chunks...")
    new_chunks= retrieve_fn(query_embedding, n_results=5)

    if is_retrieval_good(query, new_chunks):
        print("Healing successful. Generating answer with new chunks...")
        return generate_fn(query, new_chunks)
    
    print("Could not find relevant chunks. Using fallback...")
    return "Sorry, I don't have enough information to answer this question."
