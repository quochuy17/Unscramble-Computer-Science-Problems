import csv
from collections import defaultdict
from datetime import datetime

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

    # Task 2: Calculate the total duration of calls for each phone number in September 2016
    calls_dictionary = defaultdict(int)

    for caller, receiver, timestamp, duration in calls:
        date = datetime.strptime(timestamp, "%d-%m-%Y %H:%M:%S")
        if date.year == 2016 and date.month == 9:
            calls_dictionary[caller] += int(duration)
            calls_dictionary[receiver] += int(duration)

    # Find the phone number with the longest total call duration
    highest_duration_phone, highest_duration = max(calls_dictionary.items(), key=lambda x: x[1])

    # Print the result
    template_import = "{} spent the longest time, {} seconds, on the phone during September 2016."
    print(template_import.format(highest_duration_phone, highest_duration))
