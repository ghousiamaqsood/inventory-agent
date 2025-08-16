# # # -------------------------------
# # # Inventory Agent Project
# # # Homework using OpenAI Chat API
# # # -------------------------------

# # import os
# # import json
# # from openai import OpenAI

# # # -------------------------------
# # # API Key Handling
# # # -------------------------------
# # api_key = os.getenv("OPENAI_API_KEY")

# # if not api_key:
# #     # fallback: directly assign key (testing only ⚠️)
# #     api_key = "REMOVED"

# # client = OpenAI(api_key=api_key)

# # print("✅ API Key Loaded!")

# # # -------------------------------
# # # Helper functions for inventory
# # # -------------------------------
# # def load_inventory():
# #     """Load inventory data from JSON file"""
# #     with open("inventory.json", "r") as f:
# #         return json.load(f)

# # def save_inventory(data):
# #     """Save inventory data to JSON file"""
# #     with open("inventory.json", "w") as f:
# #         json.dump(data, f, indent=2)

# # # -------------------------------
# # # Tools for the Agent
# # # -------------------------------
# # def check_stock(product: str) -> str:
# #     data = load_inventory()
# #     if product in data:
# #         return f"{product} has {data[product]} items left."
# #     else:
# #         return f"{product} not found in inventory."

# # def add_stock(product: str, quantity: int) -> str:
# #     data = load_inventory()
# #     if product in data:
# #         data[product] += quantity
# #     else:
# #         data[product] = quantity
# #     save_inventory(data)
# #     return f"Added {quantity} {product}. New stock: {data[product]}."

# # def low_stock_report(threshold: int = 5) -> str:
# #     data = load_inventory()
# #     low_items = {k: v for k, v in data.items() if v < threshold}
# #     if not low_items:
# #         return "No low stock items."
# #     return f"Low stock items: {low_items}"

# # # -------------------------------
# # # Chatbot Loop (Agent Simulation)
# # # -------------------------------
# # if __name__ == "__main__":
# #     print("🤖 Inventory Agent Ready! Type 'exit' to quit.\n")

# #     while True:
# #         user_input = input("You: ")
# #         if user_input.lower() == "exit":
# #             break

# #         # Simple tool routing (manual agent behavior)
# #         if "check" in user_input.lower():
# #             product = user_input.split()[-1]
# #             reply = check_stock(product)
# #         elif "add" in user_input.lower():
# #             parts = user_input.split()
# #             product = parts[-2]
# #             qty = int(parts[-1])
# #             reply = add_stock(product, qty)
# #         elif "low stock" in user_input.lower():
# #             reply = low_stock_report()
# #         else:
# #             # fallback: ask GPT
# #             response = client.chat.completions.create(
# #                 model="gpt-4o-mini",
# #                 messages=[
# #                     {"role": "system", "content": "You are an inventory assistant."},
# #                     {"role": "user", "content": user_input}
# #                 ]
# #             )
# #             reply = response.choices[0].message.content

# #         print("Agent:", reply)
# # -------------------------------
# # Inventory Agent Project
# # Homework using OpenAI Chat API
# # -------------------------------

# import os
# import json
# from openai import OpenAI

# # -------------------------------
# # API Key Handling
# # -------------------------------
# api_key = os.getenv("OPENAI_API_KEY")

# if not api_key:
#     # fallback: directly assign key (testing only ⚠️)
#     api_key = "REMOVED"

# client = OpenAI(api_key=api_key)

# print("✅ API Key Loaded!")

# # -------------------------------
# # Helper functions for inventory
# # -------------------------------
# def load_inventory():
#     """Load inventory data from JSON file"""
#     with open("inventory.json", "r") as f:
#         return json.load(f)

# def save_inventory(data):
#     """Save inventory data to JSON file"""
#     with open("inventory.json", "w") as f:
#         json.dump(data, f, indent=2)

# # -------------------------------
# # Tools for the Agent
# # -------------------------------
# def check_stock(product: str) -> str:
#     data = load_inventory()
#     if product in data:
#         return f"{product} has {data[product]} items left."
#     else:
#         return f"{product} not found in inventory."

# def add_stock(product: str, quantity: int) -> str:
#     data = load_inventory()
#     if product in data:
#         data[product] += quantity
#     else:
#         data[product] = quantity
#     save_inventory(data)
#     return f"Added {quantity} {product}. New stock: {data[product]}."

# def low_stock_report(threshold: int = 5) -> str:
#     data = load_inventory()
#     low_items = {k: v for k, v in data.items() if v < threshold}
#     if not low_items:
#         return "No low stock items."
#     return f"Low stock items: {low_items}"

# # -------------------------------
# # Chatbot Loop (Agent Simulation)
# # -------------------------------
# if __name__ == "__main__":
#     print("🤖 Inventory Agent Ready! Type 'exit' to quit.\n")

#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == "exit":
#             break

#         # Simple tool routing (manual agent behavior)
#         if "check" in user_input.lower():
#             product = user_input.split()[-1]
#             reply = check_stock(product)

#         elif "add" in user_input.lower():
#             try:
#                 parts = user_input.lower().split()

#                 # Find first number (quantity)
#                 qty = None
#                 for p in parts:
#                     if p.isdigit():
#                         qty = int(p)
#                         break

#                 if qty is None:
#                     reply = "⚠️ Please specify a quantity (e.g., 'Add 10 chairs')."
#                 else:
#                     # Remove keywords + number to get product name
#                     exclude = {"add", "to", "the", "inventory"}
#                     item = " ".join([p for p in parts if p not in exclude and not p.isdigit()])

#                     if not item.strip():
#                         reply = "⚠️ Please specify an item name (e.g., 'Add 10 tables')."
#                     else:
#                         reply = add_stock(item.strip(), qty)

#             except Exception as e:
#                 reply = f"⚠️ Error while adding item: {e}"

#         elif "low stock" in user_input.lower():
#             reply = low_stock_report()

#         else:
#             # fallback: ask GPT
#             response = client.chat.completions.create(
#                 model="gpt-4o-mini",
#                 messages=[
#                     {"role": "system", "content": "You are an inventory assistant."},
#                     {"role": "user", "content": user_input}
#                 ]
#             )
#             reply = response.choices[0].message.content

#         print("Agent:", reply)
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
