
class QuestionGeneratorAgent:
    def generate(self, product):
        return [
            {"category": "Usage", "question": f"How should {product['name']} be used?"},
            {"category": "Safety", "question": "Are there any side effects?"},
            {"category": "Benefits", "question": "What are the benefits?"},
            {"category": "Price", "question": "What is the price?"}
        ]
