from stats import get_num_words
from stats import get_each_char

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    get_num_words(get_book_text("books/frankenstein.txt"))
    num_of_chars = get_each_char(get_book_text("books/frankenstein.txt"))
    for char in num_of_chars:
        print(f"'{char}': {num_of_chars[char]}")
main()    