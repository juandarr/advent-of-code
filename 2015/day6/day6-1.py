from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402

def parseInformation(filename):
    file = open(filename, "r")
    data = file.read()
    rawInstructions = [s.split(' ') for s in data.rstrip().split('\n')]
    instructions = [[i[1],[int(v) for v in i[2].split(',')],[int(v) for v in i[4].split(',')]] if len(i)==5 else [i[0],[int(v) for v in i[1].split(',')], [int(v) for v in i[3].split(',')]] for i in rawInstructions]
    return instructions


def computeLights(instructions):
    on = {}
    for inst in instructions:
        x1,y1 = inst[1]
        x2,y2 = inst[2]
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                if (x,y) in on:
                    if inst[0]=='off' or inst[0]=='toggle':
                        del on[(x,y)]
                    else:
                        pass
                else:
                    if inst[0]=='off':
                        pass
                    else:
                        on[(x,y)]=1
    return len(on)

def main(filename):
    instructions = parseInformation(filename)
    lightsOn = computeLights(instructions)
    return lightsOn

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2015, 6, [10**6,10**3,0], main)
    else:
        code = getAnswer(2015, 6, main)
        print("The number of lights lit is {0}".format(code))

