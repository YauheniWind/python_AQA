password = "HelloWorld"


def change_string(string):
    list_of_char = list(string)
    list_of_char.pop(0)
    list_of_char.pop()
    list_of_char.pop(2)
    list_of_char.pop(-2)
    return len(list_of_char)


string_len = change_string(password)
print(string_len)

long_string_var = "HelloMyNameIsEv"


def long_string(string):
    multiples_in_func = ""
    for index in range(len(string)):
        if index % 3 == 0:
            multiples_in_func += string[index]
    return string[:8], string[4:8], multiples_in_func, string[::-1]


print(long_string(long_string_var))


def name_in_string(name):
    if name.isnumeric():
        return name
    else:
        return f"my name is {name}"


print(name_in_string("Ev"))

test_tring = "Hello world!"


def trying(string):
    letters = string.split(" ")
    join_string = "".join(letters)
    return (
        string.find("w"),
        len(join_string),
        string.startswith("Hello"),
        string.endswith("qwe"),
    )


hola = trying(test_tring)
print(hola)
