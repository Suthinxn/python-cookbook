# ==========================================
# len() Function
# Syntax: len(object)
# Return the length (the number of items) of an object. ใช้ได้กับ object ที่มีขนาด
# Ref: https://docs.python.org/3/library/functions.html#len
# Ref: https://www.geeksforgeeks.org/python/python-len-function/
# ==========================================

print("--- len() Funtion ---")

print("--- Basic len() ---")
text = "HelloLen"
print(f"len({text}) --> {len(text)}") # 8


print("\n--- List ---")
list_info = ["cat", "dog", "brid"]
print(f"len() List: {len(list_info)}") # 3


print("\n--- Tuple ---")
numbers = (1, 2, 3, 4, 5)
print(f"len() Tuple: {len(numbers)}") # 5

print("\n--- Dict ---")
information = {"name": "Boss",
               "age": "90",}
print(f"len() Dict: {len(information)}") # 2 Dict Keys

print("\n--- Example ---")

print("--- 1. Check record API ---")
response = {
    "status": "ok",
    "data": [
        {"id": 1, "score": 80},
        {"id": 2, "score": 95},
        {"id": 3, "score": 60}
    ]
}

if len(response["data"]) == 0:
    print("No data")
else:
    print(f"Received {len(response['data'])} records")

print("--- 2. Check feature before train ---")
sample = {
    "age": 21,
    "height": 170,
    "weight": 65
}

if len(sample) != 3:
    raise ValueError("Feature size mismatch")

