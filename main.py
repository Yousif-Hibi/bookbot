import sys
from stats import *

def get_book_text(path) :
    with open(path) as f :
        file_contents= f.read()
    return file_contents

def print_result(path,book_text) : 
    num_words = number_of_word(book_text)
    print(f"Found {num_words} total words")
    array = dirctory_to_array(number_of_characters(book_text))
    for latter in array : 
        print(f"{latter['char']}: {latter['num']}") 

def main() :
    path = ""
    system_arguments = sys.argv
    print(len(system_arguments))
    if len(system_arguments) == 2 :
        path = sys.argv[1]
        print(path)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    book_text = get_book_text(path)
    print_result(path,book_text)

if __name__ == "__main__":
    main()  
