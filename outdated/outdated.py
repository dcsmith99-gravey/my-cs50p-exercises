months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        try:
            date = input("Date: ")
            if "/" in date:
                mm, dd, yyyy = date.split("/")
                mm = int(mm)
                dd = int(dd)
                yyyy = int(yyyy)
            elif " " in date:
                if "," not in date:
                    raise ValueError
                date = date.replace(",", "")
                mm, dd, yyyy = date.split(" ")
                mm = int(months.index(mm) + 1)
                dd = int(dd)
                yyyy = int(yyyy)
            if not (1 <= dd <= 31):
                raise ValueError
            if not mm <= 12:
                raise ValueError

            print(f"{yyyy}-{mm:02}-{dd:02}")
            break

        except (ValueError):
            print()
            continue

        except EOFError:
            break
main()

