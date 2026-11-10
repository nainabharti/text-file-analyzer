Text File Analyzer 📝

A beginner-friendly Python project that analyzes text files and provides useful statistics such as total lines, words, characters, unique words, and word frequency.

This project demonstrates core Python programming concepts, including file handling, data structures, functions, exception handling, and modular programming.

🚀 Features

- File Reading: Read and display the contents of a text file.
- Line Counting: Calculate the total number of lines.
- Word Counting: Calculate the total number of words.
- Character Counting: Count all characters, including spaces and punctuation.
- Unique Word Counting: Identify and count distinct words.
- Word Frequency Analysis: Calculate how many times each word appears.
- Top 5 Frequent Words: Display the five most frequently occurring words.
- Word Normalization: Convert words to lowercase and remove punctuation from word boundaries.
- Exception Handling: Handle missing files, permission errors, invalid directory paths, and decoding errors.
- Modular Programming: Organize the application into separate reusable functions.

🛠️ Technologies Used

- Python 3
- Built-in Python modules:
  - "string"

📁 Project Structure

text-file-analyzer/
│
├── main.py
│
├── test_files/
│   └── sample.txt
│
├── .gitignore
│
└── README.md

⚙️ Installation and Setup

1. Clone the repository

git clone https://github.com/nainabharti/text-file-analyzer.git

2. Navigate to the project directory

cd text-file-analyzer

3. Run the program

python main.py

No external Python packages are required.

💻 Usage

1. Run the Python program.
2. Enter the path of the text file when prompted.
3. The program reads and analyzes the file.
4. View the file statistics, word frequency, and top five most frequent words.

Example file path:

test_files/sample.txt

📊 Sample Output

===== TEXT FILE ANALYZER =====

Enter the path of the text file: test_files/sample.txt

===== FILE STATISTICS =====
Total Lines: 3
Total Words: 8
Total Characters: 45
Unique Words: 5

===== WORD FREQUENCY =====
python: 3
is: 2
easy: 1
to: 1
learn: 1

===== TOP 5 MOST FREQUENT WORDS =====
python: 3
is: 2
easy: 1
to: 1
learn: 1

Note: The sample output is illustrative. Actual results depend on the contents of the input file.

📚 Concepts Learned

Through this project, I practised:

- Variables and data types
- Strings and string methods
- Lists, sets, and dictionaries
- Conditional statements and loops
- Functions and return statements
- File handling using "open()"
- Exception handling using "try-except"
- Dictionary operations
- Lambda functions and sorting
- Modular programming

🔮 Future Scope

- Add support for PDF and Word documents.
- Generate downloadable analysis reports.
- Add graphical user interface (GUI).
- Allow users to ignore common stop words.
- Improve punctuation handling and text preprocessing.
- Support analysis of multiple files.

👩‍💻 Author

Naina Bharti

- GitHub: "@nainabharti" (https://github.com/nainabharti)

---

⭐ If you find this project useful, feel free to explore the repository!