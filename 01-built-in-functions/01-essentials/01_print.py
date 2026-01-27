# ==========================================
# print()
# Syntax: print(*objects, sep=' ', end='\n', file=None, flush=False)
# Print objects to the text stream file, separated by sep and followed by end. sep, end, file, and flush, if present, must be given as keyword arguments.
# Ref: https://docs.python.org/3/library/functions.html#print
# ==========================================

print("--- print() Function ---")

# 1. Basic
print("\n--- Basic print ---")
print("Hello, World!")  # Output: Hello, World!
print("One", "Two", "Three")  # Output: One Two Three

# 2. Separator(ตัวคั่น):
print("\n--- print with separator ---")
print("One", "Two", "Three", sep=" | ")


# 3. end of line (end)
print("\n--- print with end of line ---")
print("Loading", end="...")
print("Done!")
# Output: Loading...Done!

# 4. f-string (The Best Way to Format)
print("\n--- print with f-string ---")
name = "Python"
version = 1.13
print(f"I'm learning {name} version {version}")

# 5. f-string Debugging Trick
print("\n--- print with f-string for debugging")
score = 100
print(f"{score=}")  # Output: score=100

# 6. Decimal Formatting
print("\n--- print with decimal formatting---")
pi = 3.14159256
print(f"Pi value: {pi:.2f}")  # Output: Pi value: 3.14
