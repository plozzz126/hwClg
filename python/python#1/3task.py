product = []
total = 0

count = int(input("enter the count of products: "))

for i in range(count):
    name = input("enter product name: ")
    price = float(input("enter product price: "))
    product.append({"name": name, "price": price})
    total += price

for p in product:
    print(f"{p['name']} - {p['price']}")
print("общая стоимость", total)