# ==========================================
# abs() Function
# Syntax: abs(number)
# Ref: https://docs.python.org/3/library/functions.html#abs
# ==========================================

print("--- 1. Integer ---")
print(f"abs(-10) -> {abs(-10)}")

print("\n--- 2. Floating Point ---")
print(f"abs(-45.555) -> {abs(-45.555)}")

print("\n--- 3. Complex Number ---")
a = 10
b = 20
z = complex(a, b)  # 10 + 20j
print(f"abs() magnitude {z} is {abs(z)} ")


print("\n--- 4. Magic Methods (__abs__) ---")
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return (self.x**2 + self.y**2) ** 0.5


v = Vector(3, 4)
print(f"Vector(3,4) -> {abs(v)} ")
