from stats import count, characters, sorting
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    
    book = get_book_text(path)
    result = count(book)
    dictionary = characters(book)
    #print(result)
    
    #print(dictionary)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count(path)} total words")
    print("--------- Character Count -------")
    to_print = sorting(path)
    print(to_print)
    print("============= END ===============")
    
    
if __name__ == "__main__":
    main()