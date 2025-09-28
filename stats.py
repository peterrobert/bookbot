def count_words(text):
    stripped_text = text.strip().split()
    return len(stripped_text)


def get_letters_appearance(text):
    text_lower_case = text.lower()
    text_list = list(text_lower_case)

    letter_count = {}

    for letter in text_list:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    return letter_count


def sort_on(items):
    return items["num"]


def sorted_letter_count(characters):
    items_array = []
    for key, value in characters.items():
        if (key.isalpha()):
            new_dict = {"char": key, "num": value}
            items_array.append(new_dict)

    items_array.sort(reverse=True, key=sort_on)

    return items_array
