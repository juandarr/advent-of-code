'''
'''
def read_file(filename):
    file = open(filename,'r')
    return file.readlines()

def parseInformation(lines):
    sequence =[]
    for line in lines:
        sequence.append(line.strip().split())
    return sequence

def checkZeroes(ar):
    allZeroes = True
    for x in ar:
        if x!=0:
            allZeroes = False
            break
    return allZeroes

if __name__=='__main__': 
    test = False
    testNumber= 1
    if test:
        filename = "day9-test-input{0}.txt".format(testNumber)
    else:
        filename = "day9-1-input.txt"
    lines = read_file(filename)
    sequence = parseInformation(lines)
    net = 0
    for ar in sequence:
        cur = []
        for x in ar:
            cur.append(int(x))
        allZeroes = checkZeroes(cur)
        levels = [cur]
        while(not(allZeroes)):
            tmp = []
            c = 0
            while (c< len(cur)-1):
                tmp.append(cur[c+1]-cur[c])
                c+= 1
            cur = tmp
            levels.append(cur)
            allZeroes = checkZeroes(cur)
        c = len(levels)-2
        levels[-1].insert(0,0)
        while c>=0:
            levels[c].insert(0,-levels[c+1][0]+levels[c][0])
            c -=1
        net += levels[0][0]
    print(net)
