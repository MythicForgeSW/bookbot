def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    character_dictionary = get_letter_count(book_text)
    print(character_dictionary)

# This function reads the document at the path for text
def get_book_text(path):
    with open(path) as f:
        return f.read()

# This function counts the number of words in the text
def get_word_count(book_text):
    split_text = book_text.split()
    length_of_text = len(split_text)
    return length_of_text

# This function counts how many letters show up in the text
def get_letter_count(book_text):
    lowercase_text = book_text.lower()
    character_count = {}

    for letter in lowercase_text:
        if letter.isalpha(): # only count alphabetic characters
            if letter in character_count: # check if char is in the list
                character_count[letter] += 1 # add to counter
            else:
                character_count[letter] = 1 # add to list
    
    return character_count

main()