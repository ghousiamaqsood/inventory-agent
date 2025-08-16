
import os
from dotenv import load_dotenv
from agent import process_command

# Load API key from .env (but not used directly for homework)
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print("✅ API Key Loaded!")
else:
    print("⚠️ API Key not found. Please set it in .env file.")

print("🤖 Inventory Agent Ready! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("👋 Goodbye!")
        break
    response = process_command(user_input)
    print(f"Agent: {response}")
