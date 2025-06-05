# Challenge Day 4
# Check if a user-entered number is prime

# Prime Number Detective 🔎

number = int(input("Enter a number to check if it's prime: "))

if number <= 1:
    print(f"{number} is not prime (prime numbers are greater than 1).")
else:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            print(f"🔍 Detective found a clue: {i} divides {number}!")
            is_prime = False
            break  # We found a divisor, so no need to check further!
        else:
            continue  # Skip to the next number.

    if is_prime:
        print(f"{number} is a prime number! 🎉 Case closed.")
    else:
        print(f"{number} is not a prime number. Better luck next time, detective.")
