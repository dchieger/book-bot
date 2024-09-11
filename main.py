import os

frankenstein_book = 'books/frankenstein.txt'

def read_book(book_path):
    with open(book_path) as book:
        book_contents = book.read()

    return book_contents

def count_words(book):
    words_in_book = book.split()
    word_count = 0
    for word in words_in_book:
        word_count += 1

    return word_count

def count_char(c, book):
    words_in_book = book.split()
    ccount = 0
    looking_for = c
    book_chars
    for word in words_in_book:
        for c in word:
            c = c.lower()
            if c == looking_for:
                if c in
    return ccount

def main():
    frankenstein = read_book(frankenstein_book)
    fb_char_count = count_words(frankenstein)

    print(fb_char_count)
    print(f"this many p\'s {count_char("p", frankenstein)}")
    print(f"this many r\'s {count_char("r", frankenstein)}")
    print(f"this many o\'s {count_char("o", frankenstein)}")

if __name__ =="__main__":
          main()
