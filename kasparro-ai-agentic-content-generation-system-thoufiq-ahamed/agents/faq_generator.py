import json
from agents.base_agent import BaseAgent

class FAQGeneratorAgent(BaseAgent):
    def __init__(self):
        super().__init__("FAQGenerator")

    def run(self, product_data: dict, questions: list):
        faqs = []
        for q in questions[:5]:
            prompt = f"""
Answer the question using ONLY the product data.

Product:
{json.dumps(product_data, indent=2)}

Question: {q['question']}

Return JSON with category, question, answer.
"""
            response = self.call_llm(prompt)
            faqs.append(self.parse_json(response))

        return {
            "product": product_data.get("name"),
            "faqs": faqs
        }
