'''
https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
'''

number = int(input("What is your number: "))
if (number%2==0):
    if (number%4==0):
        print("Your number is divisible by four")
    else:
        print("Your number is even.")
else:
    print("Your number is odd.")