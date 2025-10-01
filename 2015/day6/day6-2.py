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
    on = bytearray(10**6)
    for inst in instructions:
        x1,y1 = inst[1]
        x2,y2 = inst[2]
        width = y2-y1+1
        if inst[0]=='toggle':
            for x in range(x1,x2+1):
                idx_start = x*1000+y1
                idx_end = idx_start+width
                for idx in range(idx_start, idx_end):
                    on[idx] += 2
        elif inst[0]=='on':
            for x in range(x1,x2+1):
                idx_start = x*1000+y1
                idx_end = idx_start+width
                for idx in range(idx_start, idx_end):
                    on[idx] += 1
        elif inst[0]=='off':
            for x in range(x1,x2+1):
                idx_start = x*1000+y1
                idx_end = idx_start+width
                for idx in range(idx_start, idx_end):
                    if on[idx] > 0:
                        on[idx] -= 1
    return sum(on)

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

