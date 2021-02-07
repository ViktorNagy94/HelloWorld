numbers = [1, 25, 31, 16, 60]

for number in numbers:
    if number % 8 == 0:
        #reject the list
        print("The numbers are unacceptable")
        break
else: #Ebbe az else ágba CSAK AKKOR lépünk bele, ha a for lefutott az
    #összes értékre és nem volt elfogadhatatlan input
    print("All those numbers are fine")