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

mem = {}

def findSequence(path, sequence):
    key = (''.join(path), ','.join(sequence))
    if key in mem:
        return mem[key]
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
                s = findSequence(path[c+1:],sequence[1:])
                mem[key] =s
                return s 
            elif l>0 and l<seqVal:
                break
        elif path[c]=='?':
            if l==seqVal:
                path[c]='.'
                s =findSequence(path[c+1:], sequence[1:])
                mem[key] =s
                return s 
            elif l==0:
                net = 0
                for s in ['.','#']:
                    path[c] = s
                    if s=='.':
                        net += findSequence(path[c+1:], sequence)
                    elif s=='#':
                        net += findSequence(path[c:],sequence)
                mem[key] = net
                return net
            elif l<seqVal:
                path[c]='#'
                l += 1
        c += 1
    if l==seqVal and len(sequence)==1:
        return 1
    return 0

if __name__=='__main__': 
    test =False
    if test:
        filename = "day12-test-input.txt"
    else:
        filename = "day12-1-input.txt"
    lines = read_file(filename)
    m= parseInformation(lines)
    net = 0
    for row in m:
        path = row[0]
        sequence = row[1]
        net += findSequence(path, sequence)
    print(net)