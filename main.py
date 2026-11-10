import string

print("===== TEXT FILE ANALYZER =====")

# Take file path from user
file_path = input("Enter the path of the text file: ")

# Display entered file path
print(f"\nFile path entered: {file_path}")

try:
    # Read the text file
    with open(file_path, "r") as file:
        content = file.read()

    # Check whether the file is empty
    if not content.strip():
        print("\nThe file is empty. No text available for analysis.")
    else:
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

# Handle different file-related errors
except FileNotFoundError:
    print("\nError: File not found, Please check the file path.")
except PermissionError:
    print("\nError: You don't have permission to access this file.")
except IsADirectoryError:
    print("\nError: You entered a directory path instead of a file path.")
except UnicodeDecodeError:
    print("\nError: Unable to decode the file. Please use a UTF-8 text file.")
except OSError as error:
    print(f"\nFile access error: {error}")