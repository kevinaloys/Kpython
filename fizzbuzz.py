# coding: utf-8
# FizzBuzz

# Given an integer number N

# Your task is to

#     write a function that prints to the standard output (stdout) the numbers from 1 to N (one per line) with the following restrictions
#         for multiples of three print “Fizz” instead of the number
#         for the multiples of five print “Buzz” instead of the number
#         for numbers which are multiples of both three and five print “FizzBuzz”

# Note that your function will receive the following arguments:

#     n
#         which is the integer number described above

# Data constraints

#     the maximum value of N will not exceed 1000

# Efficiency constraints

#     your function is expected to print the result in less than 2 seconds
def fizzbuzz(n):

    for i in range(1,n+1):
        if(i % 15==0):
            print "FizzBuzz"
        elif(i % 5==0):
            print "Buzz"
        elif(i % 3==0):
            print "Fizz"
        else:
            print i

fizzbuzz(50)
