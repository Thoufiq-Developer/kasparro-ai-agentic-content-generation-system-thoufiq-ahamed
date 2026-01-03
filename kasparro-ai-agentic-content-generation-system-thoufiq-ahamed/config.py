from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline

def get_llm():
    hf_pipeline = pipeline(
        "text2text-generation",
        model="google/flan-t5-base",
        max_new_tokens=256,
        do_sample=False
    )
    return HuggingFacePipeline(pipeline=hf_pipeline)
