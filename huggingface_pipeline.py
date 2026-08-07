from huggingface_hub import login
import config 
from transformers import pipeline

if config.HF_TOKEN and config.HF_TOKEN.startswith("hf_"):
    print("HF key looks good so far")
else:
    print("HF key is not set - please click the key in the left sidebar")

login(config.HF_TOKEN, add_to_git_credential=True)

my_simple_sentiment_analyzer = pipeline(task="sentiment-analysis",model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")
result = my_simple_sentiment_analyzer("I'm super excited for my trip to Thailand!")
print(result)

result = my_simple_sentiment_analyzer("I should be more excited for my trip to Thailand!")
print(result)

question="What are Hugging Face pipelines?"
context="Pipelines are a high level API for inference of LLMs with common tasks"

classifier = pipeline("zero-shot-classification")
result = classifier("Hugging Face's Transformers library is amazing!", candidate_labels=["technology", "sports", "politics"])
print(result)