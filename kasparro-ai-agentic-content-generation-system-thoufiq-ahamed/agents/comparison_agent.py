import json
from agents.base_agent import BaseAgent

class ComparisonAgent(BaseAgent):
    def __init__(self):
        super().__init__("ComparisonAgent")

    def run(self, product_data: dict):
        prompt = f"""
Create a fictional competitor comparison.

Product A:
{json.dumps(product_data, indent=2)}

Return JSON with product_b, key_differences, recommendation.
"""
        response = self.call_llm(prompt)
        return self.parse_json(response)
