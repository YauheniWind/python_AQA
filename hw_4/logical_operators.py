number_one = 13
number_two = 8

first_true = number_one > 9 and number_two > 7
second_true = number_one > 6 and number_two > 4
print(first_true, second_true)

first_false = number_two > number_one and number_one < number_two
second_false = number_one > 14 and number_two < 1
print(first_false, second_false)


first_or_true = number_one > 10 or number_two < 1
second_or_true = number_two >= 8 or number_one == 19
print(first_or_true, second_or_true)

first_or_false = number_one > 50 or number_two < 7
second_or_false = (
    number_two < 1 and number_one > 100 or number_one > 20 and number_two < 1
)
print(first_or_false, second_or_false)

string_one = "Hello"
string_two = "aaabbb"

first_try = string_one > string_two or string_two < string_one
print(first_try)
