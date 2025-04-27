'''
https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
'''

def remove_duplicates(list):
    return [i for i in set(list)]

print(remove_duplicates([1,1,2,3,5]))