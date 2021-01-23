name = input("Please type in your name: ")
age = int(input("Please type in your age: "))
if 18<= age < 31:
    print("Welcome to the holiday {}, enjoy yourself".format(name))
else:
    print("Sorry, you are refused to entry")
