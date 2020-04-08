"""
The journal module consists of 4 functions
load(name)
save(name, journal_data)
get_full_path_name(name)
add_entry(text, journal_data)
"""
import os


def load(name):
    """
    Load the journal data from a file and create a list of texts
    that represents the journal

    :param name: name of the journal file
    :return: a list of text represents the journal
    """
    filename = get_full_path_name(name)
    data = []

    if os.path.exists(filename):
        with open(filename) as file:
            for entry in file.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    """
    Save the journal_data to a file 'name'
    :param name: name of the file to save the journal data
    :param journal_data: the journal data as a list of text
    :return: None
    """
    filename = get_full_path_name(name)
    print(f'..... saving to {filename}')

    with open(filename, 'w') as file:
        for entry in journal_data:
            file.write(entry + '\n')


def get_full_path_name(name):
    """
    Get the full path of the file 'name'

    :param name: the name of the file
    :return: full path of the file 'name'
    """
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename


def add_entry(text, journal_data):
    """
    Add text entry to the journal_data

    :param text: text to add to the journal
    :param journal_data: the journal data as a list of text
    :return: None
    """
    journal_data.append(text)
