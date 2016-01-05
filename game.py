# Put your code here
from random import randint

name = raw_input("Hello, what is your name? \n")

def ask_guess():
    while True:
        try:
            guess = int(raw_input("Your guess? \n"))
            break
        except ValueError:
            print "Hahahahhahahah. No way!"
    if guess > 0 and guess <= 100:
        return guess
    else:
        print "Hahahahhahahah. No way!"
        ask_guess()

def new_game():
    print "%s , I'm thinking of a number between 1 and 100. \
    Try to guess my number. \n" % name

    answer = randint(1 , 100)

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
            Number of guesses is %d" % (name, answer, num_of_guesses)
            break
    again = raw_input("Do you want to play the game again? Y/N ")
    if again == "Y":
        new_game()
    else: 
        print "Good bye, %s" % name

new_game()

# finished!