def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print(chars_dict)


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


def get_sorted_dict(dict):
    return dict.sort()


main()