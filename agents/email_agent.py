import json
import re

class EmailAgent:
    def __init__(self, llm, memory, prompt_template):
        self.llm = llm
        self.memory = memory
        self.prompt = prompt_template

    def process(self, input_data, thread_id):
        try:
            prompt_value = self.prompt.invoke({"invoice_text": input_data})
            result = self.llm.invoke(prompt_value)
            cleaned = re.sub(r"```(?:json)?\s*([\s\S]*?)\s*```", r"\1", result.content).strip()
            result_json = json.loads(cleaned)
            self.memory.save(thread_id, "Email", "Invoice", result_json)
            return result_json
        except Exception as e:
            return {"error": f"Email processing failed: {str(e)}"}