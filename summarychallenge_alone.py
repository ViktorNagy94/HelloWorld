user_input = None
print("Please choose your option from the list below:")
options = ["Exit", "Learn python", "Learn java", "Go swimming", "Have dinner",
           "Go to bed"]
for x in range(len(options)):
    print("{}. {}".format(x, options[x]))
while user_input != 0:

    user_input = int(input("Your number here: "))
    if 0 < user_input <= 5:
        print("\nYour number was: {}".format(user_input))
    elif 0 != user_input > 5:
        print("Please choose your option from the list below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("4:\tHave a dinner")
        print("5:\tGo to bed")
        print("0:\tExit")
else:
    print("Your input was 0. Exiting now.")
