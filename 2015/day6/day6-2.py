from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    data = file.read()
    rawInstructions = [s.split(' ') for s in data.rstrip().split('\n')]
    instructions = [[i[1],i[2],i[4]] if len(i)==5 else [i[0],i[1], i[3]] for i in rawInstructions]
    return instructions

def computeLights(instructions):
    on = {}
    for inst in instructions:
        x1,y1 = map(lambda d: int(d),inst[1].split(',') )
        x2,y2 = map(lambda d: int(d),inst[2].split(',') )
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                if (x,y) in on:
                    if inst[0]=='off':
                        if on[(x,y)]>0:
                            on[(x,y)] -= 1
                    elif inst[0]=='on':
                        on[(x,y)] +=1
                    else:
                        on[(x,y)] +=2
                else:
                    if inst[0]=='off':
                        pass
                    elif inst[0]=='on':
                        on[(x,y)]=1
                    else:
                        on[(x,y)]=2
    total = 0
    for k in on:
        total += on[k]
    return total

def main(filename):
    instructions = parseInformation(filename)
    totalBrightness = computeLights(instructions)
    return totalBrightness

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2015, 6, [10**6,2*10**3,0], main)
    else:
        totalBrightness = getAnswer(2015, 6, main)
        print("The total brightness of all lights is {0}".format(totalBrightness))

