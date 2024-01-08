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

def compare(str1, str2):
    difs = 0
    for (idx, value) in enumerate(str1):
        if value != str2[idx]:
            difs += 1
    if difs==1:
        return True
    return False

def findMirror(pattern):
    i = 0
    mirrorFound = False
    mirrors = {}
    while i<len(pattern)-1:
        e = len(pattern)-1
        while (e>i):
            if pattern[i]==pattern[e] and (i==0 or e==len(pattern)-1):
                iTmp = i
                lines = []
                while (pattern[iTmp]==pattern[e]):
                    if (e-iTmp)==1:
                        lines.append(iTmp)
                        mirrorFound =True
                        break
                    else:
                        lines.append(iTmp)
                    iTmp += 1
                    e -= 1
                    if (iTmp-e==0):
                        break
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
                cols = []
                while (colJ==colE):
                    if (e-jTmp)==1 :
                        cols.append(jTmp)
                        mirrorFound =True
                        break
                    else:
                        cols.append(jTmp)
                    jTmp += 1
                    e -= 1
                    if (jTmp-e==0):
                        break
                    colJ = ''.join([pattern[i][jTmp] for i in range(len(pattern))])
                    colE = ''.join([pattern[i][e] for i in range(len(pattern))])
            if mirrorFound:
                break
            e -= 1 
        if mirrorFound:
            break
        j += 1
    if mirrorFound:
        mirrors['v']=cols[-1]+1
    return mirrors

def findMirrorSmidge(pattern, mirrors):
    i = 0
    mirrorFound = False
    mirrorsSmidge = {}
    while i<len(pattern)-1:
        e = len(pattern)-1
        while (e>i):
            comp = compare(pattern[i], pattern[e])
            used = False
            if (comp or pattern[i]==pattern[e]) and (i==0 or e==len(pattern)-1):
                iTmp = i
                eTmp = e
                lines = []
                while ((comp and not(used))  or pattern[iTmp]==pattern[eTmp]):
                    if comp and pattern[iTmp]!=pattern[eTmp]:
                        used = True
                    if (eTmp-iTmp)==1:
                        lines.append(iTmp)
                        if 'h' in mirrors:
                            if mirrors['h']== lines[-1]+1:
                                break
                        mirrorFound =True
                        break
                    else:
                        lines.append(iTmp)
                    iTmp += 1
                    eTmp -= 1
                    comp = compare(pattern[iTmp], pattern[eTmp])
                    if (iTmp-eTmp==0):
                        break
            if mirrorFound:
                break
            e -= 1 
        if mirrorFound:
            break
        i += 1
    if mirrorFound:
        mirrorsSmidge['h'] = lines[-1]+1
    j = 0
    mirrorFound = False
    while j<len(pattern[0])-1:
        e = len(pattern[0])-1
        while (e>j):
            colJ = ''.join([pattern[i][j] for i in range(len(pattern))])
            colE = ''.join([pattern[i][e] for i in range(len(pattern))])
            comp = compare(colJ, colE)
            used = False
            if (comp or colJ==colE) and (j==0 or e==len(pattern[0])-1):
                jTmp = j
                eTmp = e
                cols = []
                while ((comp and not(used)) or colJ==colE):
                    if comp and colJ!=colE:
                        used = True
                    if (eTmp-jTmp)==1 :
                        cols.append(jTmp)
                        if 'v' in mirrors:
                            if mirrors['v']== cols[-1]+1:
                                break
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
                    comp = compare(colJ, colE)
            if mirrorFound:
                break
            e -= 1 
        if mirrorFound:
            break
        j += 1
    if mirrorFound:
        mirrorsSmidge['v']=cols[-1]+1
    return mirrorsSmidge

if __name__=='__main__': 
    test = False
    if test:
        filename = "day13-test-input.txt"
    else:
        filename = "day13-1-input.txt"
    lines = read_file(filename)
    patterns= parseInformation(lines)
    net = 0
    for pattern in patterns:
        mirrors = findMirror(pattern)
        mirrorsSmidge = findMirrorSmidge(pattern, mirrors)
        max = ['x',0]
        for m in mirrorsSmidge:
            if m in mirrors:
                if mirrorsSmidge[m]!=mirrors[m]:
                    if mirrorsSmidge[m]> max[1]:
                        max = [m, mirrorsSmidge[m]]
            else:
                if mirrorsSmidge[m]> max[1]:
                    max = [m, mirrorsSmidge[m]]
        if max[1]==0:
            print(d,mirrorsSmidge, mirrors)
        if max[0]=='v':
            net += max[1]
        else:
            net += 100*max[1]
    print(net)