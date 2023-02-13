robin_name = "Robin Singh"
love = "I love arrays they are my favorite"


def string_to_array(string):
    if string.isnumeric():
        return f"Error: {string} is not string"
    else:
        return string.split()


print(f"Name: {string_to_array(robin_name)} ,Love: {string_to_array(love)}")

ivan_name = ["Ivan", "Ivanou"]
name_of_city = "Minsk"
name_of_country = "Belarus"


def greeting(list_name, city, country):
    if type(list_name) == list:
        full_name = " ".join(list_name)
        return f"Привет, {full_name}! Добро пожаловать в {city} {country}"
    else:
        return f"Error: {list_name} is not list"


print(greeting(ivan_name, name_of_city, name_of_country))

love_list = ["I", "love", "arrays", "they", "are", "my", "favorite"]


def join_strings(join_list):
    if type(join_list) == list:
        return " ".join(join_list)
    else:
        return f"Error: {join_list} is not list"


print(join_strings(love_list))

somthing_list = [12, 34, 56, 76, 234, 546, 6322, 5677, 23, 34]

somthing_list.insert(3, 44)
somthing_list.pop(6)
print(f"Update list: {somthing_list}")

a = {"a": 1, "b": 2, "c": 3}
b = {"c": 3, "d": 4, "e": 5}
ab = {}

for key, value in a.items():
    if key in b:
        ab[key] = [a[key], b[key]]
    else:
        ab[key] = [value, None]

for key, value in b.items():
    if key in a:
        ab[key] = [a[key], b[key]]
    else:
        ab[key] = [None, value]

print(ab)


def uniq_number(array):
    if type(array) == list:
        for item in array:
            if array.count(item) == 1:
                return f"Non-repeated item: {item}"
    else:
        return f"something wrong {array}"


pair_arr = [1, 5, 2, 9, 2, 9, 1]
result_uniq = uniq_number(pair_arr)

print(result_uniq)

sometext = "How do you do?"


def count_letter(string):
    lower_string = string.lower()
    dik = {}
    for element in lower_string:
        if element.isalpha():
            if element in dik.keys():
                dik[element] = dik.get(element) + 1
            elif element not in dik.keys():
                dik[element] = 1
    sort_key = dik.keys()
    sorted_key = sorted(sort_key)

    if sum(dik.values()) == len(dik):
        return f"Most common letter: {sorted_key[0]}"
    else:
        index_value = max(dik, key=dik.get)
        return f"Most common letter: {index_value}"


print(count_letter(sometext))
