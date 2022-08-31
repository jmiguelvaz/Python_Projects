import random

def run():
    lives= 5
    Random_Number = random.randint(1,100)
    Chosen_Number = int(input("Choose a number: "))
    while Chosen_Number != Random_Number:
        if Chosen_Number < Random_Number:
            lives -= 1
            print("pick a higher number")
        if Chosen_Number > Random_Number:
            print("pick a lower number")
            lives -= 1
        if lives == 0:
            print("GAME OVER")
            break

        print("you have " + str(lives) + " lives")
        Chosen_Number = int(input("Choose another number: "))
        
    if Chosen_Number == Random_Number:
        print("YOU WIN!")
    

if __name__=="__main__":
    run()