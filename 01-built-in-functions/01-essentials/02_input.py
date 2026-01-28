# ==========================================
# input()
# Syntax: input(prompt, /)
# Ref: https://docs.python.org/3/library/functions.html#input
# ==========================================

print("--- input() Function ---")

# 1. Basic
print("\n--- Basic Input ---")
name = input("Enter your name?: ")
print(f"Hello, {name}")

# 2. The "Type Trap"
print("\n--- The Type Trap Everything is string ---")
# input จะคืนค่าเป็น string เสมอ
age = input("Enter your age: ")
print(f"Your age {age}, Type: {type(age)}")

# 3. Input with Coversion (การรับค่าที่ถูกต้อง)
print("\n--- Input with Conversion ---")
# ครอบด้วย int() หรือ float() เพื่อแปลงข้อมูลที่ได้รับ
height = float(input("Enter you height (cm): "))
print(f"Your height is {height:.2f} cm")
print(f"Height type is now: {type(height)}")
