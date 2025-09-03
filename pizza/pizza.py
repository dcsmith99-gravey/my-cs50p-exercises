import sys
from tabulate import tabulate
import csv

if len(sys.argv) < 2:
    sys.exit("Too few command line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command line arguments")

filename = sys.argv[1]

if not filename.endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open (filename, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(tabulate(rows, headers="keys", tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")
