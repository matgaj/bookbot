from stats import count_words, count_char_appearances

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = count_words(book)
    char_appearances = count_char_appearances(book)
    print(f"{num_words} words found in the document")
    print(char_appearances)


main()