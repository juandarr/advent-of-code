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

def checkRucksacks(rucksacks):
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

if __name__=='__main__': 
    test = False
    if test:
        filename = "day3-test-input.txt"
    else:
        filename = "day3-input.txt"
    # Create the priorities hash map: first a-z, then A-Z
    priorities = getPriorities()
    rucksacks = parseInformation(filename)
    priorities = checkRucksacks(rucksacks)
    print("Addition of priorities is {0}".format(priorities))


