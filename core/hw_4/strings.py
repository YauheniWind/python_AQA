def change_string(string):
    list_of_char = list(string)
    list_of_char.pop(0)
    list_of_char.pop()
    list_of_char.pop(2)
    list_of_char.pop(-2)
    return len(list_of_char)


def long_string(string):
    multiples_in_func = ""
    for index in range(len(string)):
        if index % 3 == 0:
            multiples_in_func += string[index]
    return string[:8], string[4:8], multiples_in_func, string[::-1]


def name_in_string(name):
    if name.isnumeric():
        return name
    else:
        return f"my name is {name}"


def trying(string):
    letters = string.split(" ")
    join_string = "".join(letters)
    return (
        string.find("w"),
        len(join_string),
        string.startswith("Hello"),
        string.endswith("qwe"),
    )
