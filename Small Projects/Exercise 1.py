'''
https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''
name = input("What is your name: ")
age = int(input("How old are you: "))
current_year = int(input("What is the current year: "))
year = current_year - age + 100
print(name + ", you will be 100 years old in the year " + str(year))