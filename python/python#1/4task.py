
listG = []

name = input("введите имя: ")
gradeC = int(input("введите сколько вы хотите ввести оценок от 1 - 5: "))
for i in range(gradeC):
    grade = int(input("enter your grades: "))
    listG.append(grade)

summa = 0
max_num = listG[0]
min_num = listG[0]
for num in listG:
    if num > max_num:
        max_num = num 
    if num < min_num:
        min_num = num
    summa += num 

if gradeC > 0:
    avg = summa / gradeC
else: 
    average = 0

print(f"среднее: {avg:.2f} ")
print(f"максимальное: {max_num}")
print(f"минимальное: {min_num}")

if avg >= 4:
    print("Хороший результат")
else:
    print("нужно повторить тему")
