def number_product(n):
    product = 1
    while n > 0:
        product *= n
        n -= 1
    return product


print(number_product(5))

s1 = int(input("Enter area one: "))
s2 = int(input("Enter area two: "))


def area_calculation(s_one, s_two):
    if type(s_one) and type(s_two) == int:
        year = 1
        while s_one > 0.1 * s_two:
            s_one *= 2
            s_two *= 3
            year += 1
        print(f"First area: {s_one}")
        print(f"Second area: {s_two}")
        print(f"In {year} year")
        return s_one, s_two, year
    else:
        return "Error"


area_calculation(s1, s2)


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
        print(f"Count of number: {count_of_numbers}")
        print(f"Sum of number: {sum_of_number}")
        return count_of_numbers, sum_of_number
    else:
        return "Error"


print(count_number(123))


def range_between(grandchild, grandpa):
    activate = True
    sum_of_year = 0
    while activate:
        sum_of_year = grandpa - 2 * grandchild
        print(f"Result: {sum_of_year}")
        print(f"Grandpa: {grandpa + sum_of_year}")
        print(f"Grandchild: {grandchild + sum_of_year}")
        activate = False
    return sum_of_year


print(range_between(2, 40))
