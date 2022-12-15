import functools


def make_pretty(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print("I got decorated")
        return func(*args, **kwargs)

    return inner


@make_pretty
def ordinary():
    print("I am ordinary")


@make_pretty
def greet(name):
    """Prints a greeting"""
    print(f"Hello, {name}!")


@make_pretty
def decrement(nr, step=1):
    return nr - step


# ordinary = make_pretty(ordinary)  # ordinary = inner
# print(type(ordinary))
# print(ordinary)

ordinary()

greet("Ana")

dec = decrement(10, step=2)
print(dec)

print("greet's docstring:", greet.__doc__)
print("decrement's name:", decrement.__name__)
