import os
from typing import Optional
from openai import OpenAI
from memory import add_message, get_messages
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# System prompt to guide the AI's behavior
SYSTEM_PROMPT = """You are a helpful and friendly chat assistant. 
Keep your responses concise but informative.
If you don't know something, say so clearly.
Always maintain a professional and helpful tone."""

async def chat(user_input: str) -> Optional[str]:
    # Save user message
    add_message({
        "role": "user",
        "content": user_input
    })

    # Get chat history
    history = get_messages()

    # Format messages for API
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        *[{"role": msg.role, "content": msg.content} for msg in history]
    ]

    # Get AI response
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0.7,
    )

    ai_response = completion.choices[0].message.content

    # Save AI response
    if ai_response:
        add_message({
            "role": "assistant",
            "content": ai_response
        })

    return ai_response