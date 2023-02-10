password = "HelloWorld"

list_of_char = list(password)
first_char = list_of_char.pop(0)
last_char = list_of_char.pop()
third_element = list_of_char.pop(2)
reversed_third_element = list_of_char.pop(-2)

print(first_char)
print(last_char)
print(third_element)
print(reversed_third_element)
print(len(list_of_char))

long_string = "HelloMyNameIsEv"
print(long_string[:8])
print(long_string[4:8])
multiples = ""
for index in range(len(long_string)):
    if index % 3 == 0:
        print(index)
        multiples += long_string[index]
print(multiples)

print(long_string[::-1])


def name_in_string(name):
    if name.isnumeric():
        return name
    else:
        return f"my name is {name}"


print(name_in_string("Ev"))


test_tring = "Hello world!"
find_w = test_tring.find("w")
letters = test_tring.split(" ")
join_letters = "".join(letters)

print(find_w)
print(len(join_letters))

start_with = test_tring.startswith("Hello")
end_with = test_tring.endswith("qwe")

print(start_with)
print(end_with)
