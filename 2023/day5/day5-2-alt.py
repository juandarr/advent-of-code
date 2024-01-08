def read_file(filename):
    return open(filename, "r")

def parseInformation(lines):
    c = 0
    seedsRanges = ''
    mapping = {}
    currentMapping = ''
    for line in lines:
        if c==0:
            tmp = line.strip().split(':')[1].strip().split()
            seedsRanges = [tmp[n: n+2] for n in range(0,len(tmp), 2)]
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
    return seedsRanges, mapping

if __name__=='__main__': 
    test =True 
    if test:
        filename = "day5-test-input.txt"
    else:
        filename = "day5-1-input.txt"
    mappingLabels = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
    lines = read_file(filename)
    seedsRanges, mapping= parseInformation(lines)
    minLocation = float('inf')
    pastNode= ''
    for seedRange in seedsRanges:
        for seed in range(int(seedRange[0]), int(seedRange[0]) +int(seedRange[1])):
            currentNode = int(seed)
            # c = 0
            for label in mappingLabels:
                for s in mapping[label]:
                    pastNode =currentNode
                    if currentNode >= int(s[1]) and currentNode < int(s[1]) + int(s[2]):
                        dif = currentNode - int(s[1])
                        currentNode = int(s[0]) + dif
                        break
                # c += 1
                # if c==2:
                #     print(pastNode,currentNode, label)
            if minLocation > currentNode:
                minLocation = currentNode
    print(minLocation)