
from openai_client import client
from openai_client import client, deployment
import re
import json
from openai import AzureOpenAI
import os

def slugify(s: str) -> str:
    s = s.lower().replace("&", "and")
    s = re.sub(r'[^a-z0-9]+', '_', s)
    return s.strip('_')

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

def run_mitre(prompt, response, category):
    with open(f"schemas/mitreschema.json", "r") as f:
        schema = json.load(f)

    with open(f"prompts/{category.lower()}_mitre.txt", "r") as f:
        system_prompt = f.read().replace("{schema_str}", json.dumps(schema, indent=2))

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Prompt: {prompt}\nResponse: {response}"}
    ]

    chat_response = client.chat.completions.create(
        model=deployment,
        messages=messages,
        temperature=0
    )

    result_text = chat_response.choices[0].message.content
    try:
        return json.loads(result_text)[0]["annotations"]["MITRE ATLAS"]
    except:
        return []
