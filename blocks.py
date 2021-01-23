name = input("Please enter your name: ")
age = int(input("How old are you, {0}?".format(name)))
print(age)

# if age >= 18:  # if a pythonban
#     print("You are old enough to vote")
#     print("Please put an x in the box")
# else: #else
#     print("You are too young to vote. Please come back in {0} years".format(18 - age))

if age < 18:
    print("You are too young to vote. Please come back in {0} years".format(18 - age))
elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi")
else:
    print("You are old enough to vote")
    print("Please put an x in the box")