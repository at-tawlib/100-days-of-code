# Modify add function to take an unlimited number of arguments.
# Use loop to sum_args all the arguments inside the function.
def add(*args):
    """function with multiple arguments (positional arguments)"""
    sum_args = 0
    for arg in args:
        sum_args += arg
    return sum_args


print(add(2, 4, 5, 6, 6, 7, 7, 7))


def calculate(n, **kwargs):
    """keyword arguments"""
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


print(calculate(2, add=3, multiply=5))


class Car:
    def __init__(self, **kw):
        # it's better to use get coz it returns none if the key is not available
        # using the key index "kw["make"] causes error if the key is not found
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(f"{my_car.model}, {my_car.colour}, {my_car.make}")
no_car = Car()
print(f"{no_car.model}, {no_car.colour}, {no_car.make}")
