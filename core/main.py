import hw_3
import hw_4

# HW_3
print("-------HW_3-------")
print(hw_3.change_to_int(1.6))
print(hw_3.change_to_int(2.99))
print(hw_3.change_symbol("www.my_site.com#about", "#", "/"))
print(hw_3.add_ing("run"))
print(hw_3.reverse_string("Ivanov Ivan"))
print(hw_3.delete_space("    Hello world    "))
print(hw_3.string_in_other_string("employ", "employment"))
print(hw_3.uniq_number([1, 5, 2, 9, 2, 9, 1]))

print("-------HW_4-------")
# HW_4_variables
print(hw_4.big_int(10, 3.5))
print(hw_4.reduction(8.4, 1))
print(hw_4.division(10, 84))
print(hw_4.string_var("No", "Yes"))
# HW_4_strings
print(hw_4.change_string("HelloWorld"))
print(hw_4.long_string("HelloMyNameIsEv"))
print(hw_4.name_in_string("Ev"))
print(hw_4.trying("Hello world!"))

# HW_4_lists
print(hw_4.change_list(["Ev", "Rick", "Amanda"], [22, 54, 89]))
print(hw_4.join_lists(["Ev", "Rick", "Amanda"], [22, 54, 89]))
print(hw_4.slice_list(hw_4.join_lists(["Ev", "Rick", "Amanda"], [22, 54, 89])))
print(hw_4.add_elements(hw_4.slice_of_list, 34, "Nikita"))
print(hw_4.intersection_list(hw_4.a, hw_4.b))
print(hw_4.uniq_list(hw_4.uniq))

# HW_4_logical_operators
print(hw_4.true_operations(hw_4.number_one, hw_4.number_two, 9, 7))
print(hw_4.false_operations(hw_4.number_one, hw_4.number_two, 50, 70))
print(hw_4.true_or_operation(hw_4.number_one, hw_4.number_two, 9, 7))
print(hw_4.false_or_operation(hw_4.number_one, hw_4.number_two, 50, 7))
print(hw_4.try_str(hw_4.string_one, hw_4.string_two))

# HW_4_dictionaries
print(hw_4.count_people(hw_4.school))
print(hw_4.change_students(hw_4.school, "1a", 2))
print(hw_4.add_class(hw_4.school, "1z", 65))
print(hw_4.clear_class(hw_4.school, "1z"))

# HW_4_type_conversions
print(hw_4.string_to_array(hw_4.robin_name))
print(
    hw_4.greeting(
        hw_4.ivan_name,
        hw_4.name_of_city,
        hw_4.name_of_country,
    )
)
print(hw_4.join_strings(hw_4.love_list))
print(hw_4.insert_and_pop_element(hw_4.somthing_list, 1, 4, 6))
print(hw_4.reunion(hw_4.a, hw_4.b, hw_4.ab))
print(hw_4.count_letter(hw_4.sometext))

# HW_4_conditions
print(hw_4.add(10))
print(
    hw_4.count_positive_numbers(
        hw_4.number_one,
        hw_4.number_two,
        hw_4.number_three,
    )
)
print(hw_4.counting_year(hw_4.year))
print(hw_4.what_day_is_it_today(hw_4.day))
print(hw_4.body_weight_in_kilo(hw_4.unit_of_measurement, hw_4.body_weight))

# HW_4_loop_for
print(hw_4.plus_in_range(hw_4.first_number, hw_4.second_number))
print(hw_4.winner(hw_4.dict_of_swim))

# HW_4_loop_while
print(hw_4.number_product(5))
print(hw_4.area_calculation(hw_4.s1, hw_4.s2))
print(hw_4.count_number(123))
print(hw_4.range_between(2, 40))
