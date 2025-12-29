# ===== round() =====
# ? Syntax: round(number, ndigits=None)
# Banker’s Rounding (Round Half to Even)

# Binary Float
# Python (and most languages) follows IEEE 754 standard
# Computers store floats in Binary, not Decimal.


print(round(2.675, 2))
print(round(2.775, 2))

print(round(2.5))  # return 2
print(round(3.5))  # return 4
print(round(4.5))  # return 4

# ndigits negative
print(round(2025, -1))  # Return 2020 (Ones place หลักหน่วย)
print(round(2025, -2))  # Return 2000 (Tens place หลักสิบ)


# Magic Methods
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __round__(self, ndigits=None):  # Magic Methods
        return round(self.price, ndigits)


my_item = Product("Gamimg Mouse", 99.555)

print(round(my_item, 2))
print(round(my_item))
