'''
https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
(Hint: remember to use the user input lessons from the very first exercise)
'''
import random

secret_number = random.randint(1,9)
guess = int(input("Guess a number between 1 and 9: "))
while guess != secret_number:
    if guess < secret_number:
        guess = input("Too low, guess again (or type exit to exit). ")
    else:
        guess = input("Too high, guess again (or type exit to exit).")
    if guess == "exit":
        break
    else:
        guess = int(guess)
print("The number was " + str(secret_number) + ".")