def read_file(filename):
    return open(filename, "r")

def parseInformation(line):
    tmp = line.strip().split(':')
    numberSets = tmp[1].strip().split('|')
    winnerSet = set(numberSets[0].strip().split())
    candidates = numberSets[1].strip().split()
    print(winnerSet, candidates)
    matches = 0
    for candidate in candidates:
        if candidate in winnerSet:
            matches += 1
    if matches>0:
        return 2**(matches-1)
    else: 
        return 0

if __name__=='__main__': 
    lines = read_file("day4-1-input.txt")
    #linesTest= ['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53','Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19','Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1','Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83','Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36','Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11']
    net = 0
    for line in lines:
        net += parseInformation(line)
    print(net)