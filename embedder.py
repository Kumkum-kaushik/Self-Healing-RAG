from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
def get_embeddings(chunks):
    embeddings = model.encode(chunks, show_progress_bar=True)
    return embeddings
def get_query_embedding(query):
    embedding= model.encode([query])
    return embedding
