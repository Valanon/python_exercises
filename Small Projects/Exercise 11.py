'''
https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
Ask the user for a number and determine whether the number is prime or not.
'''
import math
def check_prime(number):
    if math.isnan(number):
        return "Ths is not a number."
    stop = int(math.sqrt(number))
    for i in range(2,stop+1):
        if number % i == 0:
            return str(number) + " is not a prime number."
    return str(number) + " is a prime number."

print(check_prime(int(input("What number would you like to check? "))))