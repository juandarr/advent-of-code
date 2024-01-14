from os.path import dirname, abspath
import sys
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from utils import performTests, getAnswer

def parseInformation(filename):
    file = open(filename, "r")
    calories = file.read()
    calories = calories.rstrip().split('\n\n')
    return list(map(lambda c: map(int,tuple(c.split('\n'))), calories))

def max3Calories(calories):
    biggest3 = [0, 0, 0]
    current = 0
    for group in calories:
        current = 0
        for calorie in group:
            current += calorie
        for idx, val in enumerate(biggest3):
            if (val < current):
                for i in range(2,idx,-1):
                    biggest3[i] = biggest3[i-1]
                biggest3[idx] = current
                break
    return biggest3

def main(filename):
    calories = parseInformation(filename)
    biggest3 = max3Calories(calories)
    return sum(biggest3)

if __name__=='__main__': 
    args = sys.argv[1:]
    if args[0]=='test':
        test = True
    elif args[0]=='main':
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(1,[45000],main)
    else:
        biggest = getAnswer(1, main)       
        print("Total sum is {0}".format(biggest))
