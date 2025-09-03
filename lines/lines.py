import sys

if len(sys.argv) < 2:
    sys.exit("Too few command line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command line arguments")

filename = sys.argv[1]

if not filename.endswith(".py"):
    sys.exit("Not a Python file")

try:
    with open (filename, "r") as f:
        lines = 0
        for line in f:
            stripped = line.strip()
            if stripped and not stripped.startswith("#"):
                lines += 1
        print(lines)

except FileNotFoundError:
    sys.exit("File does not exist")
