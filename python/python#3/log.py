import json
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)


USERS_FILE = DATA_DIR / "users.json"

class User:
    def __init__(self, username, __password):
        self.username = username
        self.__password = __password

    def get_pass(self):
        return self.__password

class reg_log():
    def __init__(self):
        self.users = []
        self.x = []
        self.load()

    def load(self):
        try:
            with open(USERS_FILE, "r", encoding="utf-8") as file:
                users = json.load(file)

            for user in users:
                self.users.append(User(user["username"], user["password"]))

        except FileNotFoundError:
            pass

    def dictt(self):
        self.x = []
        for i in range(len(self.users)):
            self.x.append({"username": self.users[i].username, "password": self.users[i].get_pass()})
        return self.x
        

    def save(self):
        with open(USERS_FILE, "w", encoding="utf-8") as file:
            json.dump(self.dictt(), file, ensure_ascii=False, indent=4)

    def reg(self, username, password):
        for i in range(len(self.users)):
            if self.users[i].username == username:
                print("такой пользователь уже существует ")
                return

        self.users.append(User(username, password))

    def log(self, username, password):
        for i in range(len(self.users)):
            if self.users[i].username == username:
                if self.users[i].get_pass() == password:
                    print("успешно вошли в аккаунт")
                    return True
        else:   
            print("неверный логин или пароль")
            return False

    
        
