"""Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
(враховуються як великі так і маленькі).
Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".
"""


while True:
    user_input = input("Enter your text here: ")
    if 'H' in user_input or "h" in user_input:
        print("Nice! Good Job! Wow!")
        break
    else:
        print("Bro, there is no 'H' here, try again")
