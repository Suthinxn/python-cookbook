# ==========================================
# round() Function
# Syntax: round(number, ndigits=None)
# ==========================================

print("--- 1. The Floating Point Trap (IEEE 754) ---")
print(f"round(2.67, 2) -> {round(2.675, 2)}")
print(round(2.635, 2))

print(round(2.675, 2))  # 2.67
# 2.67499999999999982236
# print(f"{2.675:.20f}")
print(round(2.775, 2))  # 2.77

# Banker’s Rounding (Round Half to Even)
# Binary Float

print("\n--- 2. Banker's Rounding (Round Half to Even) ---")
# Rule: If standard rounding end in .5, round to the nearest EVEN number.
# จะปัดเลขที่ลงท้ายด้วย .5 ไปหาเลขคู่
# Python (and most languages) follows IEEE 754 standard
# Computers store floats in Binary, not Decimal.
print(round(2.5))  # return 2
print(round(3.5))  # return 4
print(round(4.5))  # return 4


print("\n--- 3. Negative ndigits (Rounding Integers) ---")
num = 2025

# -1: Round to nearest 10 (Tens place / หลักสิบ)
print(round(num, -1))  # Return 2020

# -2: Round to nearest 100 (Hundreds place / หลักร้อย)
print(round(num, -2))  # Return 2000

# -3: Round to nearest 1000 (Thousands place / หลักพัน)
print(round(num, -3))  # 2000 (Closer to 2000 than 3000)

print("\n--- 4. Magic Methods (__round__) ---")


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __round__(self, ndigits=None):  # Magic Methods
        return round(self.price, ndigits)

    # def __repr__(self):
    #     return f"Product({self.name}, {self.price})"


my_item = Product("Gamimg Mouse", 99.555)

print(f"Original: {my_item}")
print(f"Rounded (2 digits): {round(my_item, 2)}")  # 99.56
print(f"Rounded (Integer): {round(my_item)}")  # 100
