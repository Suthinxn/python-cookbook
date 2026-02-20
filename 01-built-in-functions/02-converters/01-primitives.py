# ==========================================
# Primitive Converters: int(), float(), str(), bool()
# ฟังก์ชั่นสำหรับแปลงชนิดของข้อมูลพื้นฐาน
# ==========================================

print("--- Primitive Converters ---")

# ==========================================
# 1. int() - แปลงเป็นจำนวนเต็ม
# Syntax: int(string, /, base=10)
# Ref: https://docs.python.org/3/library/functions.html#int
# ==========================================

print("\n--- 1. int() ---")
print(f"String to int: {int('100')} (Type: {type(int('100'))})")
print(f"Float to int: {int(3.99)}")
# Advanced
print(f"Binary string to int: {int('01001000', base=2)}")  # 72
print(f"Hex string to int: {int('FF', base=16)}")  # 255

# ==========================================
# 2. float() - แปลงเป็นทศนิยม
# Syntax: float(number=0.0, /)
# Ref: https://docs.python.org/3/library/functions.html#float
# ==========================================

print("\n--- 2. float() ---")
print(f"String to float: {float('3.14')}")
print(f"Int to float: {float(5)}")
# Advanced
print(f"Infinity: {float('inf')}")  # ใช้กำหนดค่าเริ่มต้นให้มากกว่าทุกจำนวนบนโลก
print(f"Negative Inf: {float('-inf')}")
print(f"Not a Number: {float('nan')}")

# ==========================================
# 3. str() - แปลงทุกสิ่งเป็นข้อความ
# Syntax: str(object, *, errors)
# Ref: https://docs.python.org/3/library/functions.html#func-str
# ==========================================

print("\n--- 3. str() ---")
num = 404
text = "Error: " + str(num)  # ต้องแปลงเป็น string ก่อน
print(text)

# แปลง List เป็น String
my_list = [1, 2, 3]
list_str = str(my_list)
print(f"List as String: {list_str} (Length: {len(list_str)})")  # นับช่องว่างด้วย(" ")

# ==========================================
# 4. bool() - แปลงเป็นค่าความจริง (True / False)
# Syntax: bool(object=False, /)
# Ref: https://docs.python.org/3/library/functions.html#bool
# ข้อมูลที่ "ว่างเปล่า" หรือ "เป็นศูนย์" จะได้ False เสมอ
# ==========================================

print("\n--- 4. bool() (True/False) ---")
print(f"bool(0): {bool(0)}")
print(f"bool(''): {bool('')}")
print(f"bool([]): {bool([])}")
print(f"bool(None): {bool(None)}")

print(f"bool(1): {bool(1)}")
print(f"bool(-5) {bool(-5)}")
print(f"bool(' ') {bool(' ')}")
print(f"bool('False'): {bool('False')}")
