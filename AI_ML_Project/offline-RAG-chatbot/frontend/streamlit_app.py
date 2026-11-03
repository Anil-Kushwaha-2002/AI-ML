import streamlit as st
import requests


BACKEND_URL = "http://127.0.0.1:8000"


st.title("Offline PDF RAG Chatbot")


uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)


if uploaded_file is not None:

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file,
            "application/pdf"
        )
    }

    response = requests.post(
        f"{BACKEND_URL}/upload_pdf/",
        files=files
    )

    st.success(response.json()["message"])


# Replace your question section
question = st.text_input("Ask Question")


if st.button("Submit"):

    response = requests.get(
        f"{BACKEND_URL}/ask/",
        params={"query": question}
    )

    print(response.status_code)
    print(response.text)

    if response.status_code == 200:

        data = response.json()

        if "answer" in data:

            st.write("Answer:")
            st.write(data["answer"])

        else:

            st.error("Backend Error")
            st.write(data)

    else:

        st.error("Server Error")
        st.write(response.text)