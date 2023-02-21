import os

# Task 1


def check_element(name_of_file: str):
    if name_of_file.isnumeric():
        return "Error"
    elif name_of_file.endswith("txt"):
        with open(name_of_file) as file:
            for element in file:
                list_element = list(map(int, element))
                if len(list_element) < 3:
                    return "Error in file fewer elements than 3"
                else:
                    first_two_el = list_element[:2]
                    last_two_el = list_element[-2:]
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
        with open(name_of_file) as file:
            for element in file:
                split_element = element.split(" ")
                str_elem = list(map(str, split_element))
                for i in str_elem:
                    if int(i) % 2 == 0:
                        even_numbers.append(i)
                        file_even = open(name_of_even, "w")
                        file_even.writelines(even_numbers)
                        file_even.close()
                    else:
                        odd_numbers.append(i)
                        file_even = open(name_of_odd, "w")
                        file_even.writelines(odd_numbers)
                        file_even.close()
        return f"Data in {name_of_even} is {even_numbers}. Data in {name_of_odd} is {odd_numbers}"
    else:
        return "Error"


sperate_elem = separate_files("mix_number.txt", "even.txt", "odd.txt")


# Task 3
def square(numbers):
    return numbers**2


def squareding(name_of_file: str):
    if name_of_file.isnumeric():
        return "Error"
    elif name_of_file.endswith("txt"):
        with open(name_of_file, "r+") as file:
            print(file)
            for element in file:
                # split elements
                split_elements = element.split(" ")
                # Delete none from list
                with_out_none = list(filter(None, split_elements))
                # Convert type to float
                float_elements = list(map(float, with_out_none))
                # Multiply elements
                squareding_elements = list(map(square, float_elements))
                file.seek(0)
                file.truncate()
                for i in squareding_elements:
                    file.write(f"{str(i)} ")
        return f"New real numbers: {squareding_elements}"


square_var = squareding("real_numbers.txt")


def add_in_binary_file(name_of_file: str, data_value: any, encode: bool = True):
    # Crate file with some data
    a = data_value
    if encode == True:
        a = data_value.encode("utf8")
    with open(name_of_file, "wb+") as file:
        file.write(a)
    return data_value


def swaapiii(file_one: str, file_two: str):
    # Read files and write data, swape info
    bdata_read_one = read_bin_file(file_one)
    bdata_read_two = read_bin_file(file_two)

    os.remove(file_one)
    os.remove(file_two)

    add_in_binary_file(file_two, bdata_read_one, False)
    add_in_binary_file(file_one, bdata_read_two, False)
    return f"{bdata_read_one} {bdata_read_two}"


def read_bin_file(file):
    # read files
    with open(file, "rb+") as f1:
        bdata_read = f1.read()
    return bdata_read


print(add_in_binary_file("change_file_one.bin", "1234"))
print(add_in_binary_file("change_file_two.bin", "abcs"))

swaapiii(
    "change_file_one.bin",
    "change_file_two.bin",
)

read_bin_one = read_bin_file("change_file_one.bin")
read_bin_two = read_bin_file("change_file_two.bin")
print(read_bin_one, read_bin_two)
