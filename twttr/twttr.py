
def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    no_vowel = ""
    for char in word:
        if char in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
            no_vowel += char.replace(char, "")
        else:
            no_vowel += char
    return no_vowel


if __name__ == "__main__":
    main()

