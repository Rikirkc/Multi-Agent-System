import uuid
from agents.classifier_agent import ClassifierAgent
from agents.json_agent import JSONAgent
from agents.email_agent import EmailAgent
from agents.pdf_agent import PDFAgent
from utils.email_fetcher import EmailFetcher
from utils.shared_memory import SharedMemory

class MultiAgentSystem:
    def __init__(self, llm, prompt_template, imap_server, imap_user, imap_password):
        self.memory = SharedMemory()
        self.llm = llm
        self.classifier = ClassifierAgent(self.llm)
        self.json_agent = JSONAgent(self.llm, self.memory, prompt_template)
        self.email_agent = EmailAgent(self.llm, self.memory, prompt_template)
        self.pdf_agent = PDFAgent(self.llm, self.memory, prompt_template)
        self.email_fetcher = EmailFetcher(imap_server, imap_user, imap_password, self.json_agent, self.memory)

    def process_input(self, input_data, thread_id=None):
        if thread_id is None:
            thread_id = str(uuid.uuid4())

        if not input_data or (isinstance(input_data, str) and not input_data.strip()):
            return {"error": "Invalid or empty input"}

        classification = self.classifier.classify(input_data)
        format_type = classification.get("format", "")
        intent = classification.get("intent", "")

        if not format_type or format_type == "Unknown":
            return {"error": "Unable to classify input format"}

        if format_type == "PDF":
            return self.pdf_agent.process(input_data, thread_id)
        elif format_type == "JSON":
            return self.json_agent.process(input_data, thread_id)
        elif format_type == "Email":
            return self.email_agent.process(input_data, thread_id)
        else:
            return {"error": "Unsupported format"}
