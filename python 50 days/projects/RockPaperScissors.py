import random

def game():
    while True:
        print("If you want to exit the game enter 0")
        userdecision = int(input("1.rock, 2.paper, 3.scissors: "))
        
        if userdecision == 0:
            print("Thank you for playing the game")
            break
        
        systemdecision = random.choice(["rock", "paper", "scissors"])
        
        if userdecision == 1 and systemdecision == "rock":
            print("It is a draw, try again")
        elif userdecision == 1 and systemdecision == "paper":
            print("System wins")
        elif userdecision == 1 and systemdecision == "scissors":
            print("Congrats, You win")
        elif userdecision == 2 and systemdecision == "paper":
            print("It's a draw, try again")
        elif userdecision == 2 and systemdecision == "rock":
            print("Congrats, You win")
        elif userdecision == 2 and systemdecision == "scissors":
            print("System wins")
        elif userdecision == 3 and systemdecision == "paper":
            print("Congrats, You win")
        elif userdecision == 3 and systemdecision == "rock":
            print("System wins")
        elif userdecision == 3 and systemdecision == "scissors":
            print("It's a draw, try again")
        else:
            print("Invalid input, please try again")
  
game()
