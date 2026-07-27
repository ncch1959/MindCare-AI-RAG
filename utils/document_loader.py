from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader
)

from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_documents(folder_path):

    documents = []

    folder = Path(folder_path)

    print("\n====================================")
    print("Cargando documentos")
    print("====================================")

    for file in folder.iterdir():

        try:

            if file.suffix.lower() == ".pdf":

                loader = PyPDFLoader(
                    str(file)
                )

            elif file.suffix.lower() == ".docx":

                loader = Docx2txtLoader(
                    str(file)
                )

            elif file.suffix.lower() in [
                ".txt",
                ".md"
            ]:

                loader = TextLoader(
                    str(file),
                    encoding="utf-8"
                )

            else:

                continue


            docs = loader.load()


            for doc in docs:

                doc.metadata["source"] = file.name


            documents.extend(docs)


            print(
                f"✔ Cargado: {file.name}"
            )


        except Exception as e:

            print(
                f"❌ Error cargando {file.name}: {e}"
            )


    print(
        f"\nTotal documentos cargados: {len(documents)}"
    )

    return documents



def split_documents(documents):


    print("\n====================================")
    print("Dividiendo documentos en fragmentos")
    print("====================================")


    splitter = RecursiveCharacterTextSplitter(

        chunk_size=1500,

        chunk_overlap=300,

        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )


    chunks = splitter.split_documents(
        documents
    )


    print(
        f"Fragmentos creados: {len(chunks)}"
    )


    return chunks