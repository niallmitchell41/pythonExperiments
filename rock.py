# Nialls rock paper scissors game
# By Niall Mitchell 26th dec 2016

import random
play_again = "yes"
choices = ["rock","paper","scissors"]

#title
title = "rock, paper, scissors --- by Niall Mitchell"
print ("*" * 80 )
print (title)
print ("*" * 80 )

print (" Let's play the classic game!!")

# get player to make choices

while play_again == "yes":
    print ("choose rock, paper, or scissors: ")
    player_choice = input ("enter your choice : ")
    computer_choice = choices[random.randint(0,2)]

    print ("Your choice is " + player_choice + ".")
    print ("The computer's choice is " + computer_choice + ".")

    if player_choice == computer_choice:
        print ("IT'S A DRAW")

    else:
        if ((player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "scissors" and computer_choice == "paper") or
            (player_choice == "paper" and computer_choice == "rock")):
             print ("!" * 80)
             print ("YOU WIN!!")
             print ("!" * 80)

        else:
             print (":(" * 40)
             print ("YOU LOSE!!!")
             print (":(" * 40)

    play_again = input ("Do you want to play again [yes/no]? ")
             

