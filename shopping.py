shopping_list = ["milk","pasta","eggs","spam","bread","rice"]


for item in shopping_list:
    if item == "spam":
        continue  #IF you use this, it will jump back
        # to the beginning of the for, the following
        # code wont be executed
        #if you use BREAK, for will terminate
    print("Buy "+ item)