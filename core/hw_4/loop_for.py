def plus_in_range(range_one, range_two):
    result = 0
    for i in range(range_one, range_two):
        result += i
    return result


print(plus_in_range(1, 11))

first_number = int(input("First number: "))
second_number = int(input("Second number: "))

print(plus_in_range(first_number, second_number))

dict_of_swim = {
    "Бекиш Александр": 21.07,
    "Будник Алексей": 20.34,
    "Гребень Анастасия": 22.12,
    "Давидович Татьяна": 30,
    "Дешук Дмитрий": 24.01,
    "Казак Анна": 28.17,
}


def winner(dict_swim):
    time = 0
    person = ""
    for key in dict_swim:
        if dict_swim[key] <= min(dict_swim.values()):
            time = dict_swim[key]
            person = key
    return f"Person: {person}, time: {time}"


print(winner(dict_of_swim))


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
