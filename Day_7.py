# Opening the file
with open('sample.txt', 'r') as file:
    text = file.read()

# Splitting text into words
words = text.split()

# Creating a dictonary to store word frequencies
word_freq = {}

# Looping through the words
for word in words:
    # Removing punctuation and converting to lowercase
    word = word.strip('.,!?()"').lower()
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Printing the result
for word, freq in word_freq.items():
    print(f'{word}: {freq}')