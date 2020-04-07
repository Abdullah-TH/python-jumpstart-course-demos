import datetime


def print_header():
    print('------------------------------')
    print('        BIRTHDAY APP')
    print('------------------------------')
    print()


def get_birthday_from_user():
    print('When were you born?')
    year = int(input('Enter year [YYYY]: '))
    month = int(input('Enter month [MM]: '))
    day = int(input('Enter day [DD]: '))

    birthday = datetime.date(year, month, day)
    return birthday


def compute_days_between_dates(first_date, second_date):
    this_year = datetime.date(second_date.year, first_date.month, first_date.day)
    number_of_days = this_year - second_date
    return number_of_days.days


def print_birthday_information(number_of_days):
    if number_of_days > 0:
        print(f'Your birthday is in {number_of_days} days!')
    elif number_of_days < 0:
        print(f'You had your birthday {-number_of_days} days ago this year.')
    else:
        print('Happy birthday!!!')


def main():
    print_header()
    birthday = get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(birthday, today)
    print_birthday_information(number_of_days)


main()
