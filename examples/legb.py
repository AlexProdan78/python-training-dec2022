X = 100


def my_func(a):
    b = 10

    # print('id X inside function before shadowing', id(X))
    X = "ceva"
    # print('id X inside function after shadowing', id(X))

    def inner(c):
        d = 11

        print("Built-in names used in local (inner) scope:", int, len)
        print("Global names used in local (inner) scope:", X, my_func, MyClass)
        print("Enclosing names used in local (inner) scope:", a, b, inner)
        print("Local names used in local (inner) scope:", c, d, end="\n\n")

    inner(22)

    print("Built-in names used in local (my_func) scope:", int, ValueError, len)
    print("Global names used in local (my_func) scope:", X, my_func, MyClass)
    print("Local names used in local (my_func) scope:", a, b, inner, end="\n\n")


class MyClass:
    pass


if __name__ == "__main__":  # if current module is run
    print(f"Executable statements in {__name__}", end="\n\n")
    # print('id X global before function call', id(X))
    my_func(20)
    # print('id X global before after call', id(X))

    print("Built-in names used in global scope:", int, ValueError, len)
    print("Global names used in global scope:", X, my_func, MyClass)
