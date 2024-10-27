# first function
def multiplication_table1(number):
    multiplier = 1
    results = []

    while True:
        result = number * multiplier
        if result > 25:
            break
        results.append(f"{number}x{multiplier}={result}")
        multiplier += 1

    return results


# 2nd function
def arithmetic_average(numbers):
    return sum(numbers) / len(numbers) if numbers else "The list is empty"


number_list = [1, 2, 3, 4, 5, 6, 7, 10, 70]
average = arithmetic_average(number_list)
print(average)

number_list2 = []
average = arithmetic_average(number_list2)
print(average)

# 3rd function


def reverse_string(reverse):
    return reverse[::-1]


text = "Hello World"
reversed_text = reverse_string(text)
print(reversed_text)
