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