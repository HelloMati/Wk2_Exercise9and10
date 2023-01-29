var = input("Please enter a value: ")
print(f'Print of the input all in upper case: {var.upper()}')  # method returns a string where all characters are in upper case.
print(f'Number of characters: {len(var)}')  # function returns the number of items in an object.
print(f'Are all characters numbers? Using .isdigit(): {var.isdigit()}')  # method returns True if all the characters are digits, otherwise False.
print(f'Are all characters numbers? Using .isdecimal():{var.isdecimal()}')  # method checks whether the string consists only decimals (0-9) or not.

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

### COMMENT: difference between isdigit() VS isdecimal()

