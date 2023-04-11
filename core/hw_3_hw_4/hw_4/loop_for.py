def plus_in_range(a, b):
    total = 0
    if a < 0 or b < 0:
        return "Error"
    if type(a) == str or type(b) == str:
        return a + b
    else:
        try:
            if a > b:
                a, b = b, a

            for i in range(a, b + 1):
                total += i
        except:
            raise TypeError("Type is not integer or string")

    return total


first_number = 1
second_number = 4


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


def uniq_number(array):
    if type(array) == list:
        for item in array:
            if array.count(item) == 1:
                return f"Non-repeated item: {item}"
    else:
        return f"something wrong {array}"


pair_arr = [1, 5, 2, 9, 2, 9, 1]
result_uniq = uniq_number(pair_arr)
