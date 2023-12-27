from time import sleep, time

def read_file(filename):
    file = open(filename,'r')
    return file.readlines()

def parseInformation(lines):
    # Read lines and expand by rows
    bricks = {}
    c = 1
    for line in lines:
        points = line.strip().split('~')
        p = []
        for point in points:
            x,y,z = point.split(',')
            p.append([int(x), int(y), int(z)])
        bricks[c] =p
        c+=1
    return  bricks

def exploreFall(bricks):
    lev = {}
    minLev = float('inf') 
    maxLev = -float('inf') 
    for label in bricks:
        brick = bricks[label]
        levels = list(range(brick[0][-1], brick[1][-1]+1))
        for level in levels:
            if level<minLev:
                minLev = level
            elif level>maxLev:
                maxLev = level
            if level in lev :
                lev[level][label] = True
            else:
                lev[level] = {label: True}
    movingDown = True
    curLevel = minLev  
    while (movingDown and curLevel<=maxLev):
        movingDown = False
        if curLevel in lev:
            for b in lev[curLevel]:
                brick = bricks[lev[curLevel][b]]
                goesBelow = True
                belowLevel = curLevel -1
                if belowLevel>0:
                    if belowLevel in lev:
                        for bBelow in lev[belowLevel]:
                            brickBelow = lev[belowLevel][bBelow]
                            for idx in range(2):
                                m = list(range(max(brick[0][idx],brickBelow[0][idx]), min(brick[1][idx], brickBelow[1][idx])))
                                if m==[]:
                                    continue 
                                else:
                                    goesBelow =False
                                    break
                            if not(goesBelow):
                                break
                    else:
                        lev[belowLevel] = {b:True}
                        del lev[curLevel][b]
                        goesBelow = False
                        movingDown = True
                else:
                    break
                if goesBelow:
                    movingDown  = True
                    del lev[curLevel][b]
                    if belowLevel in lev:
                        lev[belowLevel][b] =True
                    else:
                        lev[belowLevel] = {b:True}
        else:
            curLevel +=1
    return lev, [minLev, maxLev]


if __name__=='__main__': 
    test = True
    testNumber = 1
    if test:
        filename = "day22-test{0}-input.txt".format(testNumber)
    else:
        filename = "day22-1-input.txt"
    lines = read_file(filename)
    bricks = parseInformation(lines)
    print(bricks, len(bricks))
    levs, limits = exploreFall(bricks)
    print(levs, limits)