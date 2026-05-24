# Self-Healing RAG Pipeline

A Retrieval-Augmented Generation (RAG) pipeline that detects poor retrieval results and retries automatically before generating a response.

Built using ChromaDB, Sentence Transformers, Groq, and Streamlit.

---

## Overview

Traditional RAG systems sometimes retrieve irrelevant chunks, which leads to inaccurate or hallucinated answers from the LLM.

This project adds a simple “self-healing” mechanism to improve retrieval quality. After retrieving chunks, the system checks whether the retrieved context is actually relevant to the user query. If the retrieval quality looks poor, it retries with more chunks before generating the final response.

If relevant information still cannot be found, the system returns a fallback response instead of generating misleading answers.

---

## Pipeline Flow

```text
PDF → Text Chunks → Embeddings → ChromaDB
                                      ↓
User Query → Query Embedding → Retrieve Chunks
                                      ↓
                          Retrieval Quality Check
                           ↙                ↘
                      Relevant            Irrelevant
                         ↓                     ↓
                Generate Answer        Retry Retrieval
                                              ↓
                                      Still Irrelevant?
                                              ↓
                                      Return Fallback
```

---

## Project Structure

```text
self-healing-rag/
├── ingestion.py      # PDF loading and chunking
├── embedder.py       # Embedding generation
├── retriever.py      # ChromaDB retrieval logic
├── generator.py      # Groq LLM response generation
├── healer.py         # Retrieval validation logic
├── main.py           # CLI pipeline
└── app.py            # Streamlit interface
```

---

## Features

* PDF-based document ingestion
* Semantic search using embeddings
* ChromaDB vector storage
* Groq + LLaMA 3 integration
* Retrieval validation before generation
* Retry mechanism for weak retrievals
* Streamlit-based UI

---

## Tech Stack

* ChromaDB
* Sentence Transformers (`all-MiniLM-L6-v2`)
* Groq API
* LLaMA 3
* PyPDF
* Streamlit

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/self-healing-rag.git
cd self-healing-rag
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install chromadb sentence-transformers pypdf groq streamlit
```

---

## Add API Key

Add your Groq API key inside `generator.py`:

```python
client = Groq(api_key="your_api_key")
```

---

## Run the Project

### Terminal Version

```bash
python main.py
```

### Streamlit App

```bash
streamlit run app.py
```

---

## Self-Healing Logic

The healing mechanism is implemented in `healer.py`.

After retrieval, the pipeline checks whether the retrieved chunks contain meaningful overlap with the query. If the retrieved context appears weak or unrelated, the retriever runs again with a larger chunk count.

If the second retrieval still fails to produce relevant context, the system returns a fallback response instead of forcing an answer.

This reduces hallucinated outputs and improves reliability compared to a basic RAG pipeline.

---

## Testing

The pipeline was tested on a 435-page PDF related to Krishna philosophy.

* Total chunks generated: 3301
* Retrieval performance was stable
* Generated answers were context-aware and relevant for most queries

---

## Future Improvements

* Query rewriting for better retrieval
* Retrieval confidence scoring
* Multi-document support
* Persistent ChromaDB storage
* Hybrid search (semantic + keyword)

---
