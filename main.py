from ollama import chat

messages = []

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
        messages=messages
    )

    ai_message = response.message.content

    print("AI:", ai_message)

    messages.append({
        "role": "assistant",
        "content": ai_message
    })