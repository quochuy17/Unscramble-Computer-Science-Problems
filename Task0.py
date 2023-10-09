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

    # Task 0: Print the first record of texts and the last record of calls
    first_text = texts[0]
    last_call = calls[-1]

    print("First record of texts, {} texts {} at time {}"
          .format(first_text[0], first_text[1], first_text[2]))
    print("Last record of calls, {} calls {} at time {}, lasting {} seconds"
          .format(last_call[0], last_call[1], last_call[2], last_call[3]))
