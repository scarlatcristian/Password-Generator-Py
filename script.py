import random

numbers = '1234567890'
symbols = "!@#$%^&*?"
letters = "abcdefghijklmnopqrstvwxqz" + "abcdefghijklmnopqrstvwxqz".upper()

print("Welcome to the PyPassword Generator!")
number_letters = int(
    input("How many letters would you like in your password\n"))
number_symbols = int(
    input("How many symbols would you like in your password\n"))
number_numbers = int(
    input("How many numbers would you like in your password\n"))

password = []

if number_letters > 0:
    for letter in range(number_letters):
        password.append(random.choice(letters))
if number_symbols > 0:
    for symbol in range(number_symbols):
        password.append(random.choice(symbols))

if number_numbers > 0:
    for number in range(number_numbers):
        password.append(random.choice(numbers))

random.shuffle(password)
password = "".join(password)

print(f"Your new password is: {password}")
