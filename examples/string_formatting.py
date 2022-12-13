greeting = "hello"
name = "ana"
formatted_string = f"{greeting.capitalize()}, my name is {name[0].upper()}"
print(formatted_string)

hour = 2
minute = 30
print(f"{hour:0>2}:{minute:0>2}")

price = 12241.354
print(f"Price is {price:.2f}$")
print(f"Price is {price:.4f}$")

nr = 15
print(f"Hex: {nr:x}")
print(f"Oct: {nr:o}")
print(f"Bin: {nr:b}")
