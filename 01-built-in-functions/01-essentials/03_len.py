# ==========================================
# len()
# Syntax: len(object, /)
# Return the length (the number of items) of an object.
# Ref: https://docs.python.org/3/library/functions.html#len
# ==========================================

print("--- len() Function ---")

# 1. String (Characters Count)
print("\n--- Strings ---")
# len จะนับทุกตัวอักษร รวมถึง " " ช่องว่าง
messages = "Hello, World"
print(f"String: '{messages}'")
print(f"Length: {len(messages)}")  # Output: 12

# 2. Collections (List, Dict. Tuple)
print("\n--- Collections ---")
fruits = ["Apple", "Banana", "Cherry"]
user_info = {"name": "Admin", "id": 100, "active": True}

print(f"List items: {len(fruits)}")  # Output: 3
print(f"Dict keys: {len(user_info)}")  # Output: 3
