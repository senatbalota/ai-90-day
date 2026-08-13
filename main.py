from ollama import chat
import json

messages = [
    {
        "role": "user",
        "content": """
You are a CNC furniture project assistant.

Your job is to analyze customer requests for custom furniture.

Focus only on information provided by the customer.

Extract the following information when mentioned by the customer:

- dimensions, including width, height, and depth
- materials
- finish
- number of drawers
- number and type of shelves

Do not omit information that the customer provided.

Never invent dimensions, materials, drawers, shelves, or any other information.

If a dimension is not provided, mark it as "missing".

If the number of drawers is not provided, mark it as "missing".

If the shelves are not provided, mark them as "missing".

Only extract information stated by the customer.

Use this JSON structure:

{
  "dimensions": {
    "width": "value or missing",
    "height": "value or missing",
    "depth": "value or missing"
  },
  "materials": "value or missing",
  "finish": "value or missing",
  "drawers": "value or missing",
  "shelves": "value or missing",
  "missing_information": []
}
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

    print("\n--- PROJECT SUMMARY ---")
    print("Width:", data["dimensions"]["width"])
    print("Drawers:", data["drawers"])
    print("Shelves:", data["shelves"])
    print("Material:", data["materials"])
    print("Finish:", data["finish"])

    if data["missing_information"]:
         print("\n--- QUESTIONS FOR CUSTOMER ---")

for item in data["missing_information"]:
    if item == "height":
        print("What height would you like for the TV unit?")
    elif item == "depth":
        print("What depth would you like for the TV unit?")
    elif item == "shelves":
        print("How many shelves would you like?")

    else:
         print("\nAll required information is available.")