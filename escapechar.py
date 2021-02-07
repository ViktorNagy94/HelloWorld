split_string = "This string has been\nsplit over\nseveral\nlines"
print(split_string)

tabbed_string = "1\t2\t3\t4\t5"
print(tabbed_string)

print('The pet shop owner said "No, no, \'e\'s uh,... he\'s resting".')

print("The pet shop owner said \"No, no, 'e's uh,... he's resting\".")

print("""The pet shop owner said "No, no, \
'e's uh,... he's resting".""")

another_split_string = """This string has been \
split over \
several \
lines"""

print(another_split_string)

# amennyiben használni szeretnénk a \ karaktert is (backslash)
# Ezt többféleképpen is megtehetjük.
# Az egyik a duplázás, másik a string előtti r,
# mintha rawstring lenne

print("C:\\Users\\nagyviktor\\notes.txt")
print(r"C:\Users\nagyviktor\notes.txt")
