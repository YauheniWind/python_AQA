# Task 1
def change_to_int(a):
    if type(a) == bool or type(a) == str:
        return a
    else:
        return int(a)


result_1 = change_to_int(1.6)
result_2 = change_to_int(2.99)
print(result_1)
print(result_2)


# Task 2
def change_symbol(string, old_symbol, new_symbol):
    if type(string) == str:
        new_string = string.replace(old_symbol, new_symbol)
        return new_string
    else:
        return f"Is not a string {string}"


result_3 = change_symbol("www.my_site.com#about", "#", "/")
print(result_3)


# Task 3
def add_ing(string):
    if type(string) == str:
        ing_string = f"{string}ing"
        return ing_string
    else:
        return f"something wrong {string}"


result_4 = add_ing("run")
print(result_4)


def delete_space(string):
    if type(string) == str:
        return f"{string}".strip()
    else:
        return f"something wrong {string}"


result_5 = delete_space("    Hello world    ")
print(result_5)


# Task 6
school = {"1a": 10, "1b": 20, "1c": 11, "1d": 21, "1e": 5, "1f": 33, "1g": 9, "1h": 2, "1j": 18}
print(school)


# Task 7
list_of_something = [1, 2, "Hola", 76]
print(list_of_something[1])


# Task 8
def string_in_other_string(string_one, string_two):
    if type(string_one) and type(string_two) == str:
        return string_one in string_two
    else:
        return f"something wrong {string_one}, {string_two}"


result_6 = string_in_other_string("employ", "employment")
print(result_6)


# Task 9
x = "My name is Agent Smith"
print(x[1])
print(x[3:16:3])


# Task 10
def uniq_number(array):
    for item in array:
        if array.count(item) == 1:
            return f"Non-repeated item: {item}"


pair_arr = [1, 5, 2, 9, 2, 9, 1]
result_7 = uniq_number(pair_arr)

print(result_7)
