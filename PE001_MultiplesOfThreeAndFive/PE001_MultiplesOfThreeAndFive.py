'''

'''

def multiplesOfThreeAndFive():
    calculation = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            calculation += i
    return calculation

if __name__ == '__main__':
    print(multiplesOfThreeAndFive())
