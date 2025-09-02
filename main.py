import sys

from stats import count_words, count_characters, sort_characters

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    text_contents = get_book_text(sys.argv[1])
    num_words = count_words(text_contents)
    num_caracters = count_characters(text_contents)
    sorted_characters = sort_characters(num_caracters)

    print("============ BOOKBOT ============")
    print("Analyzing book found at ")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_characters:
        item_character = item["char"]
        item_character_num = item["num"]

        if item_character.isalpha():
            print(f"{item_character}: {item_character_num}")

    print("============= END ===============")


main()
