import json
from agents.base_agent import BaseAgent

class ContentGeneratorAgent(BaseAgent):
    def __init__(self):
        super().__init__("ContentGenerator")

    def run(self, product_data: dict):
        prompt = f"""
Create product page content.

Product:
{json.dumps(product_data, indent=2)}

Return JSON with:
description, key_benefits, usage_guide, target_audience
"""
        response = self.call_llm(prompt)
        return self.parse_json(response)
