import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command line arguments")

before = sys.argv[1]
after = sys.argv[2]

if not before.endswith(".csv"):
    sys.exit("Not a CSV file")

if not after.endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open (before, "r") as b, open (after, "w") as a:
        reader = csv.DictReader(b)
        writer = csv.DictWriter(a, fieldnames=["first", "last", "house"])
        writer.writeheader()

        for row in reader:
            last, first = row["name"].split(",")
            last = last.strip()
            first = first.strip()

            writer.writerow({
                "first": first,
                "last": last,
                "house": row["house"]
            })

except FileNotFoundError:
    sys.exit(f"Could not read {before}")


