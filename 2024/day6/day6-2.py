from os.path import dirname, abspath
import sys
import copy 

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    str = file.read()
    rows = str.split('\n')
    for idx,row in enumerate(rows):
        rows[idx] = list(row)
    return rows

def locateSoldier(rows):
    i= 0
    dirs = {'<':(0,-1),'>':(0,1),'^':(-1,0),'v':(1,0)}
    while (i<len(rows)):
        j = 0
        while(j<len(rows[0])):
            if rows[i][j] in dirs:
                return (i,j), dirs[rows[i][j]]
            j+=1
        i+=1
    return (None, None), None

def traverse(rows):
    start,direc = locateSoldier(rows)
    i, j = start
    d = direc
    uniqueVisited = 1
    visited = {(i,j):1}
    while True:
        i += d[0]
        j += d[1]
        if i<0 or i>=len(rows) or j<0 or j>=len(rows[0]):
            break
        elif rows[i][j]=='#':
            i -= d[0]
            j -= d[1]
            d = (d[1],-1*d[0])
            continue
        if (i,j) not in visited:
            visited[(i,j)]=1
            uniqueVisited +=1
    loops = 0
    for v in visited:
        rows_cp = copy.deepcopy(rows)
        rows_cp[v[0]][v[1]] = '#'
        i, j = start
        d = direc
        trace = {((i,j),d):1}
        while True:
            i += d[0]
            j += d[1]
            if i<0 or i>=len(rows) or j<0 or j>=len(rows[0]):
                break
            elif rows_cp[i][j]=='#':
                i -= d[0]
                j -= d[1]
                d = (d[1],-1*d[0])
                trace[((i,j),d)]=1
                continue
            if ((i,j),d) not in trace:
                trace[((i,j),d)]=1
            else:
                loops +=1
                break
    return loops
    


def main(filename):
    rows = parseInformation(filename)
    visited = traverse(rows)
    return visited


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2024, 6, [6], main)
    else:
        total = getAnswer(2024, 6, main)
        print("The number of positions creating a loop is: {0}".format(total))