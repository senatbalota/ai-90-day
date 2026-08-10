from ollama import chat
import json

messages = [
    {
        "role": "user",
        "content": """
You are a CNC furniture project assistant.

Your job is to analyze customer requests for custom furniture.

Focus only on information explicitly provided by the customer.

Extract the following information when explicitly mentioned by the customer:

- dimensions, including width, height, and depth
- materials
- finish
- number of drawers
- number and type of shelves

Do not omit information that the customer explicitly provided.

Do not assume or invent:
- hardware
- mounting details
- manufacturing requirements

For missing information, list only information that is necessary to define the project but was not provided by the customer.

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