import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    num = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=a1f2707433e0f2f477195c129b37efbaf141d996b2d063245fd398a958169d19")
    content = response.json()
    price = float(content["data"]["priceUsd"])
    total_price = price * num
    print(f"${total_price:,.4f}")

except requests.RequestException:
  sys.exit("Error getting price")
