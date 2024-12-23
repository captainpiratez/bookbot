def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = get_chars_sorted_list_dict(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    for char_dict in chars_sorted_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")

    print("--- End report ---")

    
def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    analyzed_text = {}
    for i in text:
        lowered = i.lower()
        if lowered.isalpha():
            if lowered in analyzed_text:
                analyzed_text[lowered] += 1
            else:
                analyzed_text[lowered] = 1
    return analyzed_text


def get_chars_sorted_list_dict(dict):
    chars_list = []
    for char, count in dict.items():
        chars_list.append({"char": char, "num": count})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list


def sort_on(dict):
    return dict["num"]


main()