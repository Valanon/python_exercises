'''
https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
print(fibonacci(7))