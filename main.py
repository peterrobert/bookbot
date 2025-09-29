import sys

from stats import count_words
from stats import get_letters_appearance
from stats import sorted_letter_count


def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def print_items(sorted_array):
    for item in sorted_array:
        print(f"{item["char"]}: {item["num"]}")


def main():
   if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(
        f"Found {count_words(get_book_text(book_path))} total words")
    print("----------- Character Count ----------")

    print_items(sorted_letter_count(get_letters_appearance(
        get_book_text(book_path))))

    print("============= END ===============")


main()
