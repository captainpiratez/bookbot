def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    print(count_characters(text))

def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lowered_text = text.lower()
    analyzed_text = {}
    for i in lowered_text:
        if i in analyzed_text:
            analyzed_text[i] += 1
        else:
            analyzed_text[i] = 1
    return analyzed_text

main()