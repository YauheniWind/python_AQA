def number_product(num):
    if type(num) != int:
        return "Error"
    product = 1
    while num > 0:
        product *= num
        num -= 1
    return product


s1 = 1
s2 = 2


def area_calculation(s_one, s_two):
    if s_one <= 0 or s_two <= 0:
        return "Error"
    if type(s_one) and type(s_two) == int:
        year = 1
        while s_one > 0.1 * s_two:
            s_one *= 2
            s_two *= 3
            year += 1
        return s_one, s_two, year
    else:
        return "Error"


def count_number(n):
    if type(n) == int:
        count_of_numbers = 0
        sum_of_number = 0
        while n > 0:
            count_of_numbers += 1
            result = n % 10
            sum_of_number += result
            print(f"{count_of_numbers} - {result} - {sum_of_number}")
            n = int(n / 10)
        return count_of_numbers, sum_of_number
    else:
        return "Error"


def range_between(grandchild, grandpa):
    activate = True
    sum_of_year = 0
    while activate:
        sum_of_year = grandpa - 2 * grandchild
        activate = False
    return sum_of_year
