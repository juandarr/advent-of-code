digits = {'0': True,'1': True,'2':True,'3':True,'4':True,'5': True,'6': True,'7': True,'8': True,'9':True}

def read_file(filename):
    return open(filename, "r")

def checkItem(matrix, i,j):
    dirs = [(-1,-1),(-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    for dir in dirs:
        iTmp = i + dir[1]
        if (iTmp<0 or iTmp>=len(matrix)):
            continue
        jTmp = j + dir[0]
        if (jTmp<0 or jTmp>= len(matrix[iTmp])):
            continue
        if (matrix[iTmp][jTmp] not in digits and matrix[iTmp][jTmp] != '.'):
            if matrix[iTmp][jTmp] =='*':
                return (iTmp, jTmp)
    return False


if __name__=='__main__': 
    lines = read_file("day3-1-input.txt")
    # linesTest = ['467..114..','...*......','..35..633.','......#...','617*......', '.....+.58.','..592.....','......755.','...$.*....','.664.598..']
    #linesTest2 = ['.......................*......*','...910*...............233..189.','2......391.....789*............','...................983.........','0........106-...............226','.%............................$','...*......$812......812..851...','.99.711.............+.....*....','...........................113.','28*.....411....%...............']
    m = []
    for line in lines:
        m.append(list(line.strip()))
    i = 0
    j = 0
    net = 0
    potentialGear = {}
    while (i < len(m)):
        tmp = ''
        j = 0
        gears = set()
        while (j < len(m[i])):
            if m[i][j] in digits:
                tmp += m[i][j]
                isGear = checkItem(m, i, j)
                if isGear != False:
                    gears.add(isGear)
                if (j == len(m[i]) -1):
                    if (tmp != '' and len(gears)>0):
                        for gear in gears:
                            if gear in potentialGear:
                                potentialGear[gear].append(int(tmp))
                            else:
                                potentialGear[gear] = [int(tmp)]
            else:
                if (tmp != '' and len(gears)>0):
                    for gear in gears:
                        if gear in potentialGear:
                            potentialGear[gear].append(int(tmp))
                        else:
                            potentialGear[gear] = [int(tmp)]
                tmp = ''
                gears = set()
            j += 1
        i += 1
    for gear in potentialGear:
        if len(potentialGear[gear])==2:
            net += potentialGear[gear][0]*potentialGear[gear][1]
            print(potentialGear[gear])
    print(net)
