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
    print(lev)
    movingDown = True
    while (movingDown) :
        movingDown = False
        curLevel = 2
        print('Starting loop: ',curLevel, maxLev)
        while curLevel<=maxLev:
            belowLevel = curLevel -1
            goingDown = []
            if curLevel in lev:
                for b in lev[curLevel]:
                    brick = bricks[b]
                    if belowLevel>0:
                        goesBelow = True
                        blocked = [False, False]
                        if belowLevel in lev:
                            for bBelow in lev[belowLevel]:
                                brickBelow = bricks[bBelow]
                                for idx in range(2):
                                    m = list(range(max(brick[0][idx],brickBelow[0][idx]), min(brick[1][idx], brickBelow[1][idx])+1))
                                    if m!=[]:
                                        blocked[idx]= True
                                    if blocked[0]==True and blocked[1]==True:
                                        goesBelow =False
                                        break
                                if not(goesBelow):
                                    break
                    else:
                        break
                    if goesBelow:
                        movingDown  = True
                        l = curLevel
                        while (l<=maxLev):
                            if l in lev:
                                if b in lev[l]:
                                    goingDown.append((b,l))
                            else:
                                break
                            l +=1
            if len(goingDown)>0:
                for val in goingDown:
                    b = val[0]
                    level = val[1]
                    lowLevel = level-1
                    del lev[level][b]
                    if lev[level]=={}:
                        del lev[level]
                    if lowLevel in lev:
                        lev[lowLevel][b] =True
                    else:
                        lev[lowLevel] = {b:True}
            curLevel +=1
    print(lev)
    c = 1
    counter =0
    while (c+1 in lev):
        for b in lev[c]:
            toTest = lev[c].copy()
            del toTest[b]
            for bAbove in lev[c+1]:
                brick = bricks[bAbove]
                goesBelow = True
                blocked = [False, False]
                for bBelow in toTest:
                    brickBelow = bricks[bBelow]
                    for idx in range(2):
                        m = list(range(max(brick[0][idx],brickBelow[0][idx]), min(brick[1][idx], brickBelow[1][idx])+1))
                        if m!=[]:
                            blocked[idx] = True 
                        if blocked[0]==True and blocked[1]==True:
                            goesBelow = False
                            break
                if (goesBelow):
                    break
            if goesBelow:
                print('CanNOT remove: ',b)
            else:
                print('Can remove: ',b)
                counter +=1
        c +=1
    counter+=len(lev[c])
    return  counter


if __name__=='__main__': 
    test = False
    testNumber = 3
    if test:
        filename = "day22-test{0}-input.txt".format(testNumber)
    else:
        filename = "day22-1-input.txt"
    lines = read_file(filename)
    bricks = parseInformation(lines)
    print(bricks, len(bricks))
    p = exploreFall(bricks)
    print(p)
# Too high: 1473
# Too high: 878