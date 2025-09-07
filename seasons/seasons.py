from datetime import date
import sys
import inflect

def main():
    dob = get_birthdate()
    minutes = get_minutes(dob)
    print(f"{words(minutes)} minutes")

def get_birthdate():
    bday_str = input("Date of Birth: ")
    try:
        return date.fromisoformat(bday_str)
    except ValueError:
        sys.exit("Invalid date")

def get_minutes(dob):
    today = date.today()
    delta = date.__sub__(today, dob)
    return delta.days * 24 * 60

def words(n):
    p = inflect.engine()
    return p.number_to_words(n, andword="").capitalize()

if __name__ == "__main__":
    main()
