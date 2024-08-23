alice_in_wonderland = '''"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough." '''
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# added a (''') at the beginning and the end of a line

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
for char in alice_in_wonderland:
    if char == "'":
        print("'", end='')
print("\nThe symbol count is:", alice_in_wonderland.count("'"))
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
print("******************************************************************************")
Black_Sea_area = 436402
Azov_Sea_Area = 37800
total_area = Black_Sea_area+Azov_Sea_Area
print(f"The total area is Black Sea Area {Black_Sea_area} km2 + Azov Sea Area {Azov_Sea_Area} km2 = {total_area} km2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
print("******************************************************************************")
total_products = 375291
fist_second_storage = 250449
second_third_storage = 22950
first_storage_only = total_products - second_third_storage
third_storage_only = total_products - first_storage_only
second_storage_only = total_products - first_storage_only - third_storage_only

print(f"Total products count is {total_products}. "
      f"\nFirst and Second storage = {fist_second_storage}. "
      f"\nSecond and Third storage is {second_third_storage} "
      f"\n First Storage only = {total_products} - {fist_second_storage}. "
      f"\nThird storage = {total_products} - {first_storage_only}"
      f"\nSecond storage = {total_products} - {first_storage_only} - {third_storage_only}")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
print("******************************************************************************")
monthly_payment = 1179
print(f"The computet total price is: Monthly payment {monthly_payment} * 18 = ", monthly_payment * 18)

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print("******************************************************************************")
print("8019 mod 8 =", 8019 % 8,
      "\n9907 mod 9 =", 9907 % 9,
      "\n2789 mod 5 =", 2789 % 5,
      "\n7248 mod 6 =", 7248 & 6,
      "\n7128 mod 5 =", 7128 % 5,
      "\n19224 mod 9 =", 19224 % 9)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
print("******************************************************************************")
pizza_large_price = 274
pizza_medium_price = 218
juice_price = 35
cake_price = 350
water_price = 21

print(f"The total price for all products is: Large Pizza x4 {pizza_large_price*4}, "
      f"+ Medium pizza x2 {pizza_medium_price*2}, "
      f"+ Juice x4 {juice_price*4}, + Cake x1 {cake_price},"
      f"+ Water x3 {water_price*3} =",
      (pizza_large_price * 4) + (pizza_medium_price * 2) + (juice_price*4) + cake_price + (water_price * 3))

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
print("******************************************************************************")

total_photos = 232
needed_pages = 232/8

print(f"The total needed pages are: "
      f"Total photos {total_photos} / 8 (maxium photos that can be placed in one page) =", needed_pages)

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
print("******************************************************************************")

tank_capacity = 48
total_distance = 1600
consumption_per_100km = 9
total_fuel_needed = (total_distance / 100) * 9
number_of_refills = total_fuel_needed / tank_capacity
print(f"#1 Total fuel needed = Total distance ({total_distance} / 100) * "
      f"{consumption_per_100km} =", total_fuel_needed, "litres",
      f"\n#2 Number of refils = Total fuel {total_fuel_needed} / Tank Capacity {tank_capacity} = ", number_of_refills)
