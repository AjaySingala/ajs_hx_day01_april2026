# Prompt as Product” (Template + Variables).

# Set env vars from config.py.
import sys
import os

# Add the folder path (use absolute or relative path)
folder_path = os.path.join(os.path.dirname(__file__), '../')
sys.path.insert(0, folder_path)

import config

# Start.
from dotenv import load_dotenv
import os
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")


def ask_llm(prompt: str):
    """Call LLM"""
    print(f"\n ask_llm()...")
    response = client.chat.completions.create(
        model=deployment,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response.choices[0].message.content


# Prompt template with variables
EMAIL_TEMPLATE = """
You are a {role}.

Write an email to a customer about:
Issue: {issue}

Include:
- Tone: {tone}
- Resolution: {resolution}
"""


# Reuse same template with different inputs
scenarios = [
    {
        "role": "Support Executive",
        "issue": "Delayed delivery",
        "tone": "Apologetic",
        "resolution": "10% discount"
    },
    {
        "role": "Premium Support Manager",
        "issue": "Product defect",
        "tone": "Highly empathetic",
        "resolution": "Full refund + replacement"
    }
]

n = 1
for s in scenarios:
    prompt = EMAIL_TEMPLATE.format(**s)  # Fill template dynamically
    print(f"\n--- Scenario {n}: {s["role"]} ---\n")
    print(f"Prompt: {prompt}\n")
    print(ask_llm(prompt))
    n += 1
