'''
https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
Take two lists and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.
'''

a = [1,2,2,3,4]
b = [2,3,3]
temp = []
for i in a:
    for j in b:
        if i == j and i not in temp:
            temp.append(i)

print(temp)