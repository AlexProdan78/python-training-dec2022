# standard library imports
import sys

# 3rd party package imports

# local imports
import legb  # import module
import pypackage.pymodule
# from pypackage import pymodule
# from pypackage.pymodule import func


print(f"Calling my_func from {legb.__name__}", end="\n\n")
legb.my_func(22)
print(legb.X, legb.MyClass)
print(sys.path)

pypackage.pymodule.func(10)

# from legb import my_func, X  # import specific names from module
#
# my_func(33)
# print(X)


# import legb as imported_module  # import module as alias
#
# imported_module.my_func(44)


# from legb import X as imported_constant  # import name from module as alias
#
# print(imported_constant)
