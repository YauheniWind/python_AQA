list_of_names = ["Ev", "Rick", "Amanda"]
list_of_numbers = [22, 54, 89]

list_of_numbers[-1] = 66
print(list_of_numbers)

list_of_names_and_numbers = list_of_names + list_of_numbers
print(list_of_names_and_numbers)

slice_of_list = list_of_names_and_numbers[::2]
print(slice_of_list)

slice_of_list += [34, "Nikita"]
print(slice_of_list)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(f"Intersection of two lists: {set(a) & set(b)}")

uniq = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
print(f"Uniq list: {set(uniq)}")
