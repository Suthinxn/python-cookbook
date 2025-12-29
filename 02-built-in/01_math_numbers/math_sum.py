# ===== sum() =====
# ? Syntax: sum(iterable, start=0)

# List
numbers = [1, 2, 3, 4, 5]
result = sum(numbers)
print(result)  # 15

numbers = [1, 2, 3, 4, 5]
result = sum(numbers, 5)
# 5 + (1 + 2 + 3 + 4 + 5)
print(result)  # 20

# Dictionary
dict_numbers = {"a": 2, "b": 4, "c": 6}
print(dict_numbers.values())
print(sum(dict_numbers.values()))

# Set
set_numbers = {1, 3, 5, 7, 9}
print(sum(set_numbers))

# Tuple
tuple_numbers = (2, 4, 6, 8, 10)
print(sum(tuple_numbers))

# Flatten List
nested_list = [[1, 2], [3, 4], [5, 6]]

flat_list = sum(nested_list, [])
print(flat_list)  # [1, 2, 3, 4, 5, 6]
# Note แนะนำในข้อมูลที่มีไม่เยอะ ถ้าข้อมูลเยอะแนะนำ itertools.chain

# ใช้รวมเวลา (Timedelta)
from datetime import timedelta

tasks = [timedelta(minutes=10), timedelta(minutes=20), timedelta(hours=1)]

total_time = sum(tasks, timedelta())
print(total_time)  # 1:30:00

# How to sum text
words = ["Hello", "World"]
# print(sum(words, ""))
# TypeError: sum() can't sum strings [use ''.join(seq) instead]

print("".join(words))  # HelloWorld
