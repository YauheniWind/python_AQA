number_plus_one = "10"


def add(number):
    if type(number) == int or type(number) == float and number > 0:
        return number + 1
    else:
        return f"Error {type(number)} in not a number"


number_plus_one_val = add(number_plus_one)
print(number_plus_one_val)

number_one = 2
number_two = 5
number_three = -10


def count_positive_numbers(*args):
    counter_positive = 0
    for i in args:
        if i > 0:
            counter_positive += 1
    return counter_positive


year = 2023


def counting_year(a):
    if a % 4 != 0:
        return "365"
    elif a % 100 != 0:
        return "366"
    elif a % 400 != 0:
        return "365"
    else:
        return "366"


day = 2


def what_day_is_it_today(number):
    match number:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Out of range"


unit_of_measurement = 2
body_weight = 2


def body_weight_in_kilo(measurement, body_w):
    match measurement:
        case 1:
            return body_w
        case 2:
            return body_w / 1000000
        case 3:
            return body_w / 1000
        case 4:
            return body_w * 1000
        case 5:
            return body_w * 100
        case _:
            return "Out of range"
