import os

from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import Chroma

from langchain_community.embeddings import SentenceTransformerEmbeddings

from langchain_ollama import OllamaLLM

from langchain.chains import RetrievalQA

# from langchain.chains import RetrievalQA


PDF_FOLDER = "upload_pdfs"
DB_FOLDER = "vector_db"


embedding_model = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

llm = OllamaLLM(
    model="tinyllama"
)


def create_vector_db():

    documents = []

    for file in os.listdir(PDF_FOLDER):

        if file.endswith(".pdf"):

            pdf_path = os.path.join(PDF_FOLDER, file)

            loader = PyPDFLoader(pdf_path)

            docs = loader.load()

            documents.extend(docs)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    split_docs = text_splitter.split_documents(documents)

    vector_db = Chroma.from_documents(
        documents=split_docs,
        embedding=embedding_model,
        persist_directory=DB_FOLDER
    )

    vector_db.persist()

    return "Vector DB Created Successfully"


def load_qa_chain():

    vector_db = Chroma(
        persist_directory=DB_FOLDER,
        embedding_function=embedding_model
    )

    retriever = vector_db.as_retriever(search_kwargs={"k": 3})

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )

    return qa_chain


def ask_question(question):

    qa_chain = load_qa_chain()

    response = qa_chain.invoke(question)

    return response["result"]