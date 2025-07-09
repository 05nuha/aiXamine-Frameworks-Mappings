import os
from openai import AzureOpenAI
import json

endpoint = "https://qcri-oai-aixamine-01.openai.azure.com/"
model_name = "gpt-4.1-mini"
deployment = "gpt-4.1-mini-aixamine"

subscription_key = os.getenv("AZURE_OPENAI_KEY")
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_key=subscription_key,
    api_version=api_version,
    azure_endpoint=endpoint,
)


