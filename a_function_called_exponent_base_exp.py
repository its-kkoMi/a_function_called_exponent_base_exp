# Assignment 5 - Exercise 15
# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer.

# Ask user for base and exponent

base = int(input("Enter a base number: "))
exponent = int(input("Enter an exponent: "))

# Use a while loop

def power(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    return result

# Print output

print(base, "raised to the power of", exponent, "is", power(base, exponent))