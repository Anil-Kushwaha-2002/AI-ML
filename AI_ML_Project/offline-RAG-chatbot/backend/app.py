import os

# from backend.rag_pipeline import create_vector_db, ask_question

from fastapi import FastAPI, UploadFile, File

from rag_pipeline import create_vector_db, ask_question


app = FastAPI()


UPLOAD_FOLDER = "upload_pdfs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():

    return {"message": "Offline RAG PDF Chatbot Running"}


@app.post("/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as f:

        content = await file.read()

        f.write(content)

    result = create_vector_db()

    return {"message": result}


@app.get("/ask/")
def ask(query: str):

    try:

        answer = ask_question(query)

        return {
            "question": query,
            "answer": answer
        }

    except Exception as e:

        return {
            "error": str(e)
        }