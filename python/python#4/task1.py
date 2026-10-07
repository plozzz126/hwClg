from abc import ABC, abstractmethod
from datetime import datetime
import json
from pathlib import Path


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class Creditcard(PaymentMethod):
    def __init__(self, balance):
        self.balance = balance

    def pay(self, amount):
        self.balance -= amount
        print(f"Списано {amount} с карты. Остаток: {self.balance}")


class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Перевод {amount} через PayPal успешно выполнен")


def process_order(p_method, amount):
    p_method.pay(amount)

    history_path = Path(__file__).with_name("history.json")

    try:
        with history_path.open("r", encoding="utf-8") as file:
            history = json.load(file)
    except FileNotFoundError:
        history = []

    operation = {
        "method": type(p_method).__name__,
        "amount": amount,
        "time": datetime.now().strftime("%H:%M:%S"),
    }

    if isinstance(p_method, Creditcard):
        operation["balance"] = p_method.balance

    history.append(operation)

    with history_path.open("w", encoding="utf-8") as file:
        json.dump(history, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    card = Creditcard(100000)
    paypal = PayPal()

    process_order(card, 1000)
    process_order(paypal, 1000)
    process_order(card, 500)
    process_order(paypal, 500)
