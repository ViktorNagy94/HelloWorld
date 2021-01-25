for i in range(10, 0, -2):
    print("i is now: {}".format(i))

#Tehát a for a pythonban range-el (is) működik. Amikor egy bizonyos számsor
#alapján szeretnék végigiterálni egy tömböt akkor for i in range (0,20)
# kifejezéssel tudok a 0-19 elem között iterálni
#a kezdőérték beleszámít a végző nem. kezdőérték nélkül 0-tól indul.
#LEhet lépíésközt megadni, pl range(0,10,2) <- 0-9ig 2vel
#lehet visszafelé lépni,
# ilyenkor negatív lépés kell, ha megadjuk range(10,0,2) <. 10-1ig  2vel