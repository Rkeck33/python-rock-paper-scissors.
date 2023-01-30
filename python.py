#Rock, Paper, Scissors - Ryan
import random
while True:
    R_P_S = input("select rock, paper, or scissors:")
    #print(R_P_S)

    choices=['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    #print(choices)

    if R_P_S == 'rock' and 'computer_choice' == 'rock':
        print('tie')
    if R_P_S == 'paper' and 'computer_choice' == 'paper':
        print('tie')
    if R_P_S == 'scissors' and 'computer_choice' == 'scissors':
        print ('tie')
    elif R_P_S == 'rock':
        if computer_choice == 'scissors':
            print("Rock smashes scissors! You win!")
        else:
            print('paper covers rock you lose')
    elif R_P_S == "paper":
        if computer_choice == "rock":
            print("paper covers rock you win")
        else:
            print("scissors cuts paper you lose")
    elif R_P_S == ("scissors"):
        if computer_choice == "paper":
            print("scissors cuts paper you win")
        else:
            print("rock smashes scissors you lose")
        
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
     break