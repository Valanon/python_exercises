'''
https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
'''

def reverse(string):
    return " ".join([i for i in string.split()[::-1]])

print(reverse("hi how are you"))