import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
        pattern = r"^\s*(\d{1,2})(?::([0-5]\d))?\s+(AM|PM)\s+to\s+(\d{1,2})(?::([0-5]\d))?\s+(AM|PM)\s*$"
        match = re.search(pattern, s)
        if not match:
            raise ValueError("Please enter a valid format")

        h1, m1, p1, h2, m2, p2 = match.groups()
        h1 = int(h1)
        m1 = int(m1) if m1 is not None else 0
        h2 = int(h2)
        m2 = int(m2) if m2 is not None else 0

        if not ((1 <= h1 <= 12) and (1 <= h2 <= 12) and (0 <= m1 <= 59) and (0 <= m2 <= 59)):
            raise ValueError("Please enter a valid time")

        time1 = time_convert(h1, m1, p1)
        time2 = time_convert(h2, m2, p2)

        return f"{time1} to {time2}"

def time_convert(hour, minute, period):
    if period == 'AM':
        if hour == 12:
            hour = 0
        else:
            hour
    else:
        if hour == 12:
            hour
        else:
            hour = hour + 12

    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()
