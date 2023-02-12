school = {
    "1a": 10,
    "1b": 20,
    "1c": 11,
    "1d": 21,
    "1e": 5,
    "1f": 33,
    "1g": 9,
    "1h": 2,
    "1j": 18,
}
print(school)
for number_of_class, people in school.items():
    print(f"Class: {number_of_class}, Number of students: {people}")


def change_students(dictionaries, key, value):
    if type(dictionaries) == dict:
        class_new_value = dictionaries[key] = value
        return class_new_value
    else:
        return f"Error: {dictionaries} is not dict"


change_students(school, "1a", 2)
change_students(school, "1c", 3)
change_students(school, "1e", 55)


def add_class(dictionaries, key, value):
    if type(dictionaries) == dict:
        return dictionaries.update({key: value})
    else:
        return f"Error: {dictionaries} is not dict"


add_class(school, "1k", 42)
add_class(school, "1l", 32)


def clear_class(dictionaries, key):
    if type(dictionaries) == dict:
        return dictionaries.pop(key)
    else:
        return f"Error: {dictionaries} is not dict"


clear_class(school, "1a")

print(school)
