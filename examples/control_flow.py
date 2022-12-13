grade = 4

if grade == 10 or grade > 20:
    print('Wow! Maximum grade!')
elif grade >= 7:
    print('Good job!')
elif grade >= 5:
    print('You could have done better.')
else:
    print('Oh, no! :(')

match grade:
    case 10:
        print("Congrats!")
    case 9:
        print("Almost perfect!")
    case 8:
        print("Pretty good!")
    case 7:
        print("Good!")
    case _:
        print("All other values")
