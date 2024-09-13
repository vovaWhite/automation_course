
def sum_of_numbers_in_string(s):
    try:
        numbers = [int(num) for num in s.split(',')]
        return sum(numbers)
    except ValueError:
        return "Не можу це зробити!"


strings_array = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]


results = [sum_of_numbers_in_string(s) for s in strings_array]
print(results)
