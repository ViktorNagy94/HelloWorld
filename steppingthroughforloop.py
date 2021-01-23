number = "9,223;372:036 854,775;807"
separators = ""
for char in number:
    if not char.isnumeric(): #Ha a char változó értéke nem szám akkor lépünk bele ebbe az ifbe!
        separators = separators + char
print(separators)


#values = "".join(char if char not in separators else " " for char in number).split()
#print([int(val) for val in values])
