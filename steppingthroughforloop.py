number = input("Please enter a series of numbers using any separators you like: ")
separators = ""
for char in number:
    if not char.isnumeric(): #Ha a char változó értéke nem szám akkor lépünk bele ebbe az ifbe!
        separators = separators + char
#print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))

#values = "".join(char if char not in separators else " " for char in number).split()
#print([int(val) for val in values])
