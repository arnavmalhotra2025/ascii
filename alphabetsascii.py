# ASCII codes for all alphabet letters

# Uppercase letters A-Z
print("Uppercase letters and their ASCII codes:")
for letter in range(ord('A'), ord('Z') + 1):
    print(f"{chr(letter)}: {letter}")

print("\nLowercase letters and their ASCII codes:")
# Lowercase letters a-z
for letter in range(ord('a'), ord('z') + 1):
    print(f"{chr(letter)}: {letter}")