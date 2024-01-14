from os.path import dirname, abspath, join
import sys
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from tests import performTests

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

def main(filename):
    calories = parseInformation(filename)
    biggest = maxCalories(calories)
    return biggest

if __name__=='__main__': 

    args = sys.argv[1:]
    if args[0]=='test':
        test = True
    elif args[0]=='main':
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(1,[24000],main,[])
    else:
        dir = dirname(__file__)
        filename = join(dir,'day1-input.txt')
        biggest = main(filename)        
        print("Biggest calorie amount is: {0}".format(biggest))