"""Control Modules and Functions"""
"""Built-in module"""

import math as m

print("_____BUILT-IN MODULE_____")
num:int = 49
num_sq_rt = m.sqrt(num)
print("Square root of '49':  ", num_sq_rt)


print("Enter a number to calculate it's square root.")
num = (float(input()))
print(f"Square root of {num} is:" , m.sqrt(num))
print()

"""User-defined module"""

import greetings

print("_____USER-DEFINED MODULE_____")
name = input("Enter your name:\t")
greetings.say_hello(name)
print()

"""Third-party modules"""
print("_____THIRD-PARTY MODULE_____")
import numpy as np

Array_A = np.array([[2,3] , [5,4]])
Array_B = np.array([[[6,3] , [2,4]]])
Product_Array = Array_A@Array_B

print("Array_A:\n" , Array_A)
print("Array_B:\n" , Array_B)
print("Product of two arrays:\n" , Product_Array)
print()


"""Exception Handling"""
print("____EXCEPTION HANDLING______")
try:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    result = num1 / num2
    print("Result:" , int(result))
except ZeroDivisionError:
    print("Can't divided by zero" , ZeroDivisionError)
except ValueError:
    print("Please enter valid numbers!")