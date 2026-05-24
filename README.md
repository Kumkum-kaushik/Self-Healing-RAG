# 🕉️ Self-Healing RAG Pipeline

A RAG (Retrieval-Augmented Generation) pipeline that can detect bad retrievals and fix itself automatically. Built with ChromaDB, Sentence Transformers, and Groq.

---

## What is this?

So basically I got tired of RAG pipelines that just... silently give wrong answers. You know the feeling — you ask something, the retrieval grabs totally irrelevant chunks, and the LLM hallucinates a confident-sounding nonsense response.

This project adds a "healing" layer on top of a standard RAG pipeline. If the retrieved chunks don't look relevant to the query, the system detects it and tries again with more results. If that also fails, it honestly tells you it doesn't know — instead of making stuff up.

---

## How it works

```
PDF → Chunks → Embeddings → ChromaDB
                                ↓
Query → Query Embedding → Retrieve Top Chunks
                                ↓
                         Healer checks quality
                         ↙              ↘
                    Good?            Bad?
                  Generate         Re-retrieve
                   Answer          with more chunks
                                        ↓
                                   Still bad?
                                   Fallback msg
```

---

## Project Structure

```
self-healing-rag/
├── ingestion.py    # Reads PDF and splits into chunks
├── embedder.py     # Converts text to embeddings
├── retriever.py    # Stores and retrieves from ChromaDB
├── generator.py    # Calls Groq LLM to generate answers
├── healer.py       # The self-healing logic
├── main.py         # Puts everything together
└── app.py          # Streamlit UI
```

---

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/yourusername/self-healing-rag.git
cd self-healing-rag
```

**2. Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

**3. Install dependencies**
```bash
pip install chromadb sentence-transformers pypdf groq streamlit
```

**4. Add your Groq API key**

Get a free API key from [console.groq.com](https://console.groq.com) and add it in `generator.py`:
```python
client = Groq(api_key="your_api_key_here")
```

---

## Run it

**Terminal version:**
```bash
python main.py
```

**Streamlit UI:**
```bash
streamlit run app.py
```

Upload any PDF and start asking questions!

---

## Tech Stack

- **ChromaDB** — vector database to store and search embeddings
- **Sentence Transformers** (`all-MiniLM-L6-v2`) — converts text to 384-dimensional embeddings
- **Groq + LLaMA 3** — fast LLM inference for generating answers
- **PyPDF** — reads and extracts text from PDFs
- **Streamlit** — UI layer

---

## The Self-Healing Part (the interesting bit)

The `healer.py` file is what makes this different from a regular RAG pipeline.

After retrieval, it checks if the retrieved chunks actually contain words from the query. If they don't, it assumes the retrieval was bad and tries again — this time fetching 6 chunks instead of 3. If even that doesn't work, it returns a fallback message instead of hallucinating.

Is it perfect? No. But it's honest, which counts for a lot.

---

## Tested On

Tested with a 435-page PDF on Krishna's philosophy. Got 3,301 chunks, retrieval worked well, answers were actually relevant. Not bad.

---

## What I'd improve next

- Better healing strategy (query rewriting instead of just fetching more chunks)
- Confidence scoring on retrieved chunks
- Support for multiple PDFs at once
- Persistent ChromaDB storage (right now it resets every run)

---

## License

MIT — do whatever you want with it.
