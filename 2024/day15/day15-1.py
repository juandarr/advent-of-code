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
    simulatedWorld = False
    for i in instructions:
        lim = loc
        move = dirs[i] 
        canMove = True
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
        if simulatedWorld: 
            printMap(map, i)
            time.sleep(0.05)
    gpsSum = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j]=='O':
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
        performTests(2024, 15, [2028,10092 ],main)
    else:
        total = getAnswer(2024, 15, main)
        print("The sum of GPS coordinates is: {0}".format(total))