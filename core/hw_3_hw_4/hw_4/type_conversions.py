robin_name = "Robin Singh"
love = "I love arrays they are my favorite"


def string_to_array(string):
    if string.isnumeric():
        return f"Error: {string} is not string"
    else:
        return string.split()


ivan_name = ["Ivan", "Ivanou"]
name_of_city = "Minsk"
name_of_country = "Belarus"


def greeting(list_name, city, country):
    if type(list_name) == list:
        full_name = " ".join(list_name)
        return f"Привет, {full_name}! Добро пожаловать в {city} {country}"
    else:
        return f"Error: {list_name} is not list"


love_list = ["I", "love", "arrays", "they", "are", "my", "favorite"]


def join_strings(join_list):
    if type(join_list) == list:
        return " ".join(join_list)
    else:
        return f"Error: {join_list} is not list"


somthing_list = [12, 34, 56, 76, 234, 546, 6322, 5677, 23, 34]


def insert_and_pop_element(list_of_el, insert_el_one, insert_el_two, pop_el):
    list_of_el.insert(insert_el_one, insert_el_two)
    list_of_el.pop(pop_el)
    return list_of_el


a = {"a": 1, "b": 2, "c": 3}
b = {"c": 3, "d": 4, "e": 5}
ab = {}


def reunion(dict_one, dict_two, reunio_dict):
    for key, value in dict_one.items():
        if key in dict_two:
            reunio_dict[key] = [dict_one[key], dict_two[key]]
        else:
            reunio_dict[key] = [value, None]

    for key, value in dict_two.items():
        if key in dict_one:
            reunio_dict[key] = [dict_one[key], dict_two[key]]
        else:
            reunio_dict[key] = [None, value]
    return reunio_dict


def uniq_number(array):
    if type(array) == list:
        for item in array:
            if array.count(item) == 1:
                return f"Non-repeated item: {item}"
    else:
        return f"something wrong {array}"


pair_arr = [1, 5, 2, 9, 2, 9, 1]
result_uniq = uniq_number(pair_arr)

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
