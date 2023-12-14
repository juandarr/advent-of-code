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

def findSequence(path, sequence):
    if sequence == []:
        valid =True
        for s in ''.join(path):
            if s not in ['.','?']:
                valid = False
                break
        if valid:
            return 1
        else:
            return 0
    seqVal = int(sequence[0])
    c = 0
    l = 0
    while c<len(path):
        if path[c]=='#':
            l += 1
            if l>seqVal:
                break
        elif path[c]=='.':
            if l==seqVal:
                return findSequence(path[c+1:],sequence[1:])
            elif l>0 and l<seqVal:
                break
        elif path[c]=='?':
            if l==seqVal:
                path[c]='.'
                return findSequence(path[c+1:], sequence[1:])
            elif l==0:
                net = 0
                for s in ['.','#']:
                    path[c] = s
                    if s=='.':
                        net += findSequence(path[c+1:], sequence)
                    elif s=='#':
                        net += findSequence(path[c:],sequence)
                return net
            elif l<seqVal:
                path[c]='#'
                l += 1
        c += 1
    if l==seqVal and len(sequence)==1:
        return 1
    return 0

if __name__=='__main__': 
    test =True
    if test:
        filename = "day12-test-input.txt"
    else:
        filename = "day12-1-input.txt"
    lines = read_file(filename)
    m= parseInformation(lines)
    net = 0
    for row in m:
        path = row[0].copy()
        sequence = row[1].copy()
        for _ in range(4):
            path += ['?']+ row[0].copy()
            sequence += row[1].copy()
        net += findSequence(path, sequence)
    print(net)