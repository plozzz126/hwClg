def cht(b):
    if b % 2 == 0:
        return " ичётное число"
    else: 
        return "и нечётное число"

def pns(a):
    pp = cht(a)
    if a > 0:
        return f"положительное {pp}"    
    elif a < 0:
        return f"отрицательное {pp}"
    elif a == 0:
        return "ноль"
    
n = int(input("введите число: "))
print(pns(n))