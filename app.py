import streamlit as st
import json
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from utils.multi_agent_system import MultiAgentSystem
from utils.prompts import prompt_template
import uuid

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
imap_server = os.getenv("IMAP_SERVER")
imap_user = os.getenv("IMAP_USER")
imap_password = os.getenv("IMAP_PASSWORD")

def main():
    st.title("Invoice Processing System")
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0, api_key=api_key)
    system = MultiAgentSystem(llm, prompt_template, imap_server, imap_user, imap_password)

    st.header("Detected Email Invoices")
    if st.button("Check for New Invoices"):
        invoices = system.email_fetcher.fetch_invoices()
        if invoices and "error" not in invoices[0]:
            for subject, result, thread_id in invoices:
                st.subheader(f"Invoice: {subject}")
        else:
            st.error("Failed to fetch invoices or no new invoices found.")

    st.header("Upload Invoice File")
    uploaded_file = st.file_uploader("Choose a PDF or JSON file", type=["pdf", "json"])
    if uploaded_file is not None:
        thread_id = str(uuid.uuid4())
        if uploaded_file.type == "application/pdf":
            with open("temp.pdf", "wb") as f:
                f.write(uploaded_file.read())
            result = system.process_input("temp.pdf", thread_id)
            os.remove("temp.pdf")
        elif uploaded_file.type == "application/json":
            json_data = json.load(uploaded_file)
            result = system.process_input(json_data, thread_id)
        st.success("Processed Invoice and stored in the Shared Memory")

if __name__ == "__main__":
    main()
