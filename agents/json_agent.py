# import json
# import re

# class JSONAgent:
#     def __init__(self, llm, memory, prompt_template):
#         self.llm = llm
#         self.memory = memory
#         self.prompt = prompt_template

#     def process(self, input_data, thread_id):
#         try:
#             if isinstance(input_data, dict):
#                 input_data = json.dumps(input_data)
#             prompt_value = self.prompt.invoke({"invoice_text": input_data})
#             result = self.llm.invoke(prompt_value)
#             cleaned = re.sub(r"```(?:json)?\s*([\s\S]*?)\s*```", r"\1", result.content).strip()
#             result_json = json.loads(cleaned)
#             self.memory.save(thread_id, "JSON", "Invoice", result_json)
#             return result_json
#         except Exception as e:
#             return {"error": f"JSON processing failed: {str(e)}"}

import json
import re

class JSONAgent:
    def __init__(self, llm, memory, prompt_template):
        self.llm = llm
        self.memory = memory
        self.prompt = prompt_template

    def process(self, input_data, thread_id, source="JSON"):
        try:
            if isinstance(input_data, dict):
                input_data = json.dumps(input_data)
            prompt_value = self.prompt.invoke({"invoice_text": input_data})
            result = self.llm.invoke(prompt_value)
            cleaned = re.sub(r"```(?:json)?\s*([\s\S]*?)\s*```", r"\1", result.content).strip()
            result_json = json.loads(cleaned)
            self.memory.save(thread_id, source, "Invoice", result_json)
            return result_json
        except Exception as e:
            return {"error": f"JSON processing failed: {str(e)}"}