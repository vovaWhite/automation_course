"""Порахувати кількість унікальних символів в строці.
Якщо їх більше 10 - вивести в консоль True, інакше - False.
Строку отримати за допомогою функції input()"""

default_string = input("Enter your text here: ")

unique_characters = set(default_string)

if len(unique_characters) > 10:
    print('True')
else:
    print("False")


