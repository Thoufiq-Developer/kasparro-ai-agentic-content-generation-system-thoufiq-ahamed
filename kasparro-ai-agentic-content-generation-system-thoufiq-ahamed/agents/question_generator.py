import json
from agents.base_agent import BaseAgent

class QuestionGeneratorAgent(BaseAgent):
    def __init__(self):
        super().__init__("QuestionGenerator")

    def run(self, product_data: dict):
        prompt = f"""
Generate exactly 15 categorized user questions.

Product:
{json.dumps(product_data, indent=2)}

Categories: Usage, Safety, Benefits, Ingredients, Purchase, Comparison

Return ONLY a valid JSON array.
"""
        response = self.call_llm(prompt)
        return self.parse_json(response)
