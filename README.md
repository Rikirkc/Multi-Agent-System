# Multi-Agent-System

This project is a multi-agent system designed to process invoices from emails, PDF files, and JSON files. It uses a combination of AI agents to classify and extract invoice data, storing the results in a SQLite database. The system features a Streamlit-based frontend for uploading files and viewing processed invoices, and an IMAP-based email fetcher to process invoices from emails with "invoice" in the subject line.
Features

Multi-Agent Architecture: Includes agents for classifying input formats (PDF, JSON, Email), extracting invoice data, and processing different input types.
Email Processing: Fetches seen and unseen emails with "invoice" in the subject via IMAP, extracting JSON-formatted invoice data.
File Upload: Supports uploading PDF and JSON files through a Streamlit interface.
Database Storage: Stores extracted invoice data in a SQLite database with deduplication based on Invoice No..
Streamlit Frontend: Provides a user-friendly interface to upload files, check email invoices, and view stored invoices.

Project Structure
Multi-Agent-System/
│
├── agents/
│   ├── classifier_agent.py   # Classifies input format and intent
│   ├── json_agent.py         # Processes JSON inputs
│   ├── email_agent.py        # Processes text-based email inputs
│   ├── pdf_agent.py          # Processes PDF inputs
│
├── utils/
│   ├── multi_agent_system.py # Orchestrates agents and email fetcher
│   ├── email_fetcher.py      # Fetches invoices from email via IMAP
│   ├── shared_memory.py      # Manages SQLite database operations
│   ├── prompts.py            # Defines prompt template for extraction
│
├── dummy_data/
│   ├── test.json             # Sample JSON invoice for testing
│   ├── test.pdf              # Sample PDF invoice for testing
│
├── app.py                    # Streamlit frontend
├── .gitignore                # Excludes .env, virtual env, and database
├── README.md                 # Project documentation

Prerequisites

Python: Version 3.8 or higher
Virtual Environment: Recommended for dependency isolation
IMAP Email Account: Configured for IMAP access (e.g., Gmail with App Password)
Google Gemini API Key: For the langchain-google-genai package

Setup Instructions

Clone the Repository
git clone https://github.com/your-username/Multi-Agent-System.git
cd Multi-Agent-System


Create and Activate Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: assignmentenv\Scripts\activate


Install Dependencies
pip install streamlit sqlalchemy PyPDF2 langchain-google-genai python-dotenv


Configure Environment Variables

Create a .env file in the root directory with the following content:GEMINI_API_KEY=your_api_key
IMAP_SERVER=your_imap_server  # e.g., imap.gmail.com
IMAP_USER=your_email
IMAP_PASSWORD=your_password   # Use App Password for Gmail with 2FA


Obtain a Google Gemini API key from Google’s API services.
For Gmail, enable IMAP and generate an App Password if two-factor authentication is enabled.


Prepare Test Data

The dummy_data directory contains test.json and test.pdf for testing.
Ensure test.json contains valid JSON in the format:{
  "Invoice Date": "2025-05-01",
  "Customer Name": "John Doe",
  "Customer Billing Address": "123 Main St, City, Country",
  "Customer Shipping Address": "123 Main St, City, Country",
  "Item Names/IDs": ["Widget A", "Widget B"],
  "Quantity": ["2.00", "1.00"],
  "Invoice No.": "12345",
  "Final Amount": "130"
}


Ensure test.pdf is a text-based PDF with similar invoice details.



Running the Application

Start the Streamlit App
streamlit run app.py


The app will open in your browser at http://localhost:8501.


Using the App

Check Email Invoices: Click "Check for New Invoices" to fetch emails with "invoice" in the subject. Processed invoices are displayed with their subject, extracted data, and thread ID.
Upload Files: Use the file uploader to upload test.pdf or test.json. The processed invoice data is displayed with its thread ID.
View Stored Invoices: The "Stored Invoices" section shows all invoices in the database, including source, type, timestamp, and extracted data.



Database

Location: A SQLite database (memory.db) is created in the root directory on first run.
Schema: Stores thread_id, source (Email, PDF, JSON), type (Invoice), timestamp, and extracted_data (JSON invoice data).
Deduplication: Prevents duplicate entries based on Invoice No..

Email Processing

Emails with "invoice" in the subject are fetched via IMAP (seen and unseen).
The email body must contain valid JSON in the format shown above.
Processed emails are marked as seen to avoid re-fetching.

Troubleshooting

IMAP Connection Errors: Ensure .env variables are correct. For Gmail, use an App Password and enable IMAP in account settings.
PDF Processing Issues: Ensure PDFs are text-based (not scanned images) for PyPDF2 to extract text.
JSON Errors: Verify that JSON inputs (email or uploaded files) are valid and match the expected format.
Database Issues: Check that memory.db is writable and not locked. Delete and restart if corrupted.
Streamlit Not Loading: Run streamlit run app.py from the root directory and ensure dependencies are installed.

Contributing

Fork the repository and create a pull request with your changes.
Ensure code follows PEP 8 style guidelines.
Add tests for new features and document changes in the README.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments

Built with Streamlit, SQLAlchemy, PyPDF2, and LangChain.
Powered by Google Gemini API for AI processing.

