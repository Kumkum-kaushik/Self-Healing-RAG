from ingestion import load_pdf, chunk_text
from embedder import get_embeddings, get_query_embedding
from retriever import store_chunks, retrieve
from generator import generate_answer
from healer import heal

text = load_pdf("Krishna Philosophy.pdf")
chunks = chunk_text(text)

print(f"Total chunks: {len(chunks)}")

print("\nGenerating embeddings...")
embeddings = get_embeddings(chunks)

print("\nStoring in ChromaDB...")
store_chunks(chunks, embeddings)

query = "What is Krishna's philosophy of life?"
query_embedding = get_query_embedding(query)
retrieved_chunks = retrieve(query_embedding)

answer = heal(query, retrieved_chunks, query_embedding, retrieve, generate_answer)

print(f"\nQuestion: {query}")
print(f"\nAnswer: {answer}")