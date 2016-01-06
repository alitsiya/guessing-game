# Put your code here
from random import randint
import sys
import pdb

name = raw_input("Hello, what is your name? \n")

def ask_guess():
    guess = None
    while not guess:
        user_guess = raw_input("Your guess? \n")
        try:
            user_guess = int(user_guess)
        except ValueError:
            print "Hahahahhahahah. No way!"
            continue
        if user_guess > 0 and user_guess <= 100:
            return user_guess
        else:
            print "Hahahahhahahah. No way!"

def new_game():
    BEST_SCORE = sys.maxint
    game_played = False
    again = None

    while again == 'Y' or game_played == False:
        if again == "N":
            print "Good bye, %s" % name
            break
        else:
            game_played = True
            print "%s , I'm thinking of a number between 1 and 100. \
            Try to guess my number. \n" % name

            answer = randint(1 , 100)
            print answer #debugging cheat
            num_of_guesses = 0
            while True:
                guess = ask_guess()
                num_of_guesses += 1
                if guess > answer:
                    print "Your guess is too high, try again."
                elif guess < answer:
                    print "Your guess is too low, try again."
                else:
                    print "Well done, %s! You guessed correcly! It's number %d! \
                    # Number of guesses is %d. Best number of guesses is %d." % (name, answer, num_of_guesses, BEST_SCORE)
                    if BEST_SCORE > num_of_guesses:
                        BEST_SCORE = num_of_guesses
                    again = raw_input("Do you want to play the game again? Y/N ")
                    break


new_game()

# finished!