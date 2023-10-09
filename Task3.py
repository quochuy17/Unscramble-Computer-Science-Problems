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

    # Task 3:

    # Part A: Find the codes of numbers called by people in Bangalore
    called_numbers = []
    for call in calls:
        caller, receiver = call[0], call[1]
        if caller.startswith('(080)'):
            if receiver.startswith('('):
                end_index = receiver.find(')') + 1
                called_numbers.append(receiver[:end_index])
            elif receiver.startswith('140'):
                called_numbers.append('140')
            else:
                called_numbers.append(receiver[:4])

    # Remove duplicates and sort the called codes
    unique_called_numbers = sorted(set(called_numbers))

    print("The numbers called by people in Bangalore have codes:")
    for code in unique_called_numbers:
        print(code)

    # Part B: Calculate the percentage of calls from fixed lines in Bangalore to other fixed lines in Bangalore
    count_bangalore_calls = called_numbers.count('(080)')
    total_calls = len(called_numbers)
    percentage = (count_bangalore_calls / total_calls) * 100

    print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(round(percentage, 2)))
