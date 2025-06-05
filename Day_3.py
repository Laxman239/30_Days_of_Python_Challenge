# Challenge Day 3
# Create an inventory system tracking items and quantities with a dictionary


# The Python Pantry 🍪✨

inventory = {
    "Productivity Potion": 3,
    "Debugging Donuts": 12,
    "Focus Fuel": 5,
    "Code Coffee": 2
}

print("☕ Welcome to the Python Pantry! ☕")
print("Here's what's on the shelf today:")

for item, qty in inventory.items():
    print(f"🔹 {item}: {qty}")
