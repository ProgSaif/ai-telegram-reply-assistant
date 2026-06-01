#This is “brain”

from ollama import chat
import os

def load_file(path):
    if os.path.exists(path):
        return open(path, "r", encoding="utf-8").read()
    return ""

persona = load_file("persona.txt")
examples = load_file("examples.txt")

def generate_reply(message):

    prompt = f"""
{persona}

Examples:
{examples}

User message:
{message}

Reply in a natural, short, human-like style.
Do NOT mention AI.
"""

    response = chat(
        model="gemma4:latest",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.message.content.strip()
