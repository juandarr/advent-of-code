from os.path import dirname, abspath, join
import sys
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from utils import performTests, getAnswer

def parseInformation(filename):
    file = open(filename, "r")
    tmp= file.read()
    tmp= tmp.rstrip().split('\n')
    return tmp

def checkPartialOverlap(ranges):
    overlaps = 0
    for pair in ranges:
        # Format data for adequate comparison
        elfs = pair.split(',')
        for idx, elf in enumerate(elfs):
            elf = elf.split('-')
            elfs[idx] = [int(elf[0]), int(elf[1])]
        # If one range is inside the other range, increase variable overlaps
        if not((elfs[0][0]<elfs[1][0] and elfs[0][1]<elfs[1][0]) or (elfs[0][0]>elfs[1][1] and elfs[0][1]>elfs[1][1])):
            overlaps += 1
    return overlaps

def main(filename):
    ranges = parseInformation(filename)
    overlaps = checkPartialOverlap(ranges)
    return overlaps 

if __name__=='__main__': 
    args = sys.argv[1:]
    if args[0]=='test':
        test = True
    elif args[0]=='main':
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(4,[4],main)
    else:
        overlaps = getAnswer(4, main)
        print("The number of overlaps in work assignments is {0}".format(overlaps))