# ==========================================
# len()
# Syntax: open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# Open file and return a corresponding file object. If the file cannot be opened, an OSError is raised. See Reading and Writing Files for more examples of how to use this function.
# Ref: https://docs.python.org/3/library/functions.html#open
# ==========================================


# TODO: Dynamic Path
# from pathlib import Path

print("--- open() Function ---")

# 1. Writing to a file (Mode 'w' - Write)
# 'w' สร้างไฟล์ใหม่ ถ้ามีไฟล์เดิมอยู่จะทำการลบทิ้งไฟล์เดิมก่อน
print("\n--- 1. Writing (mode='w') ---")
path = "D:/suthinxn/learning/me/code_practice/python-cookbook/01-built-in-functions/01-essentials/sample.txt"
# ใช้ได้ทั้ง 2 แบบ
# path = r"D:\suthinxn\learning\me\code_practice\python-cookbook\01-built-in-functions\01-essentials\sample.txt"
with open(
    path,
    "w",
    encoding="utf-8",
) as f:
    f.write("Hello, Python!\n")
    f.write("บรรทัดที่ 2 (ทดสอบภาษาไทย)")

print("-> Created and write to 'sample.txt'")


# 2. Appending to a file (Mode 'a' - Append)
# 'a' นำข้อมูลไปต่อท้ายโดยไม่ลบข้อมูลเก่า
print("\n--- 2. Appending (mode='a') ---")
with open(path, "a", encoding="utf-8") as f:
    f.write("\nLine 3: Append text.\n")
print("-> Appended new line to 'sample.txt")


# 3. Reading a file (Mode 'r' - Read)
# 'r' คือค่าเริ่มต้น (Default)
print("\n--- 3. Reading (mode='r') ---")
with open(path, "r", encoding="utf-8") as f:
    # f.read() จะดึงข้อมูลออกมาเป็น string ก้อนเดียว
    content = f.read()
    print("--- File Content ---")
    print(content)
    print("--------------------")

# 4. Reading By Line (เหมาะสำหรับไฟล์ขนาดใหญ่)
print("\n--- 4. Reading Line by Line ---")
with open(path, "r", encoding="utf-8") as f:
    for line_number, line in enumerate(f, start=1):
        print(f"Line {line_number}: {line.strip()}")

# 5. Handle Error
print("\n--- 5. Handling Missing Files ---")
try:
    with open("secret_file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: The file 'secret_file.txt.' does not exist!")

# 6. Advanced Modes (x, b, +)
# Mode: 't' - Text Mode อันนี้จะเป็นโหมด Default อยู่แล้ว
# เวลาใช้โหมด "r", "w" python จะเติม t ให้แล้ว "rt", "wt"
print("\n--- 6. Advanced File Modes (x, b, +) ---")

# --- Mode 'x' (Exclusive Create) ---
# สร้างใหม่เท่านั้นหากมีไฟล์ชื่อนี้อยู่แล้วจะ Error ป้องกันการ Overwrite
path = "D:/suthinxn/learning/me/code_practice/python-cookbook/01-built-in-functions/01-essentials/my_secure_file.txt"
print("\n--- Mode 'x' : Exclusive Create ---")
try:
    with open(path, "x", encoding="utf-8") as f:
        f.write("password is password!")
    print("-> Create file successfully.")
except FileExistsError:
    print("-> Error: Cannot create file")

# --- Mode 'b' (Binary Mode) ---
print("\n--- Mode 'b' : Binary ---")
path = "D:/suthinxn/learning/me/code_practice/python-cookbook/01-built-in-functions/01-essentials/binary_file.bin"
# จะใชั "wb" (Write Binary) และไม่ระบุ encoding
with open(path, "wb") as f:
    f.write(b"\x48\x65\x6c\x6c\x6f")  # รหัสไบนารีของคำว่า Hello
    # https://www.rapidtables.com/convert/number/hex-to-ascii.html
    # Python จะแปลงจาก hexadecimal --> binary อีกที
print("-> Wrote binary data to 'binary_file.bin'")

# "rb" (Read Binary)
with open(path, "rb") as f:
    binary_data = f.read()
    print(f"-> Read from binary: {binary_data} (Type: {type(binary_data)})")

# --- Mode '+' (Update Mode) ---
print("\n--- Mode '+' : Read & Write (r+) ---")
# r+ สามารถอ่านและเขียนได้
path = "D:/suthinxn/learning/me/code_practice/python-cookbook/01-built-in-functions/01-essentials/sample.txt"
with open(path, "r+", encoding="utf-8") as f:
    content = f.read()
    f.write("\nPython coding!")
print("-> Read and updated 'sample.txt' using 'r+'")
