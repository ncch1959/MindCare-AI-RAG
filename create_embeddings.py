import os

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from config import GOOGLE_API_KEY


DOCUMENTS_PATH = "documents"
EMBEDDINGS_PATH = "embeddings"


def load_documents():

    documents = []

    for file in os.listdir(DOCUMENTS_PATH):

        if file.endswith(".pdf"):

            path = os.path.join(
                DOCUMENTS_PATH,
                file
            )

            print(f"Cargando: {file}")

            loader = PyPDFLoader(path)

            documents.extend(
                loader.load()
            )

    return documents



def create_embeddings():

    print("Cargando documentos...")

    documents = load_documents()

    print(
        f"Documentos cargados: {len(documents)} páginas"
    )


    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150
    )


    chunks = splitter.split_documents(
        documents
    )


    print(
        f"Fragmentos creados: {len(chunks)}"
    )


    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
    

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )


    os.makedirs(
        EMBEDDINGS_PATH,
        exist_ok=True
    )


    vectorstore.save_local(
        EMBEDDINGS_PATH
    )


    print(
        "✅ Embeddings creados correctamente"
    )



if __name__ == "__main__":

    create_embeddings()