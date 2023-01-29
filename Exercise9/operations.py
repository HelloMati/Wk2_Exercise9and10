var = input("Please enter a value: ")
numeric = False
print(var.upper())  # method returns a string where all characters are in upper case.
print(len(var))  # function returns the number of items in an object.
print(var.isdigit())  # method returns True if all the characters are digits, otherwise False.
print(var.isdecimal())  # method checks whether the string consists only decimals (0-9) or not.

for char in var:
    if char.isdigit():
        numeric = True
        break
print(numeric)

for char in var:
    if char.isdecimal():
        numeric = True
        break
print(numeric)
