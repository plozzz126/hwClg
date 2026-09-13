class Film():
    def __init__(self, title, rating):
        self.title = title
        self.__rating = rating

    def show_info(self):
        print(f"Название {self.title} \n рейтинг {self.__rating}")

    def get_rating(self):
        return self.__rating

    def set_rating(self, rating):
        if 0 <= rating <= 10:
            self.__rating = rating
            print("оценка успешно поставлена")
        else:
            print("ошибка: меньше 1 и больше 10 оценку ввести нельзя")


film = Film("Fear", 5)

film.show_info()

get = film.get_rating()
print(get)

film.set_rating(10)
film.show_info()