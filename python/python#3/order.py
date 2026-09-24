import json
from product import Pizza, Drink


class Order():
    def __init__(self, goods, tot_price, user, status):
        self.goods = goods
        self.tot_price = tot_price
        self.user = user
        self.status = status

    def get_ord(self):
        return self.goods, self.tot_price, self.user, self.status

    def change_status(self):
        status = int(input("Выберите статус заказа\n 1. Готовиться\n 2. Передан Курьеру\n 3. В пути\n 4. Доставлен\n Введите число: "))

        cs = ""

        match status:
            case 1:
                print("вы успешно поставили статус: Готовиться")
                cs = "Готовиться"
            case 2:
                print("вы успешно поставили статус: Передан курьеру")
                cs = "Передан курьеру"
            case 3:
                print("вы успешно поставили статус: В пути")
                cs = "В пути"

            case 4:
                print("вы успешно поставили статус: Доставлен")
                cs = "Доставлен"

            case _:
                print("Нет такого выбора")
                return

        self.status = cs

    def save(self):
        gds = []

        for i in range(len(self.goods)):

            a = self.goods[i].get_p()
            if isinstance(self.goods[i], Pizza):
                form = "size"
                gds.append({"name": a[0], "price": a[1], form: a[2]})
            elif isinstance(self.goods[i], Drink):
                form = "volume"
                gds.append({"name": a[0], "price": a[1], form: a[2]})
            else:
                gds.append({"name": a[0], "price": a[1]})

        try:
            with open("orders.json", "r", encoding="utf-8") as file:
                orders = json.load(file)
        except FileNotFoundError:
            orders = []

        data = {
            "goods": gds,
            "tot_price": self.tot_price,
            "user": self.user,
            "status": self.status
        }
        orders.append(data)
        with open ("orders.json", "w", encoding="utf-8") as file:
            json.dump(orders, file, ensure_ascii=False, indent=4)
