answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
refined = answer.strip().lower()
if refined == "42" or refined == "forty-two" or refined == "forty two":
    print("Yes")
else:
    print("No")
