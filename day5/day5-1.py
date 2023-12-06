def read_file(filename):
    return open(filename, "r")

def parseInformation(lines):
    c = 0
    seeds = ''
    mapping = {}
    currentMapping = ''
    for line in lines:
        if c==0:
            seeds = line.strip().split(':')[1].strip().split()
            c += 1
        else:
            tmp = line.strip()
            if tmp == '': continue
            if tmp!= '' and tmp[-1]==':':
                tmp = tmp.split(' ')
                currentMapping = tmp[0]
                mapping[currentMapping] = []
            else:
                tmp = tmp.split(' ') 
                mapping[currentMapping].append(tmp)
    return seeds, mapping

if __name__=='__main__': 
    test =False 
    if test:
        filename = "day5-test-input.txt"
    else:
        filename = "day5-1-input.txt"
    mappingLabels = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
    lines = read_file(filename)
    seeds, mapping= parseInformation(lines)
    minLocation = float('inf')
    for seed in seeds:
        currentNode = int(seed)
        for label in mappingLabels:
            for s in mapping[label]:
                if currentNode >= int(s[1]) and currentNode < int(s[1]) + int(s[2]):
                    dif = currentNode - int(s[1])
                    currentNode = int(s[0]) + dif
                    break
        if minLocation > currentNode:
            minLocation = currentNode
    print(minLocation)