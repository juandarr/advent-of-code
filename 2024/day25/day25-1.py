from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402

def addItem(keys, locks, grid, t):
    tmp = [-1,-1,-1,-1,-1]
    for idx,gridRow in enumerate(grid):
        if t=='lock':
            tmpRow = gridRow
        else:
            tmpRow =reversed(gridRow)
        for el in tmpRow:
            if el=='#':
                tmp[idx]+=1
            else:
                break
    if t=='lock':
        locks.add(tuple(tmp))
    else:
        keys.add(tuple(tmp))

def parseInformation(filename):
    file = open(filename, "r")
    s = file.read()
    rows = s.split('\n')
    keys = set() 
    locks = set() 
    grid = [[],[],[],[],[]]
    wall = '#'*5
    t = None
    for row in rows:
        if t==None:
            if row==wall:
                t='lock'
            else:
                t='key'
        if row=='':
            addItem(keys,locks,grid,t)
            grid = [[],[],[],[],[]]
            t = None
            continue
        for idx,el in enumerate(row):
            grid[idx].append(el)
    addItem(keys,locks,grid,t)
    return keys,locks

def checkKeys(keys,locks):
    total = 0
    for key in keys:
        for lock in locks:
            overlap = False
            for idx in range(5):
                if lock[idx]+key[idx]+2>7:
                    overlap = True
                    break
            if not overlap:
                total +=1
    return total


def main(filename):
    keys,locks = parseInformation(filename)
    out= checkKeys(keys,locks)
    return out 

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')
    if test:
        performTests(2024, 25, [3],main) 
    else:
        fits = getAnswer(2024, 25, main)
        print("The number of fits between keys and locks is {0}".format(fits))