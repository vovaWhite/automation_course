# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити/доповнити.
"""

print("Task 1")


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            break

            # Enter the action to take if the result is greater than 25
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15
print('*' * 100)
# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
print("Task 2")


def multiplication(number1, number2):
    return number1 * number2


print(multiplication(17, 5))

print('*' * 100)
# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
print("Task 3")


def arithmetic_average(numbers):
    return sum(numbers) / len(numbers) if numbers else "The list is empty"


number_list = [1, 2, 3, 4, 5, 6, 7, 10, 70]
average = arithmetic_average(number_list)
print(average)

number_list2 = []
average = arithmetic_average(number_list2)
print(average)

print('*' * 100)
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
print("Task 4")


def reverse_string(reverse):
    return reverse[::-1]


text = "Hello World"
reversed_text = reverse_string(text)
print(reversed_text)

print('*' * 100)
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
print("Task 5")


def find_longest_words(words):
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]
    return longest_words


list_of_words = ['Lviv', 'Odesa', 'Kyiv']


print(find_longest_words(list_of_words))
print('*' * 100)
# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
print('Task 6')


def find_substring_index(str1, str2):
    index = str1.find(str2)
    return index


str1 = "Hello, world!"
str2 = "world"
print(find_substring_index(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring_index(str1, str2))  # поверне -1
print('*' * 100)
# task 7
print('Task 7')
# homework 3 - Area of Seas


def total_area_of_seas(black_sea_area, azov_sea_area):
    return black_sea_area + azov_sea_area


black_sea_area = 436402
azov_sea_area = 37800


total_area = total_area_of_seas(black_sea_area, azov_sea_area)
print(f"Total area of seas {total_area} ")

print('*' * 100)
# task 8
print('Task 8')
"""Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі."""


def storages_capacity(total_items, first_and_second, second_and_third):

    first_only = (total_items - second_and_third)
    third_only = (total_items - first_and_second)
    second_only = (total_items - first_only - third_only)

    return first_only, second_only, third_only


total_items = 375291
first_and_second = 250449
second_and_third = 222950


A, B, C = storages_capacity(total_items, first_and_second, second_and_third)

print(f"First storage {A}")
print(f"Second storage {B}")
print(f"Third storage {C}")

print('*' * 100)
# task 9
print('Task 9')
"""Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера."""


def comp_price(month_quantity, monthly_payment):
    return month_quantity * monthly_payment


montly_payment = 1179
month_quantity = 18

computer_total_price = comp_price(int(month_quantity), montly_payment)
print(computer_total_price)
print('*' * 100)
# task 10
print('Task 10')
"""Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?"""


def pages_count(photos_count, page_capacity):
    return photos_count / page_capacity


photos_count = 232
page_capacity = 8

total_pages_count = pages_count(photos_count, page_capacity)
print(total_pages_count)

print('*' * 100)
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
