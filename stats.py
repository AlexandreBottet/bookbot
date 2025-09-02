def count_words(book):
    return len(book.split())


def count_characters(book):
    num_characters = {}

    for char in book:
        num_characters[char.lower()] = 0

    for char in book:
        num_characters[char.lower()] += 1

    return num_characters


def sort_on(items):
    return items["num"]


def sort_characters(characters):
    characters_sorted_list = []

    for char, num in characters.items():
        characters_dict = {}
        characters_dict["char"] = char
        characters_dict["num"] = num

        characters_sorted_list.append(characters_dict)

    characters_sorted_list.sort(reverse=True, key=sort_on)

    return characters_sorted_list
    

