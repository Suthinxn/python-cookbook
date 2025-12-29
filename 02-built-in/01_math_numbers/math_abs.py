# ===== abs() =====
# ? Syntax: abs(number)
# Integer
print(abs(-10))

# Floating-point
print(abs(-45.555))

# Complex number
a = 10
b = 20
z = complex(a, b)  # 10 + 20j
print(f"abs magnitude {z} is {abs(z)} ")


# Magic Methods
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return (self.x**2 + self.y**2) ** 0.5


v = Vector(3, 4)
print(abs(v))
