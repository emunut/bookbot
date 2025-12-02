# main.py

import sys

from stats import count_words, count_chars, sort_chars_by_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    with open(book_path, "r", encoding="utf-8") as f:
        book_contents = f.read()

    word_count = count_words(book_contents)
    char_counts = count_chars(book_contents)
    # Get the sorted list of character counts
    sorted_char_list = sort_chars_by_count(char_counts)

    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    # Iterate through the sorted list and print each character's count
    for item in sorted_char_list:
        char = item["char"]
        count = item["num"]
        print(f"{char}: {count}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
