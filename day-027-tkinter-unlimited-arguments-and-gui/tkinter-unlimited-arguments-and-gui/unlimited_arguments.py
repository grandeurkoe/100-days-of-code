# To pass unlimited positional arguments to a function we use *args as a parameter in the called function.
# Here *args is a tuple.
def add(*args):
    sum_of_numbers = 0
    for number in args:
        sum_of_numbers += number
    print(f"Sum : {sum_of_numbers}")


# To pass unlimited keyword arguments to a function we use **kwargs as a parameter in the called function.
# Here **kwargs is dictionary.
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(f"Result: {n}")


add(3, 4, 5, 6, 7, 8)
calculate(3, add=5, multiply=6)
