'''
https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
'''
a = [1,2,4,5,7]
evens = [i for i in a if i % 2 == 0]

print(evens)