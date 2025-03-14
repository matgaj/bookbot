from stats import count_words, count_char_appearances, sort_char_by_num_appearance

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)
    num_words = count_words(book)
    char_appearances = count_char_appearances(book)
    # print(f"{num_words} words found in the document")
    # print(char_appearances)

    sorted_char_appearance = sort_char_by_num_appearance(char_appearances)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for k in sorted_char_appearance:
        if k["char"].isalpha():
            print(f"{k["char"]}: {k["num"]}")

    print("============= END ===============")

main()