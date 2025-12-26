
import json, os

class PageAssemblerAgent:
    def save(self, filename, data):
        os.makedirs("output", exist_ok=True)
        with open(f"output/{filename}", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
