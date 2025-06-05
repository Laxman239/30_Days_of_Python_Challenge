# Challenge Day 6
# Generate a random 8-character password

import random
import string

print("Do you need any password?")
print("Type Yes or No")

choice = input("Enter your choice: ").lower()

if choice == 'yes':
    # Generate an 8-character password with letters, digits, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=8))
    print("Here’s your password:", password)
elif choice == 'no':
    print("Have a good day!")
else:
    print("Invalid input. Please type Yes or No.")
