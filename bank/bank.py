user_input = input("Greeting: ")
greeting = user_input.strip().lower()
if greeting == "hello" or greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")

