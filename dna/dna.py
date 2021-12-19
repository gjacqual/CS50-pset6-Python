import csv
import sys
import re


def main():
    # Check for correct quantity of arguments
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # names of files
    csv_filename = sys.argv[1]
    seq_filename = sys.argv[2]

    # open CSV file
    csv_file = open(csv_filename, "r")
    if not csv_file:
        print("CSV file didn't load")
        sys.exit(1)

    # read CSV to memory
    csv_data = csv.DictReader(csv_file)

    # get STR's list
    fields = csv_data.fieldnames[1:]

    # open DNA sequence
    seq_file = open(seq_filename, "r")
    if not seq_file:
        print("TXT file didn't load")
        sys.exit(1)

    # read content into memory
    sequence = seq_file.read()

    # Close file with sequences
    seq_file.close()

    # count the longest run repeats in the DNA sequence
    strs = count_repeats(sequence, fields)

    # compare the STR counts against each row in the CSV file

    result = compare(csv_data, strs)

    # Close file
    csv_file.close()

    if result != False:
        print(result)
    else:
        print('No match')


# for each STR compute the longest run repeats in the DNA sequence


def count_repeats(sequence, fields):
    # Convert the str list to a dictionary and set the counters to 0
    strs = dict.fromkeys(fields, 0)
    seq_len = len(sequence)

    # go step by step through sequence string
    for pos in range(seq_len):

        for str_name in strs:
            i = 0
            while re.match(str_name, sequence[pos:]):
                i += 1
                pos += len(str_name)

            # update counter of str's in dictionary
            if i > strs[str_name]:
                strs[str_name] = i
    return strs

# check each in the list of people


def compare(csv_data, strs):
    for row in csv_data:
        str_val = [int(row[str_name]) for str_name in strs]
        # if there is a match of the number of sequences
        if str_val == list(strs.values()):
            return row['name']
    return False


main()