'''
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''
#from math import pow
num = 600851475143

#num = 13195
def largestPrimeFactor(n):
    divisor = 3
    ans = []
    while  n >= divisor:
        if n % divisor == 0:
            n /= divisor
            ans.append(divisor)
            #print(divisor)
        divisor += 1
    return ans


if __name__ == '__main__':
    print(*largestPrimeFactor(num))
