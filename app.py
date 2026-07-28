import streamlit as st

from rag_agent import ask_agent


# --------------------------------------------------
# Configuración de la página
# --------------------------------------------------

st.set_page_config(
    page_title="MindCare AI RAG",
    page_icon="🧠",
    layout="wide"
)


# --------------------------------------------------
# Encabezado
# --------------------------------------------------

st.title("🧠 MindCare AI RAG")

st.markdown(
    """
    ## Asistente Inteligente de Salud Mental

    Este asistente utiliza **Inteligencia Artificial Generativa + RAG**
    para responder consultas utilizando documentos especializados
    de salud mental.

    Desarrollado por **Black_Ary SpA**
    """
)


st.divider()


# --------------------------------------------------
# Entrada de consulta
# --------------------------------------------------

question = st.text_area(
    "💬 Escribe tu consulta:",
    height=120,
    placeholder="Ejemplo: ¿Cómo afecta el envejecimiento a la salud mental?"
)


# --------------------------------------------------
# Consulta al agente
# --------------------------------------------------

if st.button("Consultar 🧠", type="primary"):

    if question.strip() == "":

        st.warning(
            "Por favor escribe una pregunta."
        )

    else:

        with st.spinner(
            "Analizando documentos y generando respuesta..."
        ):

            try:

                result = ask_agent(question)


                st.success(
                    "Respuesta generada correctamente"
                )


                st.markdown(
                    "## 📝 Respuesta"
                )

                st.write(
                    result["answer"]
                )


                if result["sources"]:

                    st.markdown(
                        "## 📚 Fuentes consultadas"
                    )

                    for source in result["sources"]:

                        st.write(
                            f"📄 {source}"
                        )


            except Exception as e:

                st.error(
                    "Ocurrió un error al consultar el agente."
                )

                st.exception(e)



# --------------------------------------------------
# Pie de página
# --------------------------------------------------

st.divider()

st.caption(
    "MindCare AI RAG · Black_Ary SpA · Google Gemini + LangChain + FAISS"
)