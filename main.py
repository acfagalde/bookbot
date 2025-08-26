import sys
from stats import word_count
from stats import letter_count

def get_book_text(filepath):
    with open(filepath) as f:
        global file_contents 
        file_contents = f.read()
    return(file_contents)

def main():
    get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    word_count(file_contents)
    print("--------- Character Count -------")
    letter_count(file_contents)
    print("============= END ===============")

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()
