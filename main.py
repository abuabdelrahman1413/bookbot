def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    print(count_words(text))
    print(count_chars(text))


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_chars(text):
    text = text.lower()
    dict_of_chars = {}
    for char in text:
        if char in dict_of_chars:
            dict_of_chars[char] += 1
        else:
            dict_of_chars[char] = 1
    return dict_of_chars


main()
