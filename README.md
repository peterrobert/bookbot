# BookBot 📚

BookBot is a simple Python project that reads a text file (a “book”), analyzes it, and provides summary statistics such as word counts and character frequency. This was built as a learning project (from Boot.dev) to practice file I/O, string parsing, and basic data analysis in Python.

BookBot is my first [Boot.dev](https://www.boot.dev) project!

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Sample Output](#sample-output)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- Read and load the full text of a book from a `.txt` file
- Count total number of words
- Compute frequency of each character (case-insensitive)
- Print a readable report with the top-n frequent characters
- (Optionally) handle multiple files / combine stats

---

## Project Structure

.
├── books/ # Folder where .txt books are stored
├── main.py # Entry point — orchestrates reading & analysis
├── stats.py # Functions for counting words, characters, etc.
├── .gitignore
└── README.md

Here’s what each part does:

- `main.py` — loads the book(s), invokes functions from `stats.py`, prints the summary
- `stats.py` — contains helper functions such as `get_text()`, `count_words()`, `char_frequencies()`
- `books/` — you drop your `.txt` files here (e.g. `frankenstein.txt`)
- `.gitignore` — excludes the `books/` directory (so you don’t accidentally commit full books)

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/peterrobert/bookbot.git
   cd bookbot
   ---Optional---
    python3 -m venv venv
    source venv/bin/activate   # on Linux/macOS
    venv\Scripts\activate      # on Windows
   ```
