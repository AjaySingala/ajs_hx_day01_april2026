# Rewrite a Poor Prompt.

# Set env vars from config.py.
import sys
import os

# Add the folder path (use absolute or relative path)
folder_path = os.path.join(os.path.dirname(__file__), '../')
sys.path.insert(0, folder_path)

import config

# Start.
from openai import AzureOpenAI

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")


# Helper function to call the model
def ask_llm(prompt: str):
    """Send a prompt to Azure OpenAI and return response text"""
    print(f"\n ask_llm()...")
    response = client.chat.completions.create(
        model=deployment,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7  # Slight creativity
    )
    return response.choices[0].message.content


# Poor prompt (ambiguous, no structure)
poor_prompt = "Write an email to a customer about a delay"

# Improved prompt (clear role + context + structure)
better_prompt = """
You are a customer support executive.

Write a professional email to a customer informing them about a 3-day delay 
in delivery of their order.

Include:
- Apology
- Reason (logistics issue)
- Reassurance
- Offer 10% discount coupon

Keep tone polite and concise.
"""


print("\n--- Poor Prompt Output ---\n")
print(ask_llm(poor_prompt))

print("\n--- Improved Prompt Output ---\n")
print(ask_llm(better_prompt))
