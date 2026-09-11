#Разделил потому что читать не приятно когда всё вместе

#3 задание

# note = input("введите свою заметку: ")

# with open("notes.txt", "a",encoding="utf-8") as file:
#     file.write(note)

# with open("notes.txt", "r", encoding="utf-8") as file:
#     content = file.read()
#     print(content)

#4 Задание 

import json

books = [
{"title": "Гарри Поттер", "year": 1997},
{"title": "Маленький принц", "year": 1943}
]

with open("books.json", "w", encoding="utf-8") as file:
    json.dump(books, file, ensure_ascii=False, indent=4)

with open("books.json", "r", encoding="utf-8") as file:
    content = json.load(file)
    print(content)

with open("books.json", "r", encoding="utf-8") as file:
    content = json.load(file)
    for con in content:
        for key, val in con.items():
            # print(key, val)
            print(f"книга: {con['title']}, год издания {con['year']}")