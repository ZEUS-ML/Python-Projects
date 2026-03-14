menu = {"biryani":110,
        "litti chokha":50,
        "chola bhatura":80,
        "kadhai paneer":90}

total = 0
cart = []
print("----------MENU----------")
for key , value in menu.items():
    print(f"{key:20}${value}")

while True:
    order = input("select an item (q to quit): ").lower()
    if order == "q":
        break
    elif order in menu:
        cart.append(order)
    else:
        print("the item is not on the menu")
print("----------YOUR ORDERS----------")
for order in cart:
    total += menu.get(order)
    print(order,end=" ")
print()
print("-------------------------------")
print()
print(f"total cart: {total}")