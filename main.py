#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password_letters = ""
number_of_letters = 0
for letter in letters:
    if number_of_letters < nr_letters:
        password_letters += random.choice(letters)
        number_of_letters += 1

password_symbols = ""
number_of_symbols = 0
for symbol in symbols:
    if number_of_symbols < nr_symbols:
        password_symbols += random.choice(symbols)
        number_of_symbols += 1

password_numbers = ""
number_of_numbers = 0
for number in numbers:
    if number_of_numbers < nr_numbers:
        password_numbers += random.choice(numbers)
        number_of_numbers += 1
# print(password_letters + password_symbols + password_numbers)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = list(password_letters + password_symbols + password_numbers)
random.shuffle(password)
final_password = ""
for a in password:
    final_password += a
print("Your password is: " + final_password)

# Another method
# password = []
# for letter in range(1, nr_letters + 1):
#   password.append(random.choice(letters))

# for symbol in range(1, nr_symbols + 1):
#   password.append(random.choice(symbols))

# for number in range(1, nr_numbers + 1):
#   password.append(random.choice(numbers))

# random.shuffle(password)
# final_password = ""
# for char in password:
#   final_password += char

# print("Your password is: " + final_password)
