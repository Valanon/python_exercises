'''
https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
'''

def list_ends(list):
    return [list[0],list[-1]]

print(list_ends([1,2,3]))