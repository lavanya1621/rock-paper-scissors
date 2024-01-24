import random
choices = ["Rock", "Paper", "Scissors"]
choice = random.choice(choices)
player= False
score = 0
while True:
    player = input("Rock Paper Scissors!!!")
    
    if player == choice:
        print("Tie!")
    elif player == "Rock":
        if choice == "Paper":
            print("whoopsiee, better luck next", choice, "kills", player)
            
        else:
            print("yayyy you won", player, "smashes", choice)
            score+=1
    elif player == "Paper":
        if choice == "Scissors":
            print("oops you lost hehe", choice, "cut", player)
            
        else:
            print("Yayyy you win", player, "kills", choice)
            score+=1
    elif player == "Scissors":
        if choice == "Rock":
            print("oops you lost hehe", choice, "smashes", player)
           
        else:
            print("You win!", player, "cut", choice)
            score+=1
    elif player=='End':
        print("Your Score")
       
        print(score)
        break