name = input("What's your name? ")

try:
    fifth_letter = name[5]
    if not fifth_letter.isalpha():
        raise ValueError("Name containing invalid characters.")
except IndexError as ex:
    print(f"Exception occurred: {ex}")
except ValueError as ex:
    print(f"Do something different with {ex}")
else:
    print("No exception")
finally:
    print("Executes every time")
