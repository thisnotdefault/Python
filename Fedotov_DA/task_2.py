cubes_odd_numbers_list = []
first_result = 0
second_result = 0

for number in range(0, 1000):
    if number % 2 != 0:
        number **= 3
        cubes_odd_numbers_list.append(number)

for number in cubes_odd_numbers_list:
    sum_digits = 0
    i = number
    while i > 0:
        digit = i % 10
        sum_digits += digit
        i //= 10

    if sum_digits % 7 == 0:
        first_result += number

print("Сумма чисел, до прибавления 17: {}".format(first_result))

for number in cubes_odd_numbers_list:
    sum_digits = 0
    number += 17
    i = number
    while i > 0:
        digit = i % 10
        sum_digits += digit
        i //= 10

    if sum_digits % 7 == 0:
        second_result += number

print("Сумма чисел , после прибавления 17: {}".format(second_result))
