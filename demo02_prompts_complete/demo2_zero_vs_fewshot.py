# Zero-shot vs Few-shot.

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


def ask_llm(messages):
    """Send structured messages to LLM"""
    print(f"\n ask_llm()...")
    response = client.chat.completions.create(
        model=deployment,
        messages=messages,
        temperature=0.2  # Keep output stable for comparison
    )
    return response.choices[0].message.content


# Input (intentionally ambiguous)
input_text = "The product quality is good, but delivery was very late and support was unresponsive."


# Zero-shot (no examples)
zero_shot_messages = [
    {
        "role": "system",
        "content": "Classify sentiment as Positive, Negative, or Neutral."
    },
    {
        "role": "user",
        "content": input_text
    }
]


# Few-shot (with examples → teaches structure + logic)
few_shot_messages = [
    {
        "role": "system",
        "content": "Extract sentiment and reason from the text. Output format: Sentiment | Reason"
    },

    # Example 1
    {
        "role": "user",
        "content": "The service was excellent and very fast."
    },
    {
        "role": "assistant",
        "content": "Positive | Fast and excellent service"
    },

    # Example 2
    {
        "role": "user",
        "content": "The product is okay but customer support is terrible."
    },
    {
        "role": "assistant",
        "content": "Negative | Poor customer support"
    },

    # Actual query
    {
        "role": "user",
        "content": input_text
    }
]


print("\n--- Zero-shot Output ---\n")
print(ask_llm(zero_shot_messages))

print("\n--- Few-shot Output ---\n")
print(ask_llm(few_shot_messages))
