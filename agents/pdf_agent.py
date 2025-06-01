import json
import re
import PyPDF2

class PDFAgent:
    def __init__(self, llm, memory, prompt_template):
        self.llm = llm
        self.memory = memory
        self.prompt = prompt_template

    def process(self, input_data, thread_id):
        try:
            with open(input_data, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    page_text = page.extract_text() or ""
                    text += page_text
            prompt_value = self.prompt.invoke({"invoice_text": text})
            result = self.llm.invoke(prompt_value)
            cleaned = re.sub(r"```(?:json)?\s*([\s\S]*?)\s*```", r"\1", result.content).strip()
            result_json = json.loads(cleaned)
            self.memory.save(thread_id, "PDF", "Invoice", result_json)
            return result_json
        except Exception as e:
            return {"error": f"PDF processing failed: {str(e)}"}
