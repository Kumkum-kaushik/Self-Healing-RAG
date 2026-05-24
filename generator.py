import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
def generate_answer(query, chunks):
    context = "\n\n".join(chunks)

    promt=f""" You are a helpful assistant. Answer the question below based on the context below:
    Context: {context}
    Question: {query}
    Answer:"""
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user", "content": promt}]
    )
    return response.choices[0].message.content