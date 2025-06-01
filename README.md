# 🧠 Multi-Agent Invoice Processor

Welcome to the Multi-Agent System – your AI-powered assistant for processing invoices from emails, PDFs, and JSON files! This project uses a team of AI agents to classify, extract, and store invoice data automatically. It features:

📥 Email fetching via IMAP

📂 File uploads through a sleek Streamlit UI

📊 Data storage with SQLite

🤖 AI-driven extraction via Google Gemini

Let’s get into it! 🚀

🔍 Features
✨ Multi-Agent Architecture
Agents work together to:

Detect file types (PDF, JSON, Email)

Extract invoice data from them

Save and deduplicate entries

📧 Email Processing

Fetches both seen and unseen emails with "invoice" in the subject

Extracts invoice data in JSON format from email bodies

📂 File Upload Support

Upload .pdf and .json files through the Streamlit UI

Data is extracted and stored with ease

🧠 AI-Powered Extraction

Uses Google Gemini via LangChain to help understand and process files

💾 SQLite Database Storage

Deduplicates using Invoice No.

Keeps a record of source, type, timestamp, and full invoice data

🖼️ Streamlit Frontend

Beautiful and functional UI

Upload files, check emails, and view stored invoices from your browser

📦 Prerequisites
🐍 Python 3.8 or higher

🌱 Virtual environment (recommended)

📧 IMAP-enabled email account (e.g., Gmail with App Password)

🔑 Google Gemini API Key (for AI-powered invoice extraction)

⚙️ Setup Instructions
1. 🧬 Clone the Repo
bash
Copy
Edit
git clone https://github.com/your-username/Multi-Agent-System.git
cd Multi-Agent-System
2. 🐍 Set Up Your Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. 📥 Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Or manually:

bash
Copy
Edit
pip install streamlit sqlalchemy PyPDF2 langchain-google-genai python-dotenv
4. 🛠️ Configure Environment Variables
Create a .env file in the root directory:

ini
Copy
Edit
GEMINI_API_KEY=your_api_key
IMAP_SERVER=imap.gmail.com
IMAP_USER=your_email@gmail.com
IMAP_PASSWORD=your_app_password
💡 Tip: Use a Gmail App Password if you have 2FA enabled.

🧪 Test Data
The dummy_data folder includes:

test.json (Sample invoice data)

test.pdf (Text-based PDF with invoice details)

Make sure test.json looks something like this:

json
Copy
Edit
{
  "Invoice Date": "2025-05-01",
  "Customer Name": "John Doe",
  "Customer Billing Address": "123 Main St",
  "Customer Shipping Address": "123 Main St",
  "Item Names/IDs": ["Widget A", "Widget B"],
  "Quantity": ["2.00", "1.00"],
  "Invoice No.": "12345",
  "Final Amount": "130"
}
🚀 Running the App
Fire it up with:

bash
Copy
Edit
streamlit run app.py
Then visit: http://localhost:8501

🧑‍💻 Using the App
📧 Check Email Invoices
Click “Check for New Invoices”

Fetches and processes emails with "invoice" in the subject

📤 Upload Files
Upload .pdf or .json invoices

Extracted data is displayed right away

📚 View Stored Invoices
See all stored invoices

Includes source (email/PDF/JSON), type, timestamp, and full data

🗃️ Database Info
Location: memory.db (auto-created in the root directory)

Contents: thread_id, source, type, timestamp, and extracted_data

Deduplication: Based on Invoice No. – no duplicates allowed!

🛠️ Troubleshooting
Problem	Solution
IMAP Errors	: Double-check .env. For Gmail, use App Password & enable IMAP.
PDF Not Reading	: Use text-based PDFs (not scanned images).
JSON Format Errors :	Make sure JSON is valid and follows expected structure.
Locked Database (memory.db) :	Close the app, delete the DB file, and restart.
Streamlit App Not Loading	: Run streamlit run app.py from the root directory.

📄 License
MIT License – see LICENSE for details.

🙌 Acknowledgments
Built with ❤️ using Streamlit, SQLAlchemy, PyPDF2, and LangChain

Powered by Google Gemini for intelligent extraction
