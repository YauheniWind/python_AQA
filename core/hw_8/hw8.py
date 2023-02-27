import time


def fibo_re(n):
    if n < 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_re(n - 1) + fibo_re(n - 2)


def fibo_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, b + a


start_one = time.time()
gen = fibo_gen()
for i in range(10):
    print(next(gen), "Gen")
end_one = time.time()


def fibo_simple(n):
    fib_num_one = 1
    fib_num_two = 1
    for _ in range(2, n):
        fib_num_one, fib_num_two = fib_num_two, fib_num_two + fib_num_one

    return fib_num_two


start_two = time.time()
print(fibo_re(9), "Recurs")
end_two = time.time()

start_three = time.time()
print(fibo_simple(9), "Simple")
end_three = time.time()


def check_type(check):
    def decor(func):
        def wrapper(*args):
            any_list = []
            for _, arg in enumerate(args):
                if check == "str":
                    any_list.append(str(arg))
                elif check == "int":
                    try:
                        if type(arg) == int:
                            any_list.append(int(arg))
                        elif type(arg) == float:
                            any_list.append(float(arg))
                        else:
                            any_list.append(int(arg))
                    except ValueError:
                        raise TypeError(f"Argument {i} must be of type {type}")
                else:
                    raise ValueError(f"Unsupported type: {check}")
            return func(*any_list)

        return wrapper

    return decor


@check_type("str")
def add_two_symbols(a, b):
    return str(a) + str(b)


@check_type("int")
def add_three_symbols(a, b, c):
    return a + b + c


number_names = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}


def dic_numbers(func):
    def wrapper(numbers_str):
        numbers = numbers_str.split()
        names = [number_names[int(n)] for n in numbers]
        sorted_names = sorted(names)
        sorted_numbers = [
            str(list(number_names.keys())[list(number_names.values()).index(name)])
            for name in sorted_names
        ]
        return func(" ".join(sorted_numbers))

    return wrapper


@dic_numbers
def numbers_name(numbers_str):
    return numbers_str
