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

# Count total words
words = content.split()
total_words = len(words)

# Count total characters
total_characters = len(content)

# Display total lines
print("\n===== FILE STATISTICS =====")
print(f"Total Lines: {total_lines}")
print(f"Total Words: {total_words}")
print(f"Total Characters: {total_characters}")