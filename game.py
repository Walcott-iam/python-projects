import random

# this is scores
computer_score = 0
my_score = 0

round_score = 3

game_choices = ["rock", "paper", "scissor"]

print("Welcome to our mini RSP game!!!")

while True:
    my_choice = input("Put in your choice in this list " + str(game_choices) + "\n")
    computer_choice = random.choices(game_choices)
    print(type(computer_choice), computer_choice)
    computer_choice = computer_choice[0]
    print(type(computer_choice), computer_choice)
    
    print("You played " + my_choice + ", computer played: ", computer_choice)

    if my_choice == "rock" and computer_choice == "paper":
        print("Computer wins, You lost")
        computer_score = computer_score + 1
    elif my_choice == "paper" and computer_choice == "rock":
        print("You win, Computer lost")
        my_score = my_score + 1
    elif my_choice == "scissor" and computer_choice == "rock":
        print("Computer wins, You lost")
        computer_score = computer_score + 1
    elif my_choice == "rock" and computer_choice == "scissor":
        print("You win, Computer lost")
        my_score = my_score + 1
    elif my_choice == "paper" and computer_choice == "scissor":
        print("Computer wins, You lost")
        computer_score = computer_score + 1
    elif my_choice == "scissor" and computer_choice == "paper":
        print("You win, Computer lost")
        my_score = my_score + 1
    else:
        print("it's a tie")

    print("My score: " + str(my_score) + ", computer score is: " + str(computer_score))
    if my_score == round_score:
        print("I won the game")
        break
    elif computer_score == round_score:
        print("Computer won the game")
        break