import string


# 1. Function to read the text file
def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        return content

    except FileNotFoundError:
        print("\nError: File not found. Please check the file path.")

    except PermissionError:
        print("\nError: You don't have permission to access this file.")

    except IsADirectoryError:
        print("\nError: You entered a directory instead of a file.")

    except UnicodeDecodeError:
        print("\nError: Unable to decode the file. Please use a UTF-8 text file.")

    except OSError as error:
        print(f"\nFile access error: {error}")

    return None


# 2. Function to clean and normalize words
def clean_words(content):
    words = content.split()
    cleaned_words = []

    for word in words:
        word = word.lower()
        word = word.strip(string.punctuation)

        if word:
            cleaned_words.append(word)

    return cleaned_words


# 3. Function to analyze the text
def analyze_text(content):

    # Count total lines
    lines = content.splitlines()
    total_lines = len(lines)

    # Count total characters
    total_characters = len(content)

    # Clean words
    cleaned_words = clean_words(content)

    # Count total words
    total_words = len(cleaned_words)

    # Count unique words
    unique_words = set(cleaned_words)
    unique_word_count = len(unique_words)

    # Calculate word frequency
    word_frequency = {}

    for word in cleaned_words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    # Find top 5 most frequent words
    top_words = sorted(
        word_frequency.items(),
        key=lambda item: item[1],
        reverse=True
    )[:5]

    # Store all analysis results in a dictionary
    statistics = {
        "total_lines": total_lines,
        "total_words": total_words,
        "total_characters": total_characters,
        "unique_word_count": unique_word_count,
        "word_frequency": word_frequency,
        "top_words": top_words
    }

    return statistics


# 4. Function to display file statistics
def display_statistics(statistics):

    print("\n===== FILE STATISTICS =====")

    print(f"Total Lines: {statistics['total_lines']}")
    print(f"Total Words: {statistics['total_words']}")
    print(f"Total Characters: {statistics['total_characters']}")
    print(f"Unique Words: {statistics['unique_word_count']}")


# 5. Function to display word frequency
def display_word_frequency(statistics):

    print("\n===== WORD FREQUENCY =====")

    word_frequency = statistics["word_frequency"]

    for word, count in word_frequency.items():
        print(f"{word}: {count}")


# 6. Function to display top 5 frequent words
def display_top_words(statistics):

    print("\n===== TOP 5 MOST FREQUENT WORDS =====")

    top_words = statistics["top_words"]

    if not top_words:
        print("No words available for frequency analysis.")
        return

    for word, count in top_words:
        print(f"{word}: {count}")


# 7. Main function to control the program
def main():

    print("===== TEXT FILE ANALYZER =====")

    # Take file path from user
    file_path = input("Enter the path of the text file: ")

    # Display entered path
    print(f"\nFile path entered: {file_path}")

    # Read file
    content = read_file(file_path)

    # Check whether file was read successfully
    if content is None:
        return

    # Check whether file is empty
    if not content.strip():
        print("\nThe file is empty. No text available for analysis.")
        return

    # Display file content
    print("\nFile Content:")
    print(content)

    # Analyze text
    statistics = analyze_text(content)

    # Display results
    display_statistics(statistics)
    display_word_frequency(statistics)
    display_top_words(statistics)


# 8. Entry point of the program
if __name__ == "__main__":
    main()