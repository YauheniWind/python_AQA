list_of_names = ["Ev", "Rick", "Amanda"]
list_of_numbers = [22, 54, 89]


def change_list(list_one, list_two):
    list_two[-1] = 66
    return list_one[1], list_two


print(change_list(list_of_names, list_of_numbers))


def join_lists(list_one, list_two):
    return list_one + list_two


list_of_names_and_numbers = join_lists(list_of_names, list_of_numbers)
print(list_of_names_and_numbers)


def slice_list(join_list):
    return join_list[::2]


slice_of_list = slice_list(list_of_names_and_numbers)
print(slice_of_list)


def add_elements(list_of_el, *args):
    list_of_el += [*args]
    return list_of_el


slice_of_list = add_elements(slice_of_list, 34, "Nikita")
print(slice_of_list)


def intersection_list(list_one, list_two):
    return set(list_one) & set(list_two)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

intersection_val = intersection_list(a, b)

print(f"Intersection of two lists: {intersection_val}")


def uniq_list(only_one):
    return set(only_one)


uniq = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
uniq_list_val = uniq_list(uniq)

print(f"Uniq list: {uniq_list_val}")
