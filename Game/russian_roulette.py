#status: Completed
#info: In this game, you will be held hostage and have to choose how many times you want to try before you die. Test your luck!
import random

def pick():
    n = int(input("How many times you want to try?: "))
    chambers = random.randint(1,6)
    die = chambers
    
    if n < die:
        print("You have survived!")
    elif n <= 0:
        print("PICK AGAIN!")
        return pick()
    else:
        print("FATALITY!")
pick()