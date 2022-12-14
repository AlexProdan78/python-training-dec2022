def my_func():
    print('Hello!')


def get_name():
    return 'Ana'


print('my_func returns:', my_func())  # doesn't return a value
name = get_name()  # returns a value
print(name)


def decrement(nr, step=1):
    return nr - step


# def decrement(nr: int, step: int = 1):  # type hints
#     return nr - step


print(decrement(10))
print(decrement(10, 2))  # call with positional arguments
print(decrement(step=2, nr=10))  # call with keyword arguments

# print(decrement({1, 2, 3}, {3, 4}))


def varargs(*args, **kwargs):
    print("args =", args, type(args))
    print("kwargs =", kwargs, type(kwargs))
    name = kwargs.get("name")
    print("name type:", type(name))
    print()


varargs()
varargs(10)
varargs(10, 20, 70, 100)

varargs(name="Ana")
varargs(age=20)

varargs(10, 20, 40, name="Ana", age=15)
