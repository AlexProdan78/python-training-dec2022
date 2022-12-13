"""
This is a docstring for script module. This module is used to exemplify some
basic concepts in Python.
"""

print("Hello world")
x = 10
print(x)

# Implicit line joining
my_shopping_list = [
    'apples',
    'bananas',
    'oranges',
    'pears',
    'peaches',
    'cherries',
]
print(my_shopping_list)
number_1 = (2131342 + 34234 + 352452 + 143131 +
            12312 + 134426 + 34162 + 31412 + 13542)
print(number_1)
multiline_str = """abs(x) (absolute value)
int(x) (conversion to integer)
float(x) (conversion to floating point)
complex(x, y) (creation of a complex number where x is real part and y imaginary part)
divmod(x, y) (creation of (x // y, x % y) pair)
pow(x, y) (x to the power y, the same as x ** y)"""
print(multiline_str)

# Explicit line joining ("\" used as line continuation character)
text = "if we have a long logical line, we can split it into physical lines by"\
       " using the backslash at the end of the line so that Python understands"\
       " that the next physical line should be considered as part of the"\
       " current logical line."
print(text)
number_2 = 2131342 + 34234 + 352452 + 143131 + \
           12312 + 134426 + 34162 + 31412 + 13542
print(number_2)

if x > 0:
    print("Over 0")
    print("Still inside if")


print("Outside if")

print("Built-in function sum:", sum((10, 20, 40)))

sum = 0  # shadowing - not recommended
sum += 1
sum += 10
print(sum)

# print("Built-in function sum:", sum((10, 20, 40)))
