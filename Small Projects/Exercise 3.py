'''
https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
Take a list and write a program that prints out all the elements of the list that are less than 5.
'''

list = int(input("What is your number: "))
temp = []
for n in list:
    if n < 5:
        temp.append(n)

print(temp)
