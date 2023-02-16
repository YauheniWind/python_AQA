import core.hw_3.hw3
from core.hw_4 import variables
from core.hw_4 import strings
from core.hw_4 import lists
from core.hw_4 import logical_operators
from core.hw_4 import dictionaries
from core.hw_4 import type_conversions
from core.hw_4 import conditions
from core.hw_4 import loop_for
from core.hw_4 import loop_while

# HW_3
print(core.hw_3.hw3.change_to_int(1.6))
print(core.hw_3.hw3.change_to_int(2.99))
print(core.hw_3.hw3.change_symbol("www.my_site.com#about", "#", "/"))
print(core.hw_3.hw3.add_ing("run"))
print(core.hw_3.hw3.reverse_string("Ivanov Ivan"))
print(core.hw_3.hw3.delete_space("    Hello world    "))
print(core.hw_3.hw3.string_in_other_string("employ", "employment"))
print(core.hw_3.hw3.uniq_number([1, 5, 2, 9, 2, 9, 1]))

# HW_4_variables
print(variables.big_int(10, 3.5))
print(variables.reduction(8.4, 1))
print(variables.division(10, 84))
print(variables.string_var("No", "Yes"))

# HW_4_strings
print(strings.change_string("HelloWorld"))
print(strings.long_string("HelloMyNameIsEv"))
print(strings.name_in_string("Ev"))
print(strings.trying("Hello world!"))

# HW_4_lists
print(lists.change_list(["Ev", "Rick", "Amanda"], [22, 54, 89]))
print(lists.join_lists(["Ev", "Rick", "Amanda"], [22, 54, 89]))
print(lists.slice_list(lists.join_lists(["Ev", "Rick", "Amanda"], [22, 54, 89])))
print(lists.add_elements(lists.slice_of_list, 34, "Nikita"))
print(lists.intersection_list(lists.a, lists.b))
print(lists.uniq_list(lists.uniq))

# HW_4_logical_operators
print(
    logical_operators.true_operations(
        logical_operators.number_one, logical_operators.number_two, 9, 7
    )
)
print(
    logical_operators.false_operations(
        logical_operators.number_one, logical_operators.number_two, 50, 70
    )
)
print(
    logical_operators.true_or_operation(
        logical_operators.number_one, logical_operators.number_two, 9, 7
    )
)
print(
    logical_operators.false_or_operation(
        logical_operators.number_one, logical_operators.number_two, 50, 7
    )
)
print(
    logical_operators.try_str(
        logical_operators.string_one, logical_operators.string_two
    )
)

# HW_4_dictionaries
print(dictionaries.count_people(dictionaries.school))
print(dictionaries.change_students(dictionaries.school, "1a", 2))
print(dictionaries.add_class(dictionaries.school, "1z", 65))
print(dictionaries.clear_class(dictionaries.school, "1z"))

# HW_4_type_conversions
print(type_conversions.string_to_array(type_conversions.robin_name))
print(
    type_conversions.greeting(
        type_conversions.ivan_name,
        type_conversions.name_of_city,
        type_conversions.name_of_country,
    )
)
print(type_conversions.join_strings(type_conversions.love_list))
print(type_conversions.insert_and_pop_element(type_conversions.somthing_list, 1, 4, 6))
print(
    type_conversions.reunion(
        type_conversions.a, type_conversions.b, type_conversions.ab
    )
)
print(type_conversions.count_letter(type_conversions.sometext))

# HW_4_conditions
print(conditions.add(10))
print(
    conditions.count_positive_numbers(
        conditions.counter,
        conditions.number_one,
        conditions.number_two,
        conditions.number_three,
    )
)
print(conditions.counting_year(conditions.year))
print(conditions.what_day_is_it_today(conditions.day))
print(
    conditions.body_weight_in_kilo(
        conditions.unit_of_measurement, conditions.body_weight
    )
)

# HW_4_loop_for
print(loop_for.plus_in_range(loop_for.first_number, loop_for.second_number))
print(loop_for.winner(loop_for.dict_of_swim))

# HW_4_loop_while
print(loop_while.number_product(5))
print(loop_while.area_calculation(loop_while.s1, loop_while.s2))
print(loop_while.count_number(123))
print(loop_while.range_between(2, 40))