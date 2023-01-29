
# Create a variable to store the hard coded pin (pin to check against)
password = 1234

# Create a variable to store the inputted pin by the user
supplied_pin = input("Enter your PIN: ")


# Create a variable to store the maximum of attempts to check pin. Set it to 3
max_attempts = 3

# Use if/else statements to check failure/success
# while loop to account for the number of attempts
while max_attempts:
    if int(supplied_pin) == password:
        print('Correct PIN. Welcome to Sky bank.')
        break
    else:
        max_attempts -= 1
        print(f'Incorrect PIN. You have: {max_attempts} left')
        if max_attempts > 0:
            supplied_pin = input("Enter your PIN: ")
        else:
            print(f'You have no attempts left. Access blocked')
