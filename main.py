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

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(
        f"Found {count_words(get_book_text("books/frankenstein.txt"))} total words")
    print("----------- Character Count ----------")

    print_items(sorted_letter_count(get_letters_appearance(
        get_book_text("books/frankenstein.txt"))))

    print("============= END ===============")


main()
