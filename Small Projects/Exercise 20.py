'''
https://www.practicepython.org/exercise/2014/11/11/20-element-search.html
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
'''

def search(list, item):
    for _ in list:
        if _ == item:
            return True
        elif _ > item:
            return False
        
print(search([0,1,2,3],4))