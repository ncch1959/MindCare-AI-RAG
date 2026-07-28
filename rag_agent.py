import streamlit as st

from langchain_community.llms import Ollama
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from config import (
    GOOGLE_API_KEY,
    EMBEDDINGS_PATH
)


@st.cache_resource
def load_agent():

    print("Cargando agente RAG...")

    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"

    )

    vectorstore = FAISS.load_local(
        EMBEDDINGS_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": 10
        }
    )

    llm = Ollama(
    model="llama3.1:8b",
    temperature=0.1

    )

    return llm, retriever


def ask_agent(question):

    llm, retriever = load_agent()

    documents = retriever.invoke(question)

    print("\n==============================")
    print("DOCUMENTOS RECUPERADOS")
    print("==============================")

    for i, doc in enumerate(documents):
        print(f"\n--- DOCUMENTO {i + 1} ---")
        print(doc.page_content)

    if not documents:
        return {
            "answer": "No encontré información relacionada en los documentos.",
            "sources": []
        }

    context = "\n\n".join(
        doc.page_content
        for doc in documents
    )

    prompt = f"""
Eres el asistente oficial de la empresa Black_Ary Spa.

Debes responder utilizando EXCLUSIVAMENTE la información entregada en el contexto.

REGLAS IMPORTANTES:

- Contesta únicamente la pregunta realizada.
- Responde de forma clara, profesional y suficientemente desarrollada.
- Incluye los puntos principales encontrados en los documentos.
- Organiza la respuesta en secciones o viñetas cuando la pregunta sea   amplia.
- Resume la información incluyendo todos los puntos relevantes encontrados.
- No copies capítulos completos.
- No repitas información.
- Utiliza viñetas cuando corresponda.
- Si la información no existe en el contexto, indícalo claramente.
- Nunca inventes información.

Acciones adicionales sugeridas

Estructurar respuestas en pasos o secciones: síntomas, causas, recomendaciones, recursos.

Usar lenguaje accesible: evitar tecnicismos innecesarios para que cuidadores y familiares comprendan fácilmente.

Incluir advertencias claras: recordar que las guías no sustituyen atención médica profesional.

Ofrecer recursos complementarios: señalar documentos oficiales, guías prácticas y programas comunitarios.

Mantener enfoque contextualizado: adaptar ejemplos y recomendaciones al entorno chileno o hispanohablante cuando sea posible.


==========================
CONTEXTO
==========================

{context}

==========================
PREGUNTA
==========================

{question}

==========================
RESPUESTA
==========================
"""

    try:

        response = llm.invoke(prompt)

    except Exception as e:

        error = str(e)

        if "RESOURCE_EXHAUSTED" in error or "429" in error:

            return {
                "answer": (
                    "⚠️ El servicio de Inteligencia Artificial de Gemini "
                    "no está disponible porque la cuota de la API se ha agotado.\n\n"
                    "Por favor, intenta nuevamente más tarde."
                ),
                "sources": []
            }

        return {
            "answer": (
                "⚠️ Ocurrió un error al consultar el modelo.\n\n"
                f"Detalle técnico:\n{error}"
            ),
            "sources": []
        }

    sources = []

    for doc in documents:

        source = doc.metadata.get(
            "source",
            "Documento interno"
        )

        if source not in sources:
            sources.append(source)

    return {
    "answer": response,
    "sources": sources
}
    