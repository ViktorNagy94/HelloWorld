import random

highest = 1000
answer = random.randint(1,highest)
print(answer) #TODO: Remove after testing
guess = 0
print("Please guess a number between 1 and (quit with 0) {}: ".format(highest))


while guess != answer:
    guess=int(input())
    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else: #@guess must be greater than @answer
                print("Please guess lower")
