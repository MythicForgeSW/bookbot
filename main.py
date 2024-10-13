def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    print(f"{word_count} words were found in this document!")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(book_text):
    split_text = book_text.split()
    length_of_text = len(split_text)
    return length_of_text

main()