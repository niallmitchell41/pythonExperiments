# title : parrot gussing game
# by niall mitchell
# guess parrots age
# between 1 and 20
# 5 guesses
# you get the parrot if win


# title
print ("*" * 80 )
print ("PARROT GUESSING GAME")
print("*" * 80)

#instructions

import random


player_name = input ("Please Enter Your Name : ")
player_age = input ("Please Enter your Age :")


instructions = """
You walk imto an old smelly pet shop.
As the door closes behind you, you see
a beautiful blue parrot sitting very
still in a cage. the pet shop owner
greets you and says,
"Today is your lucky day!
this is the rare Norwegian Blue Parrot.

Guess his age and take him home for free pounds!!



You get six guesses."
"""
print (instructions)

number_of_guesses = 0

# parrots age
# todo : make this automatically pick a random number between 1 and 10
parrot_age = random.randint (1,10)


# while loop will repeat until the number of guesses is 10


while number_of_guesses < 6:


    # get a guess
    # todo :need to repeat six times
    guess = input ("Guess the age of the parrot [pick a number from 1 to 10] : ")
    guess = int (guess)

    # add one to our guest counter
    number_of_guesses = number_of_guesses + 1

    # check if guess is right
    if guess == parrot_age:
        print ("Congratulations " + player_name + " You Win! Enjoy your parrot £3.00 please")
        print ("you: what!!")
        break
    
    else:
        print ("wrong! you obviously  are dumb")
        print ("did you say you were " + player_age + " , You must be kidding , TRY AGAIN")


    # check if this is fifth guess
    # if true, tell them they lose and reveal parrots age

    if number_of_guesses == 6:
        print ("you lose")
        print ("the parrots age is " + str (parrot_age))

# stop indenting (This marks the end of the loop)
print ("Thankyou for playing " + player_name )
       

