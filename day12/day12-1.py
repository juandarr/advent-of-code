def read_file(filename):
    file = open(filename,'r')
    return file.readlines()

def parseInformation(lines):
    m =[]
    # Read lines and expand by rows
    for line in lines:
        tmp = line.strip().split()
        m.append([list(tmp[0]),tmp[1].split(',') ])
    return m
def findSequence(path, sequence, l):
    if sequence == []:
        return 1
    print('start: ', path, sequence)
    seqVal = int(sequence[0])
    c = 0
    endOfPath = False
    while c<len(path):
        if path[c]=='#':
            while path[c]=='#':
                l += 1
                c += 1
                if c==len(path):
                    endOfPath = True
                    break
            if not(endOfPath):
                acum += findSequence(path[c:], sequence[1:],  0 )
        elif path[c]=='.':
            while (path[c]=='.'):
                c += 1
                if c==len(path):
                    endOfPath = True
                    break
        elif path[c]=='?':
            if l==seqVal:
                path[c]='.'
                acum += findSequence(path[c+1:], sequence[1:], 0)
            elif l==0:
                for s in ['.','#']:
                    path[c] = s
                    if s=='.':
                        acum += findSequence(path[c+1:], sequence, 0)
                    elif s=='#':
                        l += 1
                        acum += findSequence(path[c:],sequence, l)
            elif l<seqVal:
                path[c]='#'
        c += 1
    if l==seqVal and endOfPath:
        return 1 
    else:
        return 0

if __name__=='__main__': 
    test =True
    if test:
        filename = "day12-test-input.txt"
    else:
        filename = "day12-1-input.txt"
    lines = read_file(filename)
    m= parseInformation(lines)
    d =0
    for row in m:
        path = row[0]
        sequence = row[1]
        print(path, sequence)
        acum = 0
        s=findSequence(path, sequence, 0)
        print(s)
        d+=1
        if d>3:
            break
    print(ways)



