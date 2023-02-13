result = 0

for i in range(1, 11):
    result += i

print(result)

first_number = int(input("First number: "))
second_number = int(input("Second number: "))
result_sum = 0

for i in range(first_number, second_number):
    result_sum += i

print(result_sum)

dict_of_swim = {
    "Бекиш Александр": 21.07,
    "Будник Алексей": 20.34,
    "Гребень Анастасия": 22.12,
    "Давидович Татьяна": 30,
    "Дешук Дмитрий": 24.01,
    "Казак Анна": 28.17,
}

time = 0
person = ""

for key in dict_of_swim:
    if dict_of_swim[key] <= min(dict_of_swim.values()):
        time = dict_of_swim[key]
        person = key
print(f"Person: {person}, time: {time}")


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
