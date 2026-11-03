from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text


def get_chunks(text):
    splitter = CharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    return splitter.split_text(text)


def get_vector_store(chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(chunks, embedding=embeddings)
    return vectorstore




# from langchain.text_splitter import CharacterTextSplitter

# from langchain.embeddings import OpenAIEmbeddings

# from langchain.vectorstores import FAISS

# from PyPDF2 import PdfReader

# import os


# def load_pdf(file_path):

#     reader = PdfReader(file_path)

#     text = ''

#     for page in reader.pages:

#         text += page.extract_text()

#     return text


# def get_chunks(text):

#     splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

#     return splitter.split_text(text)


# def get_vector_store(chunks):

#     embeddings = OpenAIEmbeddings()

#     vectorstore = FAISS.from_texts(chunks, embedding=embeddings)

#     return vectorstore