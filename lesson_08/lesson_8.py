# Функція для обчислення суми чисел у рядку, розділених комою
def sum_of_numbers_in_string(s):
    try:
        # Розділяємо рядок за комами і перетворюємо елементи в числа
        numbers = [int(num) for num in s.split(',')]
        return sum(numbers)
    except ValueError:
        # Якщо з'являються символи, що не є числами, ловимо помилку
        return "Не можу це зробити!"

# Масив зі строками
strings_array = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

# Виведення суми для кожного рядка
results = [sum_of_numbers_in_string(s) for s in strings_array]
print(results)