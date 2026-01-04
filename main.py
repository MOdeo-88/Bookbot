from stats import (get_num_words, get_num_char, sorter)
import sys

def main():
    try:
        text = get_book_text(sys.argv[1])
        num_words = get_num_words(text)
        num_char = get_num_char(text)
        sorted_chars= sorter(num_char)
        print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...")
        print(f"----------- Word Count ----------\nFound {num_words} total words")
        print(f"--------- Character Count -------")
        for char , count in sorted_chars.items():
            if char.isalpha():
                print(f"{char}: {count}")    

    except IndexError :
        print("you need a file path argument \n Usage: python3 main.py <path_to_book>")
        raise sys.exit(1)
    except Exception as x:
        print(x)
def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)



main()