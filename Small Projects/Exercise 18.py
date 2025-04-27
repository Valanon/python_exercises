'''
https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html
Create a program that will play the “cows and bulls” game with the user. The game works like this:
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout the game and tell the user at the end.
'''
import random

def check_guess(num, guess):
    num = str(num)
    guess = str(guess)
    cows = 0
    bulls = 0
    for i in range(len(num)):
        if num[i] == guess[i]:
            cows += 1
        elif guess[i] in num:
            bulls += 1
    return (cows,bulls)

def game():
    number = random.randint(1000,9999)
    guesses = 0
    print("Guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a cow. For every digit the user guessed correctly in the wrong place is a bull.")
    while True:
        guess = int(input("enter a 4 digit guess: "))
        (a,b) = check_guess(number, guess)
        guesses += 1
        if a == num:
            break
        else:    
            print(str(a) + " cows and " + str(b) + " bulls")
    print("You got it, it took " + str(guesses) + " guesses")

game(4)