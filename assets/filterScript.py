#!/usr/bin/env python3

import json

INPUT_FILE = "dictionary_ru.json"
OUTPUT_FILE = "dictionary_ru_filtered.json"

MIN_LENGTH = 4
MAX_LENGTH = 18


def main():
    # Read dictionary
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        dictionary = json.load(f)

    # Filter by word length
    filtered = {
        word: definition
        for word, definition in dictionary.items()
        if MIN_LENGTH <= len(word) <= MAX_LENGTH
    }

    # Sort alphabetically
    filtered = dict(sorted(filtered.items(), key=lambda item: item[0]))

    # Save
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(
            filtered,
            f,
            ensure_ascii=False,
            indent=2
        )

    print(f"Original words : {len(dictionary):,}")
    print(f"Filtered words : {len(filtered):,}")
    print(f"Saved to       : {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
