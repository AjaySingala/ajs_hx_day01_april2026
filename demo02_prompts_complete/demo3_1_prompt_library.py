# Build a 3-Scenario Prompt Library.

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
    """Reusable function to call LLM"""
    print(f"\n ask_llm()...")
    response = client.chat.completions.create(
        model=deployment,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response.choices[0].message.content


# Prompt Library (3 business scenarios)
PROMPT_LIBRARY = {

    "email_response": """
    You are a customer support manager.
    Draft a response to a complaint about late delivery.
    Keep it professional and include apology and resolution.
    """,

    "data_summary": """
    You are a business analyst.
    Summarize the following sales data into key insights:

    Region A: 20% growth
    Region B: -5% decline
    Region C: 15% growth

    Provide 3 bullet insights.
    """,

    "meeting_summary": """
    You are an executive assistant.
    Summarize the following meeting notes into:
    - Key decisions
    - Action items

    Notes:
    Team discussed product launch delays.
    Marketing needs 2 more weeks.
    Engineering flagged bugs.
    """
}


# Simulate usage.
for scenario, prompt in PROMPT_LIBRARY.items():
    print(f"\n--- Scenario: {scenario} ---\n")
    print(ask_llm(prompt))

