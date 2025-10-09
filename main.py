import sys
from stats import *

print(sys.argv)
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]



def main():
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_char(text)
    sorted = sort_dict(num_chars)



    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print('----------- Word Count ----------')
    print(f"Found {num_words} total words")
    print('--------- Character Count -------')
    for i in sorted:
        print(f"{i['char']}: {i['count']}")
    print("============= END ===============")
main()
