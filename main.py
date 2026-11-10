import string

print("===== TEXT FILE ANALYZER =====")

# Take file path from user
file_path = input("Enter the path of the text file: ")

# Display entered file path
print(f"\nFile path entered: {file_path}")

# Read the text file
with open(file_path, "r") as file:
    content = file.read()

# Display file content
print("\nFile Content:")
print(content)

# Count total lines
lines = content.splitlines()
total_lines = len(lines)

# Split content into words
words = content.split()

# Normalize words
cleaned_words = []

for word in words:
    word = word.lower()
    word = word.strip(string.punctuation)
    cleaned_words.append(word)

# Count total words
total_words = len(cleaned_words)

# Count total characters
total_characters = len(content)

# Count unique words
unique_words = set(cleaned_words)
unique_word_count = len(unique_words)

# Calculate frequency of each word
word_frequency = {}

for word in cleaned_words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1 

# Find top 5 most frequent words
top_words = sorted(word_frequency.items(), key =lambda item: item[1], reverse = True)[:5]

# Display statistics
print("\n===== FILE STATISTICS =====")
print(f"Total Lines: {total_lines}")
print(f"Total Words: {total_words}")
print(f"Total Characters: {total_characters}")
print(f"Unique Words: {unique_word_count}")

# Display word frequency
print("\n===== WORD FREQUENCY =====")

for word, count in word_frequency.items():
    print(f"{word}: {count}")

# Display top 5 frequent words
print("\n===== TOP 5 MOST FREQUENT WORDS =====")
for word, count in top_words:
    print(f"{word}: {count}")