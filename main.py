from Multiple_Function import MultipleFunction
from Point import Point

function_input = input("Please enter your function: ")
function = MultipleFunction(function_input)

is_variables = input("Does your function finally have 3 variables?(y/n): ")

if is_variables.lower() == "y":
    x = int(input("Please enter x: "))
    y = int(input("Please enter y: "))
    z = int(input("Please enter z: "))

    point = Point(x, y, z)

    print(function.get_gradian())
    print(function.get_gradian_value(point).show())

elif is_variables.lower() == "n":
    n = int(input("Please enter the number of symbols: "))

    i = n

    symbols = []
    while i > 0:
        symbol = input("please enter the symbols (one by one): ")
        symbols.append(symbol)
        i -= 1

    i = n

    parameters = []
    print("Please enter the point parameters (one by one): ")
    while i > 0:
        parameter = input("Parameter: ")
        parameters.append(parameter)
        i -= 1

    point = Point()
    point.set_multi(parameters)

    function.set_symbols(symbols)
    print(function.get_gradian_n_value(point).show_multi())
