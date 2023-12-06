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
    test =  False
    if test:
        filename = "day5-test-input.txt"
    else:
        filename = "day5-1-input.txt"
    mappingLabels = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
    lines = read_file(filename)
    seedsRanges, mapping= parseInformation(lines)
    minLocation = float('inf')
    inputRanges = seedsRanges
    outputRanges = []
    ln = 0
    for label in mappingLabels:
        if outputRanges != []:
            inputRanges = outputRanges.copy()
        outputRanges = []
        # print(label)
        for s in mapping[label]:
            c = 0
            tmp = []
            # print('new mapping: ',s,inputRanges)
            while c<len(inputRanges):
                ranges = inputRanges[c]
                #Lists cases of range overlapping
                #outside to the left -works
                if int(s[1])+int(s[2])-1<int(ranges[0]):
                    # print('outside to the left', s, ranges)
                    tmp.append(inputRanges[c])
                #outside to the right - works
                if int(s[1])>int(ranges[0]) + int(ranges[1]) -1:
                    # print('outside to the right', s, ranges)
                    tmp.append(inputRanges[c])
                #intersection to the left - works?
                if int(s[1])<int(ranges[0]) and int(s[1])+int(s[2])-1 < int(ranges[0])+ int(ranges[1])-1 and int(s[1])+int(s[2])-1 >= int(ranges[0]):
                    dif = int(ranges[0])- int(s[1])
                    tmp.append([int(s[1])+int(s[2]), int(ranges[0]) +int(ranges[1]) -int(s[1])-int(s[2])])
                    outputRanges.append([int(s[0])+dif, int(s[1])+int(s[2])-int(ranges[0])])
                    # print('Intersection to the left: ',s, ranges)
                    # print('Here are changes: ', tmp[-1], outputRanges[-1])
                #intersection to the right - works?
                if int(s[1])+int(s[2])-1 > int(ranges[0])+int(ranges[1])-1 and int(s[1]) <= int(ranges[0])+ int(ranges[1])-1 and int(s[1]) > int(ranges[0]):
                    dif = int(ranges[0])+int(ranges[1])-int(s[1])
                    tmp.append([int(ranges[0]), int(ranges[1]) - dif])
                    outputRanges.append([int(s[0]), dif])
                    # print('Intersection to the right: ',s, ranges)
                    # print('Here are changes: ', tmp[-1], outputRanges[-1])
                #inside the range - works?
                if int(s[1]) >= int(ranges[0]) and int(s[1])+int(s[2])-1<= int(ranges[0])+int(ranges[1])-1:
                    if int(s[1])- int(ranges[0])>0:
                        tmp.append([int(ranges[0]), int(s[1])- int(ranges[0])])
                    if   (int(ranges[0]) +int(ranges[1])) - (int(s[1])+int(s[2]))>0:
                        tmp.append([int(s[1])+ int(s[2]),    (int(ranges[0]) +int(ranges[1])) - (int(s[1])+ int(s[2]))] ) 
                    outputRanges.append([int(s[0]), int(s[2])])
                    # print('Covering inside range', s, ranges)
                    # if len(tmp)>1:
                    #     print('Here are changes: ', tmp[-2], tmp[-1], outputRanges[-1])
                    # elif len(tmp)>0:
                    #     print('Here are changes: ', tmp[-1], outputRanges[-1])
                #covering whole range - works
                if int(s[1]) <= int(ranges[0]) and int(s[1])+int(s[2])-1>= int(ranges[0])+int(ranges[1])-1:
                    outputRanges.append([int(s[0])+int(ranges[0])-int(s[1]), int(ranges[1])])
                    # print('Covering whole range', s, ranges)
                    # print('Here are changes: ', outputRanges[-1])
                c += 1
            inputRanges = tmp.copy()
        ln += 1
        for ranges in tmp:
            outputRanges.append(ranges)
        # print('outputRanges: ', outputRanges)
        if ln==7:
            break
    minVal = float('inf')
    for ranges in outputRanges:
        if ranges[0] < minVal:
            minVal = ranges[0]
    print(minVal)