import time
import math

# Defining the decorator
def intime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f"⏱️ Function '{func.__name__}' executed in {duration:.6f} seconds")
        return result
    return wrapper

# Applying the decorator
@intime
def compute_log(value, base='e'):
    if value <= 0:
        return "Error: Logarithm is undefined for non-positive numbers."
    
    try:
        if base == 'e':
            return math.log(value)
        elif isinstance(base, (int, float)) and base > 0 and base != 1:
            return math.log(value, base)
        elif base == 10:
            return math.log10(value)
        else:
            return "Error: Invalid base."
    except Exception as e:
        return f"Error: {str(e)}"

print(compute_log(10))         # Natural log
print(compute_log(10, 10))     # Log base 10
print(compute_log(100, 2))     # Log base 2
print(compute_log(-5))         # Error

