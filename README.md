## System Performance:
Given a single product dataset (GlowBoost Vitamin C Serum), the system automatically:

- Cleans and structures the raw product data
- Generates user-style questions about the product
- Converts those questions into an FAQ page
- Creates a product description page
- Generates a comparison page with a fictional competitor

All outputs are produced in machine-readable JSON format

Instead of using one large function or one prompt, the system is split into
**independent agents**, where each agent:

- Has a single responsibility
- Takes structured input
- Produces structured output
- Can be reused or replaced easily

This makes the system easier to understand, debug, and extend.

## How the system works (simple explanation)

1. Product data is given as input
2. The data parser agent cleans and normalizes it
3. The question generator creates user questions
4. The FAQ agent answers those questions
5. The content agent builds the product page
6. The comparison agent creates a competitor comparison
7. Final output is returned as JSON

## Technology Used

- Python
- LangChain
- Hugging Face Transformers
- Local instruction-tuned model (google/flan-t5-base)



