# ==========================================
# sum() Function
# Syntax: sum(iterable, start=0)
# ==========================================

print("--- 1. Basic List ---")
numbers = [1, 2, 3, 4, 5]
print(f"Normal sum: {sum(numbers)}")  # 15


# Usage with 'start' argument
# Logic: 5 + (1 + 2 + 3 + 4 + 5)
print(f"Sum with start = 5: {sum(numbers, 5)}")  # 20


print("\n--- 2. Other Data Type ---")
# Dictionary
dict_numbers = {"a": 2, "b": 4, "c": 6}
# Note: ต้องใช้ .values() ถ้า sum(dict_numbers) เฉยๆ จะไปบวก Key แทน
print(f"Dictionary values: {sum(dict_numbers.values())}")

# Set
set_numbers = {1, 3, 5, 7, 9}
print(f"Set sum: {sum(set_numbers)}")

# Tuple
tuple_numbers = (2, 4, 6, 8, 10)
print(f"Tuple sum: {sum(tuple_numbers)}")

print("\n--- 3. Advanced Tricks ---")
# Flatten List (รวม List ซ้อน List)
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = sum(nested_list, [])
print(f"Flatten listL {flat_list}")  # [1, 2, 3, 4, 5, 6]
# Note: แนะนำใช้กับข้อมูลน้อยๆ ถ้าข้อมูลเยอะแนะนำ itertools.chain() จะเร็วกว่า


print("\n--- 4. Sum with Objects (Timedelta) ---")
from datetime import timedelta

tasks = [timedelta(minutes=10), timedelta(minutes=20), timedelta(hours=1)]
# Note: ต้องระบุ start เป็น timedelta() หรือ 0
total_time = sum(tasks, timedelta())
print(total_time)  # 1:30:00

print("\n--- 5. Common Errors ---")
# How to sum text?
words = ["Hello", "World"]

# WRONG:
# print(sum(words, ""))
# TypeError: sum() can't sum strings [use ''.join(seq) instead]

# CORRECT
print(f"Correct way (join): {''.join(words)}")
