from os.path import dirname, abspath, join
import sys
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from utils import performTests, getAnswer

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

def checkGroups(rucksacks, priorities):
    netPriorities = 0
    items = []
    for rucksack in rucksacks:
        items.append(set(rucksack))
        if len(items) == 3:
            for a in items[0]:
                if a in items[1] and a in items[2]:
                    netPriorities += priorities[a]
                    break
            items = []
    return netPriorities

def main(filename):
    # Create the priorities hash map: first a-z, then A-Z
    priorities = getPriorities()
    rucksacks = parseInformation(filename)
    netPriorities = checkGroups(rucksacks, priorities)
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
        performTests(3,[70],main)
    else:
        netPriorities = getAnswer(3,main)        
        print("Addition of priorities is {0}".format(netPriorities))