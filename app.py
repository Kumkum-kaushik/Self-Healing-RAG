import streamlit as st
from ingestion import load_pdf, chunk_text
from embedder import get_embeddings, get_query_embedding
from retriever import store_chunks, retrieve
from generator import generate_answer
from healer import heal

st.title("🕉️ Self-Healing RAG Pipeline")
st.subheader("Ask anything from your PDF!")

if "ready" not in st.session_state:
    st.session_state.ready = False

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file and not st.session_state.ready:
    with st.spinner("Reading and processing PDF..."):
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.getvalue())
        
        text = load_pdf("temp.pdf")
        chunks = chunk_text(text)
        embeddings = get_embeddings(chunks)
        store_chunks(chunks, embeddings)
        
        st.session_state.chunks = chunks
        st.session_state.ready = True
    
    st.success(f"✅ PDF processed! {len(chunks)} chunks ready.")

if st.session_state.ready:
    query = st.text_input("Ask your question:")
    
    if query:
        with st.spinner("Finding answer..."):
            query_embedding = get_query_embedding(query)
            retrieved_chunks = retrieve(query_embedding)
            answer = heal(query, retrieved_chunks, query_embedding, retrieve, generate_answer)
        
        st.markdown("### Answer:")
        st.write(answer)
