# Python 3 program to find factorial of given number
# Factorial of a non-negative integer,
# is multiplication of all integers smaller than or equal to n.
def factorial(num):
    fact = 1
    if num < 0:
        return 0
    elif num == 0 or num == 1:
        return 1
    else:
        while num > 1:
            fact *= num
            num -= 1
        return fact


while True:
    number = int(input("Enter the number: "))
    print("The factorial of",number,"is",factorial(number))


