numbers = []

try:
    with open('numbers.txt', 'r') as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            try:
                number = int(line)
                numbers.append(number)
            except ValueError:
                print(f"⚠️ Warning: Line {line_number} - '{line}' is not a valid number. Skipping.")
except FileNotFoundError:
    print("❌ Error: File 'numbers.txt' not found.")

print(f"✅ Successfully read {len(numbers)} valid numbers:")
print(numbers)