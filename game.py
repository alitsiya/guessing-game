# Put your code here
import random

name = raw_input("Hello, what is your name? \n")
print "%s , I'm thinking of a number between 1 and 100. \
Try to guess my number. \n" % name

answer = random.randint(1 , 100)
num_of_guesses = 0
while True:
    guess = int(raw_input("Your guess? \n"))
    num_of_guesses += 1
    if guess > answer:
        print "Your guess is too high, try again."
    elif guess < answer:
        print "Your guess is too low, try again."
    else:
        print "Well done, %s! You guessed correcly! It's number %d! \
        Number of guesses is %d" % (name, answer, num_of_guesses)
        break

# finished!