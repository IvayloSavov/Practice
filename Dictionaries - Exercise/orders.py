from collections import defaultdict

products = {}

command = input()

while command != "buy":
    product, price, quantity = command.split()

    if product not in products:
        products[product] = {
            "price": 0.0,
            "quantity": 0
        }

    products[product]["price"] = float(price)
    products[product]["quantity"] += int(quantity)

    command = input()

for product in products:
    print(f"{product} -> {products[product]['quantity'] * products[product]['price']:.2f}")