# Take integer user input in Python

# ✅ Take user input integer value
user_input = int(input('Enter an integer: '))
print(user_input)

# ------------------------------------------------

# ✅ Take user input integer value with validation
try:
    user_input = int(input('Enter an integer: '))
    print(user_input)
except ValueError:
    print('Enter a valid integer')