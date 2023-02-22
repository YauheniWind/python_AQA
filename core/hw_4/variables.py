var_int = 10
var_float = 8.4
var_str = "No"


def big_int(number_one, number_two):
    return number_one * number_two


big_int_from_def = big_int(var_int, 3.5)


def reduction(number_one, number_two):
    return number_one - number_two


var_float_from_def = reduction(var_float, 1)


def division(number_one, number_two):
    return number_one / number_two


var_int_division = division(var_int, var_float)
var_big_int_division = division(big_int_from_def, var_float)


def string_var(str_one, str_two):
    return str_one + str_one + str_two * 3


# var_str += "No" + "Yes" * 3
var_str_from_def = string_var(var_str, "Yes")
