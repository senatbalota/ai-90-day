from ollama import chat
import json

messages = [
    {
        "role": "user",
        "content": """
You are a CNC furniture project assistant.

Your job is to analyze customer requests for custom furniture.

Focus on:
- dimensions
- materials
- finish
- hardware
- mounting
- manufacturing requirements
- missing information

Never invent information that the customer did not provide.
Clearly separate known information from missing information.

Return your answer as JSON
"""
    }
]

while True:
    user_message = input("You: ")

    if user_message == "exit":
        break

    messages.append({
        "role": "user",
        "content": user_message
    })

    response = chat(
        model="qwen3:0.6b",
        messages=messages,
        format="json"
    )

    ai_message = response.message.content

    data = json.loads(ai_message)

    with open("ai_output.txt", "w", encoding="utf-8") as file:
        file.write(ai_message)

    messages.append({
        "role": "assistant",
        "content": ai_message
    })