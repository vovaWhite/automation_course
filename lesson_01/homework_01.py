# task 01 == Виправте синтаксичні помилки
print("Hello", end=" ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
letter: str
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4

# task 05 == виправте назви змінних
side_1 = 1
side_2 = 2
side_3 = 3
side_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = side_1 + side_2 + side_3 + side_4
print()

"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apple_tree = 4
pear_tree = apple_tree + 5
plum_tree = pear_tree - 2
print('Task 7')
print('Apple Trees =', apple_tree,
      '\nPear Trees =', pear_tree,
      '\nPlum Trees =', plum_tree)
print("Total number of trees is ", plum_tree + pear_tree + apple_tree)

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
# temperature overview
print('Task 8')
morning_temperature = 5
afternoon_temperature = 5 - 10
evening_temperature = afternoon_temperature + 4

print('Температура зранку: 0 + 5 =', morning_temperature,
      '\nТемпература після обіду: 5-10 =', afternoon_temperature,
      '\nТемпература ввечері: -5+4 =', evening_temperature)

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys = 24
girls = boys / 2
total_count = (boys - 1) + (girls - 2)
print('Task 9')
print('Boys:', boys,
      '\nGirls: 24/2=', girls,
      '\nTotal Count: (24-1)+(12-2)', total_count)

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
first_book = 8
second_book = first_book + 2
third_book = (first_book + second_book) / 2
total_price = first_book + second_book + third_book
print("Task 10")
print('First Book price:', first_book,
      '\nSecond Book price: 8+2=', second_book,
      '\nThird book price: (8+10)/2=', third_book,
      "\nTotal price = 8+10+9=", total_price)
