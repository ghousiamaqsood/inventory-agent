import json
import os

INVENTORY_FILE = "inventory.json"

def load_inventory():
    if not os.path.exists(INVENTORY_FILE):
        return {}
    with open(INVENTORY_FILE, "r") as f:
        return json.load(f)

def save_inventory(inventory):
    with open(INVENTORY_FILE, "w") as f:
        json.dump(inventory, f, indent=4)

def process_command(command):
    inventory = load_inventory()
    words = command.lower().split()

    # Add item
    if "add" in words:
        try:
            qty = int(words[words.index("add")+1])
            item = words[words.index("to")+1] if "to" in words else words[-1]
            inventory[item] = inventory.get(item, 0) + qty
            save_inventory(inventory)
            return f"Added {qty} {item}(s). New stock: {inventory[item]}."
        except:
            return "❌ Invalid add command."

    # Remove item
    elif "remove" in words:
        try:
            qty = int(words[words.index("remove")+1])
            item = words[-1]
            if item in inventory and inventory[item] >= qty:
                inventory[item] -= qty
                save_inventory(inventory)
                return f"Removed {qty} {item}(s). Remaining stock: {inventory[item]}."
            else:
                return f"❌ Not enough {item} in stock."
        except:
            return "❌ Invalid remove command."

    # Check stock
    elif "check" in words or "stock" in words:
        item = words[-1]
        if item in inventory:
            return f"Stock for {item}: {inventory[item]}"
        else:
            return f"❌ {item} not found in inventory."

    # Show all
    elif "show" in words and "all" in words:
        return json.dumps(inventory, indent=4)

    else:
        return "❌ Command not recognized."
