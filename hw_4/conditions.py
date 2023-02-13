number_plus_one = 10

if number_plus_one > 0:
    number_plus_one += 1

print(number_plus_one)

number_one = 2
number_two = 5
number_three = -10
counter = 0

if number_one > 0:
    counter += 1
if number_two > 0:
    counter += 1
if number_three > 0:
    counter += 1

print(f"Positive numbers: {counter}")

year = int(input("Enter number of year: "))
if year % 4 != 0:
    print('365')
elif year % 100 != 0:
    print('366')
elif year % 400 != 0:
    print('365')
else:
    print('366')

day = int(input("Enter number in range 1-7: "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Out of range")

unit_of_measurement = int(input("Enter unit of measurement: "))
body_weight = int(input("Enter body weight: "))

match unit_of_measurement:
    case 1:
        print(body_weight)
    case 2:
        print(body_weight / 1000000)
    case 3:
        print(body_weight / 1000)
    case 4:
        print(body_weight * 1000)
    case 5:
        print(body_weight * 100)
    case _:
        print("Out of range")