import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return f"{file_contents}"
       
from stats import word_count
from stats import count_characters
from stats import sort_characters

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        contents = word_count(text)
        characters = count_characters(text)
        sorted = sort_characters(characters)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {contents} total words")
        print("--------- Character Count -------")
        for char_dict in sorted:
            character = char_dict['char']
            count = char_dict['count']
            print(f'{character}: {count}')
        print("============= END ===============")

main()