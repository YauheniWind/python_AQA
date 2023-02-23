# Task 1
user_name = "Ev"
greeting = lambda name: f"Hello {name}"

# Task 2
names = ["Helen", "Shanik", "Jozho"]

greetings = lambda names_in_lam: [f"Hello, {name}" for name in names_in_lam]
new_greetings = greetings(names)

# Task 3
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
numbers_positive = []


def get_list(list_numbers):
    try:
        for elem in list_numbers:
            if elem > 0:
                numbers_positive.append(elem)
                yield elem
    except:
        yield 0


for i in get_list(numbers):
    print(i)

# Task 4
sentence = "the quick brown fox jumps over the lazy dog"
count_list = []


def count(word, counting_list):
    try:
        a = word.split()
        for elem in a:
            if elem != "the":
                counting_list.append(len(elem))
        yield counting_list
    except:
        yield 0


for i in count(sentence, count_list):
    print(i)

languages = input("Enter language RU/EU: ").upper()
message = input("Enter message: ").upper()
move = int(input("Enter shift: "))


def cesar_encode(word, shift, language="EU"):
    alphabet_EU = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    encode = ""
    if language == "EU":
        for char_eu in word:
            place = alphabet_EU.find(char_eu)
            shift_place = place + shift
            encode += alphabet_EU[shift_place]
    else:
        for char_eu in word:
            place = alphabet_RU.find(char_eu)
            shift_place = place + shift
            encode += alphabet_RU[shift_place]

    return encode


def cesar_decode(word, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    decode = ""

    for char_eu in word:
        place = alphabet.find(char_eu)
        shift_place = place - shift
        decode += alphabet[shift_place]

    return decode


encode_mes = cesar_encode(message, move, languages)
decode_mes = cesar_decode(encode_mes, move)
print(encode_mes)
print(decode_mes)
