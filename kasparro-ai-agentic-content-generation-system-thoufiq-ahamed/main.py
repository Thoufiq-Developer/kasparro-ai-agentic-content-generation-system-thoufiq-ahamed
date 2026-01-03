import json
from agents import (
    DataParserAgent,
    QuestionGeneratorAgent,
    FAQGeneratorAgent,
    ContentGeneratorAgent,
    ComparisonAgent
)

PRODUCT_DATA = {
    "product_name": "GlowBoost Vitamin C Serum",
    "concentration": "10% Vitamin C",
    "skin_type": ["Oily", "Combination"],
    "key_ingredients": ["Vitamin C", "Hyaluronic Acid"],
    "benefits": ["Brightening", "Fades dark spots"],
    "how_to_use": "Apply 2–3 drops in the morning before sunscreen",
    "side_effects": "Mild tingling for sensitive skin",
    "price": "₹699"
}

def main():
    parser = DataParserAgent()
    qgen = QuestionGeneratorAgent()
    faq = FAQGeneratorAgent()
    content = ContentGeneratorAgent()
    compare = ComparisonAgent()

    parsed = parser.run(PRODUCT_DATA)
    questions = qgen.run(parsed)
    faqs = faq.run(parsed, questions)
    page = content.run(parsed)
    comparison = compare.run(parsed)

    print(json.dumps({
        "parsed_data": parsed,
        "questions": questions,
        "faq_page": faqs,
        "product_page": page,
        "comparison_page": comparison
    }, indent=2))

if __name__ == "__main__":
    main()
