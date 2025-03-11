import random

def start_game():
    result = random.randint(1,100)
    print("total change for win = 10 ")
    for i in range(1,11):
        guss = int(input("Guess the number (in range 1-100) :"))
        if result == guss:
            return " Congrats You Win "
        elif result < guss:
            print(f"too high..\n remain chance {10-i}")
        elif result > guss:
            print(f"too low..\n remain chance {10-i}")
        else:
            print("Invalid Input \n Try again...")
    print("You Lose \n Game Over ")

print(start_game())