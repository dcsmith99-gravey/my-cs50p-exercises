def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            continue

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if x < 0 or y < 0 or x > y:
        raise ValueError
    else:
        return round(((x / y)) * 100)

if __name__ == "__main__":
    main()



