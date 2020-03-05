#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

print(factorial_recursive(4))



"""
## my crappy attempt to do recursion for factorial that failed miserably
total = 0
def factorial(num):
    currentNumber = num
    nextNumber = num - 1
    if (nextNumber != 0):
        total = currentNumber * nextNumber
        factorial(nextNumber) 
    return total

findFactorial = factorial(10)
print(f"findFactorial is {findFactorial}")
"""