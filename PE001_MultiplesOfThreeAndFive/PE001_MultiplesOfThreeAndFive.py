'''
Multiples of Three and Five
Find the sum of all the multiples of 3 or 5 below 1000.
'''

def multiplesOfThreeAndFive():
    calculation = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            calculation += i
    return calculation

if __name__ == '__main__':
    print(multiplesOfThreeAndFive())
