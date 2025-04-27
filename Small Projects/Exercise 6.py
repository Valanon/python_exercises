'''
https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
'''

string = str(input("Please give a word: "))
length = int(len(string)/2)
isPalindrome = True
for i in range(length+1):
    if string[i] !=string[-(i+1)]:
        isPalindrome = False
        break
if isPalindrome:
    print("This word is a palindrome.")
else:
    print("This word is not a palindrome.")