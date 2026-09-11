users = {}
todos = {}

def register():
    login = input(" enter login: ")
    passwr = input("enter password: ")
    if login in users:
        print("такой пользователь существует")
        return

    users[login] = passwr
    todos[login] = []

    print("reg success")

def login():
    while True:
        trL = input("enter login: ")
        trP = input("enter password: ")
        if trL in users:
            if trP == users[trL]:
                print("вошло")
                return trL
            else:
                print("неверный пароль")
        else:
            print("нет такого пользователя")

def add_task(user):
    task = input("enter quest: ")
    todos[user].append(task)
    print("добавило")

def show_tasks(user):
    print(f"вот задачи \n {todos[user]}")

def delete_task(user):
    show_tasks(user)
    det = int(input("выберите какое задание хотите удалить: "))
    if det < len(todos[user]):
        todos[user].pop(det -1)
    else:
        print("нету такого")
    
register()
user = login()
while True:
    choice = int(input("1. Добавить задачу \n 2. показать задачи \n 3. удалить задачу \n 0. выйти с аккаунта \n "))
    if choice == 1:
        add_task(user)

    elif choice == 2:
        show_tasks(user)

    elif choice == 3:
        delete_task(user)

    elif choice == 0:
        user = None
        break

