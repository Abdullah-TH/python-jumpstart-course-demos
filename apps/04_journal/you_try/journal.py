import os


def load(name):
    filename = get_full_path_name(name)
    data = []

    if os.path.exists(filename):
        with open(filename) as file:
            for entry in file.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    filename = get_full_path_name(name)
    print(f'..... saving to {filename}')

    with open(filename, 'w') as file:
        for entry in journal_data:
            file.write(entry + '\n')


def get_full_path_name(name):
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename


def add_entry(text, journal_data):
    journal_data.append(text)
