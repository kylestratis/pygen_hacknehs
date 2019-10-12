"""
Example 1: Reading large files with generator functions
Usage: replace "some_csv.txt" with location of your CSV
"""


def main(gen=True):
    if gen:
        csv_gen = csv_reader_gen("hg38.fa")
    else:
        csv_gen = csv_reader("hg38.fa")
    row_count = 0

    for row in csv_gen:
        row_count += 1

    print(f"Row count is {row_count}")


def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result


def csv_reader_gen(file_name):
    for row in open(file_name, "r"):
        yield row


if __name__ == "__main__":
    main(False)
