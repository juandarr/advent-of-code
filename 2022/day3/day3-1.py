from os.path import dirname, abspath, join
import sys
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from tests import performTests

def parseInformation(filename):
    file = open(filename, "r")
    tmp= file.read()
    tmp= tmp.rstrip().split('\n')
    return tmp

def getPriorities():
    priorities = {}
    p = 1
    for i in range(97, 97+26):
        priorities[chr(i)] = p
        p += 1
    for i in range(65, 65+26):
        priorities[chr(i)] = p
        p += 1
    return priorities

def checkRucksacks(rucksacks, priorities):
    netPriorities = 0
    for rucksack in rucksacks:
        m = int(len(rucksack)/2)
        section1 = set(rucksack[0:m])
        section2 = set(rucksack[m:])
        # For eachh rucksack, find the item that is in both containers (first and second halfs)
        for a in section1:
            if a in section2:
                netPriorities += priorities[a]
                break
    return netPriorities

def main(filename):
    # Create the priorities hash map: first a-z, then A-Z
    priorities = getPriorities()
    rucksacks = parseInformation(filename)
    netPriorities = checkRucksacks(rucksacks, priorities)
    return netPriorities 

if __name__=='__main__': 
    args = sys.argv[1:]
    if args[0]=='test':
        test = True
    elif args[0]=='main':
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(3,[157],main,[])
    else:
        dir = dirname(__file__)
        filename = join(dir,'day3-input.txt')
        netPriorities = main(filename)        
        print("Addition of priorities is {0}".format(netPriorities))