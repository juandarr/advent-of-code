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

def checkGroups(rucksacks):
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

if __name__=='__main__': 
    test = False
    if test:
        filename = "day3-test-input.txt"
    else:
        filename = "day3-input.txt"
    # Create the priorities hash map: first a-z, then A-Z
    priorities = getPriorities()
    rucksacks = parseInformation(filename)
    priorities = checkGroups(rucksacks)
    print("Addition of priorities is {0}".format(priorities))


