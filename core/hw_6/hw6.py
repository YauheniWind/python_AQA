import os


# Task 1
def check_element(name_of_file: str):
    if name_of_file.isnumeric():
        return "Error"
    elif name_of_file.endswith("txt"):
        with open(name_of_file) as file:
            element_list = list(file.readline())
            if len(element_list) < 3:
                return "Error in file: fewer elements than 3"
            else:
                first_two_el = element_list[:2]
                last_two_el = element_list[-2:]
                return f"First two element: {first_two_el} , last two element: {last_two_el}"
    else:
        return "Error"


show_elem = check_element("text_one.txt")


# Task 2
def separate_files(name_of_file: str, name_of_even: str, name_of_odd: str):
    if name_of_file.isnumeric():
        return "Error"
    elif (
        name_of_file.endswith("txt")
        and name_of_even.endswith("txt")
        and name_of_odd.endswith("txt")
    ):
        even_numbers = []
        odd_numbers = []
        with open(name_of_file) as file, open(name_of_even, "w") as file_even, open(
            name_of_odd, "w"
        ) as file_odd:
            for element in file:
                for i in element.split():
                    if int(i) % 2 == 0:
                        even_numbers.append(i)
                    else:
                        odd_numbers.append(i)
            file_even.write(" ".join(even_numbers))
            file_odd.write(" ".join(odd_numbers))
            return f"Data in {name_of_even} is {even_numbers}. Data in {name_of_odd} is {odd_numbers}"
    else:
        return "Error"


sperate_elem = separate_files("mix_number.txt", "even.txt", "odd.txt")


# Task 3
def squareding(name_of_file: str):
    if name_of_file.isnumeric():
        return "Error"
    elif name_of_file.endswith("txt"):
        with open(name_of_file, "r+") as file:
            elements = file.read().split()
            squareding_elements = [str(float(x) ** 2) for x in elements]
            file.seek(0)
            file.write(" ".join(squareding_elements))
            return f"New real numbers: {squareding_elements}"


square_var = squareding("real_numbers.txt")


# Helper function
def read_bin_file(file: str):
    with open(file, "rb") as f:
        return f.read()


# Task 4
def add_in_binary_file(name_of_file: str, data_value: any, encode: bool = True):
    if encode:
        data_value = str(data_value).encode("utf-8")
    with open(name_of_file, "wb") as file:
        file.write(data_value)
    return data_value


def swap_files(file_one: str, file_two: str):
    data_read_one = read_bin_file(file_one)
    data_read_two = read_bin_file(file_two)

    os.remove(file_one)
    os.remove(file_two)

    add_in_binary_file(file_two, data_read_one, False)
    add_in_binary_file(file_one, data_read_two, False)

    return f"{data_read_two} {data_read_one}"


print(add_in_binary_file("change_file_one.bin", "1234"))
print(add_in_binary_file("change_file_two.bin", "abcs"))

swap_files("change_file_one.bin", "change_file_two.bin")

read_bin_one = read_bin_file("change_file_one.bin")
read_bin_two = read_bin_file("change_file_two.bin")
