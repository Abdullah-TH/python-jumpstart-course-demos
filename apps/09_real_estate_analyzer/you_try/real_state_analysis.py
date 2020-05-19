import csv
import os
import statistics
from typing import List

from Purchase import Purchase


def main():
    print_header()
    file_name = get_data_file_name()
    data = load_file(file_name)
    query_data(data)


def print_header():
    print('------------------------------------')
    print('     REAL STATE ANALYSIS APP')
    print('------------------------------------')
    print()


def get_data_file_name():
    base_directory = os.path.dirname(__file__)
    return os.path.join(
        base_directory,
        'data',
        'SacramentoRealEstateTransactions2008.csv'
    )


def load_file(file_name):
    purchases = []

    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for item in reader:
            p = Purchase.create_from_dict(item)
            purchases.append(p)

    return purchases


def query_data(data: List[Purchase]):
    data.sort(key=lambda p: p.price)

    # Most expensive house?
    high_purchase = data[-1]
    print(f"The most expensive house is ${high_purchase.price:,}, "
          f"with {high_purchase.beds} beds and {high_purchase.baths} baths")

    # Least expensive house?
    low_purchase = data[0]
    print(f"The lease expensive house is ${low_purchase.price:,}, "
          f"with {low_purchase.beds} beds and {low_purchase.baths} baths")

    # Average house price?
    prices = []
    for purchase in data:
        prices.append(purchase.price)
    average = statistics.mean(prices)
    print(f"Average home price is ${int(average):,}")

    # Average 2-bedrooms house price?
    two_beds_homes = [p for p in data if p.beds == 2]
    average_price = statistics.mean((p.price for p in two_beds_homes))
    average_baths = statistics.mean((p.baths for p in two_beds_homes))
    average_sqft = statistics.mean((p.sq__ft for p in two_beds_homes))
    print(f"Average 2-beds rooms house is ${int(average_price)}, "
          f"baths is {round(average_baths, 1)}, square-feet is {round(average_sqft, 1)}")


if __name__ == '__main__':
    main()
