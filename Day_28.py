import time

def greet_decorator(function):
    """
    Decorator that prints a greeting, the result of the function,
    a thank-you message, execution time, and a separator line.
    """
    def wrapper(*args, **kwargs):
        print("Good Evening")
        start_time = time.time()

        result = function(*args, **kwargs)

        end_time = time.time()
        print("Thank you")
        print(f"Execution time: {end_time - start_time:.6f} seconds")

        # Separator line for better output readability
        print("-" * 18)

        return result

    return wrapper

@greet_decorator
def say_hello():
    """Prints a simple greeting message."""
    print("Hello, world!")

@greet_decorator
def add_numbers(a, b):
    """Adds two numbers and prints the result."""
    print(a + b)

# Function calls
say_hello()
add_numbers(2, 3)