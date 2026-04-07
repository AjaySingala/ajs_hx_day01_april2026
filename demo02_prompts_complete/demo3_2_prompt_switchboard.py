# Business Switchboard using Prompt Library.

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
    """Call LLM with a single prompt"""
    print(f"\n ask_llm()...")
    response = client.chat.completions.create(
        model=deployment,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response.choices[0].message.content


# Same input, different business contexts
user_input = "Customer is unhappy due to delayed delivery and poor support."


PROMPT_LIBRARY = {
    "Support Manager": f"""
    You are a customer support manager.
    Respond to this situation professionally:
    {user_input}
    """,

    "Marketing Head": f"""
    You are a marketing head.
    Turn this situation into a brand-positive communication:
    {user_input}
    """,

    "Operations Head": f"""
    You are an operations head.
    Analyze the issue and suggest process improvements:
    {user_input}
    """
}


for role, prompt in PROMPT_LIBRARY.items():
    print(f"\n--- Perspective: {role} ---\n")
    print(f"Perspective: {role}. Prompt: {prompt} \n")
    print("------------------")
    print(ask_llm(prompt))

