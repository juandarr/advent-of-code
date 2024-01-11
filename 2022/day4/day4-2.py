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

if __name__=='__main__': 
    test = False
    if test:
        filename = "day4-test-input.txt"
    else:
        filename = "day4-input.txt"
    ranges = parseInformation(filename)
    overlaps = checkPartialOverlap(ranges)
    print("The number of partial overlaps in work assignments is {0}".format(overlaps))