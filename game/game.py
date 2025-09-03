import random

def main():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
        except ValueError:
            pass

    target = random.randint(1, level)


    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                continue
            if guess < target:
                print("Too small!")
            elif guess > target:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            continue

main()




import random

def main():
    level = get_level()
    target = random.randint(1, level)
    guess_number(target)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            pass  # just loop again

def guess_number(target):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                continue
            if guess < target:
                print("Too small!")
            elif guess > target:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            pass  # ignore and prompt again

main()
