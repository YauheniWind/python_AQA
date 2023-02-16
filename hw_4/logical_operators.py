number_one = 13
number_two = 8


def true_operations(operand_one, operand_two, val_one, val_two):
    return operand_one > val_one and operand_two > val_two


first_true = true_operations(number_one, number_two, 9, 7)
second_true = true_operations(number_one, number_two, 6, 4)
print(first_true, second_true)


def false_operations(operand_one, operand_two, val_one, val_two):
    return operand_one > val_one and operand_two > val_two


first_false = false_operations(number_one, number_two, 50, 10)
second_false = false_operations(number_one, number_two, 14, 9)
print(first_false, second_false)


def true_or_operation(operand_one, operand_two, val_one, val_two):
    return operand_one >= val_one or operand_two == val_two


first_or_true = true_or_operation(number_one, number_two, 13, 19)
second_or_true = true_or_operation(number_one, number_two, 8, 13)
print(first_or_true, second_or_true)


def false_or_operation(operand_one, operand_two, val_one, val_two):
    return operand_one > val_one or operand_two < val_two


first_or_false = false_or_operation(number_one, number_two, 50, 7)
second_or_false = false_or_operation(number_one, number_two, 100, 1)
print(first_or_false, second_or_false)

string_one = "Hello"
string_two = "aaabbb"


def try_str(str_one, str_two):
    return str_one > str_two


first_try = try_str(string_one, string_two)
print(first_try)
