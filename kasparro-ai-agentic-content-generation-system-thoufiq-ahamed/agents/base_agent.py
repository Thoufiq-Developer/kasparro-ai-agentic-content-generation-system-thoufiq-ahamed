import json
import re
from config import get_llm

class BaseAgent:
    def __init__(self, name: str):
        self.name = name
        self.llm = get_llm()

    def call_llm(self, prompt: str) -> str:
        return self.llm.invoke(prompt)

    def parse_json(self, text: str):
        if not text or not text.strip():
            raise ValueError(f"[{self.name}] LLM returned empty response")

        # 1. Try direct JSON
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            pass

        # 2. Try extracting JSON object or array
        match = re.search(r"\{.*\}|\[.*\]", text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group())
            except json.JSONDecodeError:
                pass

        # 3. Fail loudly with raw output (for debugging)
        raise ValueError(
            f"[{self.name}] JSON parsing failed.\n"
            f"Raw model output:\n{text}"
        )
