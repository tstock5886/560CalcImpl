#!/usr/bin/python3

# Title: Travis' implementation of Nate's Basic Math Module
# Author: Travis Stockwell
# Date: 2019.11.08

import natemath

print ("Travis' magic python calculator\n")
print ("Let's test this python library\n")

print ("---- Addition ----\n")
print ("1 + 5 = "),
print (natemath.addValue(1,5))

print ("1.2 + 5.7 = "),
print (natemath.addValue(1.2,5.7))

print ("---- Subtraction ----\n")
print ("1 - 5 = "),
print (natemath.subValue(1,5))

print ("1.2 - 5.7 = "),
print (natemath.subValue(1.2,5.7))

print ("---- Multiplication ----\n")
print ("1 * 5 = "),
print (natemath.multiValue(1,5))

print ("1.2 * 5.7 = "),
print (natemath.multiValue(1.2,5.7))

print ("---- Division ----\n")
print ("1 / 5 = "),
print (natemath.divValue(1,5))
print ("Notice we have a type problem here where the integers passed in stayed integers and the built-in math library rounded the answer to 0.")

print ("1.2 / 5.7 = "),
print (natemath.divValue(1.2,5.7))

print ("---- Power ----\n")
print ("2 ^ 5 = "),
print (natemath.expValue(2,5))

print ("5 ^ -1 = "),
print (natemath.expValue(5,-1))

print ("---- Square Root ----\n")
print ("sqrt(100) = "),
print (natemath.sqrtValue(100))

print ("sqrt(3.3) = "),
print (natemath.sqrtValue(3.3))

print ("sqrt(3) = "),
print (natemath.sqrtValue(3))
