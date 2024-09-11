import os

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

def get_dict(book):
    char_dic = {}
    words_in_book = book.split()
    seen = []

    for word in words_in_book:
        for char_key in word:
            char_key = char_key.lower()
            if char_key in seen:
                char_dic[char_key] += 1
            else:
                char_dic[char_key] = 1
                seen.append(char_key)
                
    return char_dic

def sort_book_dict(book_dict):
    new_book_dict = {}
    for key in book_dict:
        # if ord(key) in range(ord("a"), ord("z")+1):
        #     new_book_dict[key] = book_dict[key]
        if key.isalpha():
            new_book_dict[key] = book_dict[key]
    book_dict = {key: book_dict[key] for key in sorted(book_dict)}
    book_dict = new_book_dict 

    return book_dict

def print_book_dict(book_dict):
    for key, value in book_dict.items():
        print(f"{key}: {value}")

    return None

def main():
    frankenstein_book_path = 'books/frankenstein.txt'
    frankenstein_book = read_book(frankenstein_book_path)
    frankenstein_char_dict = get_dict(frankenstein_book)
    frankenstein_char_dict = sort_book_dict(frankenstein_char_dict)
    print_book_dict(frankenstein_char_dict)
    

if __name__ =="__main__":
          main()
