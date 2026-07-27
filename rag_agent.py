import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

from config import (
    GOOGLE_API_KEY,
    EMBEDDINGS_PATH
)


@st.cache_resource
def load_agent():

    print("Cargando agente RAG...")

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=GOOGLE_API_KEY
    )

    vectorstore = FAISS.load_local(
        EMBEDDINGS_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": 4
        }
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=GOOGLE_API_KEY,
        temperature=0.1,
        max_output_tokens=350
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
- Responde de forma breve y profesional.
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
        "answer": response.content,
        "sources": sources
    }