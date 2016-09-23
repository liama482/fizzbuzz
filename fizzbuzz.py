"""
fizzbuzz.py
Author: Liam
Credit: 

Assignment:

Write a program that prints the numbers from 1 to 100. But for 
multiples of three print “Fizz” instead of the number and for 
the multiples of five print “Buzz”. For numbers which are multiples 
of both three and five print “FizzBuzz”.

We will use a variation of this test in which the last number of 
the series isn't necessarily 100, and the two numbers being tested 
for multiples aren't necessarily three and five. For example, your 
program should behave just like this:

How many numbers shall we print? 25
For multiples of what number shall we print 'Fizz'? 3
For multiples of what number shall we print 'Buzz'? 5
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
"""

b = input("How many numbers shall we print? ")
fizz = input ("For multiples of what number shall we print 'Fizz'? ")
buzz = input("For multiples of what number shall we print 'Buzz'? ")
b=int(b)
f=int(fizz)
bz=int(buzz)

for n in range (1,b):
    if n%fizz != 0 and n%buzz != 0:
        print(n)
    else:
        if n%fizz == 0 and n%buzz != 0:
            print("Fizz")
        if n%fizz != 0 and n%buzz == 0:
            print("Buzz")
        #if n%fizz == 0 and n%buzz == 0:
            #print("FizzBuzz")

#if temperature < 55 and weather == "raining":
 #   print("You should bring a warm raincoat.")
