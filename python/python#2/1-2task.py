
prices = [1200, 3500, 800, 2100, 5000, 1700]

first = prices[0:3]
print(first)
second = prices[-2:]
print(second)
third = prices[::-1]
print(third)

max_vl = prices[0]
min_vl = prices[0]

for i in range(1, len(prices)):
    if max_vl < prices[i]:
        max_vl = prices[i]
    if min_vl > prices[i]:
        min_vl = prices[i]

count = len(prices)

print(f"максимальное {max_vl} \n минимальное {min_vl} \n количество элементов {count} \n\n\n\n 2 ЗАДАНИЕ \n\n")

students = [
{"name": "Анна", "grade": 5},
{"name": "Иван", "grade": 4},
{"name": "Олег", "grade": 3}
]

students.append({"name": "Алексей", "grade": 2})
for item in students:
    for vl in item.values():
        print(vl)

students[3].update({"grade": 5})
print(students[3])



