amount_due = 50
accepted = [25, 10, 5]
inserted = 0

while inserted < amount_due:
    print(f"Amount Due: {amount_due - inserted}")
    coin = int(input("Insert Coin: "))
    if coin in accepted:
        inserted += coin
change = inserted - amount_due
print(f"Change Owed: {change}")
