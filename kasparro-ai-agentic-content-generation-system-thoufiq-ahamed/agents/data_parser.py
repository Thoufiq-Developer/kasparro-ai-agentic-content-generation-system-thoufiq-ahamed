import json
from agents.base_agent import BaseAgent

class DataParserAgent(BaseAgent):
    def __init__(self):
        super().__init__("DataParser")

    def run(self, raw_data: dict) -> dict:
        prompt = f"""
You are a JSON generator.

Convert the following product data into VALID JSON.
DO NOT add explanations.
DO NOT add text outside JSON.

Required keys:
name, ingredients, concentration, benefits, usage,
side_effects, skin_types, price, category

Data:
{json.dumps(raw_data, indent=2)}

Return ONLY JSON.
"""

        response = self.call_llm(prompt)
        return self.parse_json(response)
