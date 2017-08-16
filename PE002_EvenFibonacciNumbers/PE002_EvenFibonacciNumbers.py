'''

'''
from math import pow
def evenFibonacciNumbers():
    a, b = 1, 1
    calculation = 0
    while a <= 4e6:
        if a % 2 == 0:
            calculation += a
        a, b = b, a + b
    return calculation

if __name__ == '__main__':
    print(evenFibonacciNumbers())
