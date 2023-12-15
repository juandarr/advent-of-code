def read_file(filename):
    file = open(filename,'r')
    return file.readlines()

def parseInformation(lines):
    patterns =[]
    tmp = []
    # Read lines and expand by rows
    for line in lines:
        if line.strip()=='':
            patterns.append(tmp)
            tmp = []
        else:
            tmp.append(line.strip())
    patterns.append(tmp)
    return patterns

def findMirror(pattern):
    i = 0
    mirrorFound = False
    mirrors = {}
    while i<len(pattern)-1:
        e = len(pattern)-1
        while (e>i):
            if pattern[i]==pattern[e] and (i==0 or e==len(pattern)-1):
                iTmp = i
                eTmp = e
                lines = []
                while (pattern[iTmp]==pattern[eTmp]):
                    if (eTmp-iTmp)==1:
                        lines.append(iTmp)
                        mirrorFound =True
                        break
                    else:
                        lines.append(iTmp)
                    iTmp += 1
                    eTmp -= 1
            if mirrorFound:
                break
            e -= 1 
        if mirrorFound:
            break
        i += 1
    if mirrorFound:
        mirrors['h'] = lines[-1]+1
    j = 0
    mirrorFound = False
    while j<len(pattern[0])-1:
        e = len(pattern[0])-1
        while (e>j):
            colJ = ''.join([pattern[i][j] for i in range(len(pattern))])
            colE = ''.join([pattern[i][e] for i in range(len(pattern))])
            if colJ==colE and (j==0 or e==len(pattern[0])-1):
                jTmp = j
                eTmp = e
                cols = []
                while (colJ==colE):
                    if (eTmp-jTmp)==1 :
                        cols.append(jTmp)
                        mirrorFound =True
                        break
                    else:
                        cols.append(jTmp)
                    jTmp += 1
                    eTmp -= 1
                    if (jTmp-eTmp==0):
                        break
                    colJ = ''.join([pattern[i][jTmp] for i in range(len(pattern))])
                    colE = ''.join([pattern[i][eTmp] for i in range(len(pattern))])
            if mirrorFound:
                break
            e -= 1 
        if mirrorFound:
            break
        j += 1
    if mirrorFound:
        mirrors['v']=cols[-1]+1
    return mirrors

if __name__=='__main__': 
    test =False
    if test:
        filename = "day13-test-input.txt"
    else:
        filename = "day13-1-input.txt"
    lines = read_file(filename)
    patterns= parseInformation(lines)
    net = 0
    for pattern in patterns:
        mirrors = findMirror(pattern)
        # print(pattern,mirrors)
        max = ['x',-float('inf')]
        for m in mirrors:
            if mirrors[m]> max[1]:
                max = [m, mirrors[m]]
        if max[0]=='v':
            net += max[1]
        else:
            net += 100*max[1]
    print(net)