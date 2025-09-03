def main():
    user_input = input("What time is it? ")
    result = convert(user_input)
    if result >= 7 and result <= 8:
        print("breakfast time")
    elif result >= 12 and result <= 13:
        print("lunch time")
    elif result >= 18 and result <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    return hours + minutes / 60

if __name__ == "__main__":
    main()
