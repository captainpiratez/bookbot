# BookBot 📚🤖

BookBot is a Python script that analyzes the text of a book and generates a detailed character frequency report.

## Features

- Reads and processes text files (books)
- Counts total word occurrences
- Analyzes character frequency distribution
- Generates sorted reports by character frequency

## Requirements

- Python 3.x

## Usage

```bash
python3 main.py <path_to_book>
```

Replace `<path_to_book>` with the path to your desired book text file.  
Example:

```bash
python3 main.py books/frankenstein.txt
```

The script will analyze the provided book file and output:
- Total word count
- Character frequency analysis (sorted by occurrence)

## Example Output

```
--- Begin report of books/frankenstein.txt ---
77986 words found in the document

The 'e' character was found 46043 times
The 't' character was found 30365 times
The 'a' character was found 26743 times
...
--- End report ---
```

## License

This project is open source and available for educational purposes.

## Contributing

Feel free to fork this repository and submit pull requests for any improvements!

### BookBot is my first [Boot.dev](https://www.boot.dev) project!
