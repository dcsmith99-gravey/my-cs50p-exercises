import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

fonts = figlet.getFonts()

if len(sys.argv) == 1:
    font = random.choice(fonts)
    figlet.setFont(font=font)

elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("First argument must be -f or --font")
    if sys.argv[2] not in fonts:
        sys.exit("Invalid font name")
    else:
        figlet.setFont(font=sys.argv[2])

else:
    sys.exit("Must have 0 or 2 arguments")

text = input("Input: ")
print(f"Output: {figlet.renderText(text)}")


