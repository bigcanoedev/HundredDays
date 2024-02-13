import random

user_choice = input("Rock, Paper, or Scissors?")

#Rock = 0, Paper = 1, Scissors = 2
computer_choice = random.randint(0,2)

score = 0

while True:
    if user_choice == "Rock":
        if computer_choice == 0:
            print("Tie")
            user_choice = input("Rock, Paper, or Scissors?")
        elif computer_choice == 1:
            print("You Lose")
            break
        else:
            print("You Win!")
            user_choice = input("Rock, Paper, or Scissors?")
            score += 1
    elif user_choice == "Paper":
        if computer_choice == 0:
            print("You Win!")
            user_choice = input("Rock, Paper, or Scissors?")
            score += 1
        elif computer_choice == 1:
            print("Tie")
            user_choice = input("Rock, Paper, or Scissors?")
        else:
            print("You Lose")
            break
    elif user_choice == "Scissors":
        if computer_choice == 0:
            print("You Lose")
            break
        elif computer_choice == 1:
            print("You Win!")
            user_choice = input("Rock, Paper, or Scissors?")
            score += 1
        else:
            print("Tie")
            user_choice = input("Rock, Paper, or Scissors?")
    else:
        user_choice = input("Rock, Paper, or Scissors?")


print("Your score was: " + str(score))