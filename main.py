def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    dict_of_chars = count_chars(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(text)} words in the document")
    for i in convert_dict_to_list_of_dicts(dict_of_chars):
        print(f"The '{i['key']}' character was found {i['num']} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    return len(text.split())


def count_chars(text):
    text = text.lower()
    dict_of_chars = {}
    for char in text:
        if char in dict_of_chars and char.isalpha():
            dict_of_chars[char] += 1
        else:
            if char.isalpha():
                dict_of_chars[char] = 1
    return dict_of_chars


def sort_on(d):
    return d["num"]


def convert_dict_to_list_of_dicts(dict):
    list = [{"key": key, "num": value} for key, value in dict.items()]

    list.sort(reverse=True, key=sort_on)

    return list


main()
