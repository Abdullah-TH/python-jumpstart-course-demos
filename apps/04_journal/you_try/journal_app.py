import journal


def main():
    print_header()
    run_event_loop()


def print_header():
    print('-------------------------------')
    print('        JOURNAL APP')
    print('-------------------------------')


def run_event_loop():
    print('What do you want to do with your journal?')
    command = None
    journal_name = 'default'
    journal_list = journal.load(journal_name)

    while command != 'x':
        command = input("[L]ist entries, [A]dd entries, E[x]it: ")
        command = command.lower().strip()
        if command == 'l':
            list_entries(journal_list)
        elif command == 'a':
            add_entry(journal_list)
        elif command != 'x':
            print(f"Sorry, we don't understand '{command}'")

    print('Done, goodbye')


def list_entries(journal_data):
    journal_data = reversed(journal_data)
    for index, entry in enumerate(journal_data):
        print(f'[{index + 1}] {entry}')


def add_entry(journal_data):
    text = input("Type your entry, <enter> to exit: ")
    journal.add_entry(text, journal_data)


main()
