# bookbot
This project is a clean, command-line tool designed to perform a static analysis of text files—perfect for when you need to know exactly how many times an author used the letter  instead of actually reading the book.

Overview
The Book Analyzer processes a text file to provide two primary insights:

Total Word Count: A quick tally of every word in the document.

Character Frequency: A sorted list of every alphabetical character found in the text, ranked from most frequent to least frequent.

How to Use
To run the analyzer, use the following command in your terminal:

Bash
python3 main.py <path_to_book>
Example
Bash
python3 main.py books/frankenstein.txt
Note: If you forget to provide a file path, the script will politely remind you of the correct usage and exit.

Features
Case-Insensitive Counting: The analyzer treats "A" and "a" as the same character to ensure accuracy.

Alphabetical Focus: The report automatically filters out numbers, spaces, and punctuation, focusing only on the letters of the alphabet.

Sorted Results: Characters are displayed in descending order of frequency, making it easy to identify the most common letters.

Technical Breakdown
main.py
This is the entry point of the application. It handles:

Argument Parsing: Uses sys.argv to capture the file path from the command line.

File Handling: Reads the raw text from the specified path.

Output Formatting: Orchestrates the printing of the final report to the console.

stats.py
This module contains the "brains" of the operation:

number_of_word: Splits the string into a list to calculate the total word count.

number_of_characters: Iterates through the text to build a frequency dictionary of lowercase characters.

dirctory_to_array: Converts the dictionary into a list of dictionaries and sorts them using a helper function.


