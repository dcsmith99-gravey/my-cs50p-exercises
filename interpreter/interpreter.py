user_input = (input("Expression: "))
x, y, z = user_input.split(" ")
x = float(x)
z = float(z)

if y == "+":
    print(round((x + z), 1))
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    print(x / z)
else:
    print("Enter a valid argument")

