from product import Product, Pizza, Drink
from log import reg_log
from order import Order
from cart import Cart

auth = reg_log()
cart = Cart()

products = []

current_user = None

while True:
    choice = int(input("log/reg\n 1. Регистрация \n 2. Логин \n 0. Выход\n Введите: "))
    match choice:
        case 1:
            username = input("Введите Имя: ")
            password = input("Введите пароль: ")
            auth.reg(username, password)
            auth.save()
        case 2:
            username = input("Введите Имя: ")
            password = input("Введите пароль: ")
            if auth.log(username, password):
                current_user = username
                break

while True:
    choice = int(input("1. Управление товарами\n2. Показать товары\n3. Корзина\n4. Оформить заказ\n0. Выход\nВыберите: "))
    match choice:
        case 1:
            choice2 = int(input("1. Создать Пиццу\n2. Создать Напиток\n3. 0. Выход\n Выберите: "))
            match choice2:
                case 1:
                    name = input("Введите название Пиццы: ")
                    price = int(input("Введите цену Пиццы: "))
                    size = int(input("Введите размер пиццы в сантиметрах: "))
                    products.append(Pizza(name, price, size))
                case 2:
                    name = input("Введите название Напиток: ")
                    price = int(input("Введите цену Напитка: "))
                    volume = int(input("Введите объём напитка: "))
                    products.append(Drink(name, price, volume))        
                case 0:
                    break
                    
        case 2:
            for i in range(len(products)):
                print(i + 1, products[i].get_p())
            while True:
                choice2 = int(input("Выберите 0 что бы закончить\nВыберите продукт: "))
                if choice2 == 0:
                    break
                if 0 < choice2 <= len(products):
                    cart.add_prod(products[choice2 - 1])
                else:
                    print("неверный выбор")

        case 3:
            cart.inf_pr()
            print(f"Итого: {cart.total()}")

        case 4:
            a = cart.get_cart()
            b = cart.total()

            if not a:
                print("корзина пуста")
            else:
                order = Order(a, b, current_user, "Готовиться")
                order.save()
                cart.clear()


        case 0:
            break
        
#доделать нормальный импорт в json формат потому что goods содержит объекты а json напрямую не может взаимодействовать с объектамии обернуть циклом в словарь внутри списка 


