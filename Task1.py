import csv

def read_csv_file(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def find_unique_telephone_numbers(texts, calls):
    telephone_numbers = set()

    for text in texts:
        telephone_numbers.add(text[0])
        telephone_numbers.add(text[1])

    for call in calls:
        telephone_numbers.add(call[0])
        telephone_numbers.add(call[1])

    return telephone_numbers

if __name__ == "__main__":
    # Read data from 'texts.csv' and 'calls.csv'
    texts = read_csv_file('texts.csv')
    calls = read_csv_file('calls.csv')

    # Task 1: Find unique telephone numbers in both texts and calls records
    unique_numbers = find_unique_telephone_numbers(texts, calls)

    # Print the count of different telephone numbers in the records
    print("The records contain {} unique telephone numbers.".format(len(unique_numbers)))
