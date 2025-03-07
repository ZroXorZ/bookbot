import sys
from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) < 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit()

    txt = get_book_text(sys.argv[1])
    words_count = num_words(txt)
    char_count = sort_dict(txt)

    print ("============ BOOKBOT ============")
    print ("Analyzing book found at books/frankenstein.txt...")
    print ("----------- Word Count ----------")
    print (f"Found {words_count} total words")
    print ("--------- Character Count -------")
    for i in char_count:
        print (f"{i['char']}: {i['count']}")
    print ("============= END ===============")

main()