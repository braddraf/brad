import random
print("Choose: rock, paper, scissor")
lives = 3
while lives > 0:
    Player1 = input("Player: ")
    Computer = random.choice(["rock","paper","scissor"])
    print("Computer: " + Computer)
    if Player1 == "paper" and Computer == "rock":
        print("PLAYER 1 WINS")
        break
    elif Player1 == "scissor" and Computer == "paper":
        print("PLAYER 1 WINS")
        break
    elif Player1 == "rock" and Computer == "scissor":
        print("PLAYER 1 WINS")
        break
    elif Player1 == Computer:
        print("TIE")
        break
    else:
        print("COMPUTER WINS")
        lives = lives - 1
        print()
else:
    print("PLAYER 1 GAME OVER")