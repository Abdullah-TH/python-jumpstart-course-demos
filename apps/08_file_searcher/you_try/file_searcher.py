import os
import collections

SearchResult = collections.namedtuple("SearchResult", "file, line, text")


def main():
    print_header()

    folder = get_folder_from_user()
    if not folder:
        print("Sorry, we can't search with no folders")
        return

    text = get_search_text_from_user()
    if not text:
        print("Sorry, we can't search for nothing!")
        return

    matches = search_folders(folder, text)
    for match in matches:
        print("---------MATCH--------")
        print(f"file: {match.file}")
        print(f"line: {match.line}")
        print(f"text: {match.text.strip()}")
        print()


def print_header():
    print('---------------------------')
    print('     FILE SEARCH APP')
    print('---------------------------')


def get_folder_from_user():
    folder = input("What folder you want to search in? ")
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input("What are you searching for [single phrases only]? ")
    return text


def search_folders(folder, text):
    items = os.listdir(folder)
    for item in items:
        item_path = os.path.join(folder, item)
        if os.path.isdir(item_path):
            yield from search_folders(item_path, text)
        else:
            yield from search_file(item_path, text)


def search_file(path, text):
    text = text.lower()
    with open(path, 'r', encoding='utf-8') as file:
        line_number = 0
        for line in file:
            line_number += 1
            if line.lower().find(text) >= 0:
                yield SearchResult(file=path, line=line_number, text=line)


if __name__ == '__main__':
    main()
