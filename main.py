def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    character_amount = get_letter_count(book_text)
    generate_report(book_path, word_count, character_amount)

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

# This function generates a report for the word count and character counts
def generate_report(book_path, word_count, character_amount):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")

    # Sort the dictionary by values in descending order to get the most frequent characters first
    sorted_characters = sorted(character_amount.items(), key=lambda x: x[1], reverse=True)

    for char, count in sorted_characters:
        print(f"The '{char}' character was found {count} times")

    print("--- End Report ---")


main()