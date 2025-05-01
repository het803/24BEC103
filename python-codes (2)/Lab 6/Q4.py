food = input("Enter food items and their prices: ").split()
food = []

for i in range(0, len(food), 2):
    item = food[i]
    price = float(food[i + 1])
    food.append((item, price))

sort = sorted(food, key=lambda item: item[1], reverse=True)

print(sort)
