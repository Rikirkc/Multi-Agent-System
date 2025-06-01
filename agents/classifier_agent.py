from langchain.prompts import PromptTemplate

class ClassifierAgent:
    def __init__(self, llm):
        self.llm = llm
        self.prompt = PromptTemplate.from_template("""
            You are a classifier agent. Analyze the input and determine:
            1. Format: PDF, JSON, or Email
            2. Intent: Invoice, RFQ, Complaint, Regulation, or Other
            Return the result in JSON format:
            {{
                "format": "...",
                "intent": "..."
            }}
            Input: {input_data}
        """)

    def classify(self, input_data):
        try:
            if isinstance(input_data, str) and input_data.lower().endswith('.pdf'):
                return {"format": "PDF", "intent": "Invoice"}
            elif isinstance(input_data, dict) or (isinstance(input_data, str) and input_data.strip().startswith('{')):
                return {"format": "JSON", "intent": "Invoice"}
            elif isinstance(input_data, str) and ('Subject:' in input_data or '@' in input_data):
                return {"format": "Email", "intent": "Invoice"}
            else:
                return {"format": "Unknown", "intent": "Other"}
        except Exception as e:
            return {"format": "Unknown", "intent": "Other"}