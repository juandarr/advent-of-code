import os
import sys

def parseInformation(filename):
    file = open(filename, "r")
    calories = file.read()
    calories = calories.rstrip().split('\n\n')
    return list(map(lambda c: map(int,tuple(c.split('\n'))), calories))

def maxCalories(calories):
    biggest = 0
    for group in calories:
        current = 0
        for calorie in group:
            current += calorie
            if (biggest < current):
                biggest = current
    return biggest

if __name__=='__main__': 

    args = sys.argv[1:]
    if args[0]=='test':
        test = True
    elif args[0]=='main':
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    dirname = os.path.dirname(__file__)
    if test:
        filename = os.path.join(dirname, 'day1-test-input.txt')
    else:
        filename = os.path.join(dirname, 'day1-input.txt')
    calories = parseInformation(filename)
    biggest = maxCalories(calories)
    print("Biggest calorie amount is: {0}".format(biggest))
