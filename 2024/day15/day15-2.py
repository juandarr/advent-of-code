from os.path import dirname, abspath
import sys
import time

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402

def parseInformation(filename):
    file = open(filename, "r")
    s = file.read()
    rows = s.split('\n')
    data: dict[str, list] = {'map':[], 'instructions':[]}
    label = 'map'
    for row in rows:
        if row=='':
            label = 'instructions'
            continue
        if label=='map':
            data[label].append(list(row))
        else:
            data[label].extend(list(row))
    newMap = []
    for i in range(len(data['map'])):
        newRow = []
        for j in range(len(data['map'][0])):
            if data['map'][i][j]=='#':
                newRow.extend(['#', '#'])
            elif data['map'][i][j]=='O':
                newRow.extend(['[', ']'])
            elif data['map'][i][j]=='.':
                newRow.extend(['.', '.'])
            elif data['map'][i][j]=='@':
                newRow.extend(['@', '.'])
        newMap.append(newRow)
    data['map'] = newMap
    for i in range(len(data['map'])):
        for j in range(len(data['map'][0])):
            if data['map'][i][j]=='@':
                data['start']=[i,j]
                break
    return data

def printMap(map, move):
    print(f'Move: {move}')
    for row in map:
        print(''.join(row))
    print('\n')

def simulateWorld(data):
    map = data['map']
    instructions = data['instructions']
    dirs = {'>':(0,1), '<':(0,-1), 'v':(1,0), '^':(-1,0)}
    loc = data['start']
    for idx,i in enumerate(instructions):
        move = dirs[i] 
        canMove = True
        if i in ['<', '>']:
            lim = loc
            while map[lim[0]][lim[1]]!='.':
                lim = [lim[0]+move[0], lim[1]+move[1]]
                if map[lim[0]][lim[1]]=='#':     
                    canMove =False
                    break
            if canMove:
                new = lim
                while (new!=loc):
                    cur = [new[0]-move[0], new[1]-move[1]]
                    map[new[0]][new[1]] = map[cur[0]][cur[1]]
                    map[cur[0]][cur[1]] = '.'
                    new = cur
                loc = [loc[0]+move[0], loc[1]+move[1]]
        else:
            lim = loc
            span = 1
            stack = []
            while True:
                initiated = False
                newSpan = 1
                tmpCounter = 0
                toGapCounter = 0
                gapClosed = False
                for j in range(lim[1], lim[1]+span):
                    if map[lim[0]][j]=='.':     
                        if initiated:
                            tmpCounter +=1
                        if initiated and gapClosed:
                            gapClosed = False
                        continue
                    elif map[lim[0]][j]=='#':     
                        canMove =False
                        break
                    else:
                        if initiated and not(gapClosed):
                            gapClosed = True
                            toGapCounter += tmpCounter
                            tmpCounter = 0
                        if initiated:
                            newSpan += 1
                        else:
                            lim = [lim[0], j]
                            initiated = True
                if not(canMove):
                    break
                if newSpan>1:
                    newSpan += toGapCounter
                if map[lim[0]][lim[1]+newSpan-1]=='[':
                    newSpan +=1
                if map[lim[0]][lim[1]]==']':
                    newSpan +=1
                    lim = [lim[0], lim[1]-1]
                span = newSpan
                stack.append([lim,span])
                lim = [lim[0]+move[0], lim[1]+move[1]]
                if map[lim[0]][lim[1]:lim[1]+span]==['.']*span:
                    stack.append([lim,span])
                    break
            if canMove:
                for k in range(len(stack)-1,0,-1):
                    space = stack[k] 
                    elem = stack[k-1]
                    for j in range(elem[0][1], elem[0][1]+elem[1]):
                        id = map[elem[0][0]][j]
                        if id in ['[',']','@']:
                            map[space[0][0]][j] = id
                            map[elem[0][0]][j] = '.'
                            if id=='@':
                                loc =[space[0][0],j]
        simulationEnabled = False
        if simulationEnabled:
            print(f'Progress: {((idx+1)/len(instructions))*100}')
            printMap(map,i )
            time.sleep(0.05)
    gpsSum = 0
    for i in range(len(map)):
        for j in range(len(map[0])-1):
            if map[i][j:j+2]==['[',']']:
                gpsSum += (100*i+j)
    return gpsSum

def main(filename):
    data = parseInformation(filename)
    coordinateSum= simulateWorld(data)
    return coordinateSum

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')
    if test:
        performTests(2024, 15, [9021, 105+207+306],main, test=['2','3'])#10092
    else:
        total = getAnswer(2024, 15, main)
        print("The sum of GPS coordinates is: {0}".format(total))