var = input("Please enter a value: ")  # input() prompts the console with the string given and takes user input
print(f'Print of the input all in upper case: {var.upper()}')  # str.upper() returns the str with all upper case
print(f'Number of characters: {len(var)}')  # function returns the number of items in an object.
# Difference between .isdigit() and .isdecimal() explained below
print(f'Are all characters numbers? Using .isdigit(): {var.isdigit()}')  # str.isdigit() returns True is all numbers
print(f'Are all characters numbers? Using .isdecimal():{var.isdecimal()}')  # str.isdigit() returns True is all numbers

# Using loop to check every character of the input and assess if is a number
numeric = False
for char in var:
    if char.isdigit():
        numeric = True
        break  # No need to continue checking more characters as we already found a number
print(f'Does it contain any numeric characters? isdigit(): {numeric}')

for char in var:
    if char.isdecimal():
        numeric = True
        break  # No need to continue checking more characters as we already found a number
print(f'Does it contain any numeric characters? isdecimal(): {numeric}')


# COMMENT: difference between isdigit() VS isdecimal()
# The main difference between them is the type of character they will be able to check.

# isdigit() returns True if the string is formed by:
# → Base 10 numbers (0123456789)
# → Superscripts (2²)
# Will return False for: Roman numerals and fractions in unicode and for whitespaces or decimals.

# isdecimal() returns True if the string is formed by a Base 10 number. Any other string (e.g. fractions) is False.

print("\nTrying out differences between isdigit() and isdecimal()")
print(f'20 → isdigit: {"20".isdigit()} // isdecimal: {"20".isdecimal()}')
print(f'2² → isdigit: {"2²".isdigit()} // isdecimal: {"2²".isdecimal()}')
