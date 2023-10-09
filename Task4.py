import csv

# Function to read a CSV file and return its data as a list of lists
def read_csv_file(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

if __name__ == "__main__":
    # Read data from 'texts.csv' and 'calls.csv'
    texts = read_csv_file('texts.csv')
    calls = read_csv_file('calls.csv')

    # Task 4: Identify potential telemarketers

    # Extract telephone numbers from texts
    telephone_numbers_in_texts = set(chain.from_iterable(
        [(sender, receiver) for sender, receiver, _ in texts]))

    # Create sets of callers and call receivers
    callers = set()
    call_receivers = set()

    for caller, receiver, _, _ in calls:
        callers.add(caller)
        call_receivers.add(receiver)

    # Telemarketers don't text or receive calls
    possible_telemarketers = callers - (telephone_numbers_in_texts | call_receivers)

    print("These numbers could be telemarketers:")
    for tel_number in sorted(possible_telemarketers):
        print(tel_number)
