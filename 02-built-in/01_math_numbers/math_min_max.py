# ==========================================
# min() Function
# Syntax: min(arg1, arg2, arg3, ...) or min(iterable)
# Return the smallest item in an iterable or the smallest of two or more arguments.
# Ref: https://docs.python.org/3/library/functions.html#min
# ==========================================

print("--- min() Function ---")

print("--- List numbers ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"List min value: {min(numbers)}")  # 1

print("--- List words ---")
animal = ["cow", "dog", "cat", "owl"]
print(f"List animal: {min(animal)}")  # cat


print("--- Set ---")
numbers = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
print(f"Set min value: {min(numbers)}")  # 11


print("\n--- min() with key ---")
products = [
    {"name": "A", "price": 120},
    {"name": "B", "price": 80},
    {"name": "C", "price": 150},
]

cheapest = min(products, key=lambda x: x["price"])
print(cheapest)

# ==========================================
# max() Function
# Syntax: min(arg1, arg2, arg3, ...) or min(iterable)
# Return the largest item in an iterable or the largest of two or more arguments.
# Ref: https://docs.python.org/3/library/functions.html#max
# ==========================================

print("--- max() Function ---")

print("--- List numbers ---")
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number_set01 = 1
number_set02 = 20
number_set03 = 33

print(f"List max value: {max(number_set01, number_set02, number_set03)}")  # 1
