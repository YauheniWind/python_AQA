var_int = 10
var_float = 8.4
var_str = "No"

big_int = var_int * 3.5
var_float -= 1

var_int /= var_float
big_int /= var_float

var_str += "No" + "Yes" * 3

print(
    f"""var_int: {var_int}
var_float: {var_float}
var_str: {var_str}
big_int: {big_int}
            """
)
