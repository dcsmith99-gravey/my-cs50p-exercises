
def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")

def main():
    user_input = input("Enter your message: ")
    result = convert(user_input)
    print(result)

main()
