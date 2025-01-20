from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    str = file.read()
    rows = str.split('\n')
    for idx,row in enumerate(rows):
        rows[idx] = list(row)
    return rows

def findOcurrences(m):
    pattern = 'MAS'
    directions = [[1,1], [-1,1], [-1,-1], [1,-1]]
    i = 0 
    j = 0
    total = 0
    visited = {}
    while (i<len(m)):
        while (j<len(m[0])):
            if (m[i][j]=='M'):
                for d in directions:
                    if i+2*d[0]>=len(m) or i+2*d[0]<0 or j+2*d[1]>=len(m[0]) or j+2*d[1]<0:
                        continue
                    if m[i+d[0]][j+d[1]]=='A' and m[i+2*d[0]][j+2*d[1]]=='S':
                        it = i+d[0]
                        jt = j+d[1]
                        if (it,jt) in visited:
                            continue
                        i1 = i+2*d[0]
                        j1 = j+2*d[1]
                        if m[i1][j]=='M':
                            dt = [-1*d[0], d[1]]
                            if i1+2*dt[0]>=len(m) or i1+2*dt[0]<0 or j+2*dt[1]>=len(m[0]) or j+2*dt[1]<0:
                                continue
                            if m[i1+dt[0]][j+dt[1]]=='A' and m[i1+2*dt[0]][j+2*dt[1]]=='S':
                                total += 1
                                visited[(it,jt)]=1
                        elif m[i][j1]=='M':
                            dt = [d[0], -1*d[1]]
                            if i+2*dt[0]>=len(m) or i+2*dt[0]<0 or j1+2*dt[1]>=len(m[0]) or j1+2*dt[1]<0:
                                continue
                            if m[i+dt[0]][j1+dt[1]]=='A' and m[i+2*dt[0]][j1+2*dt[1]]=='S':
                                total += 1
                                visited[(it,jt)]=1
            j+=1
        j=0
        i+=1
    return total


def main(filename):
    m = parseInformation(filename)
    total = findOcurrences(m)
    return total


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2024, 4, [9], main)
    else:
        total = getAnswer(2024, 4, main)
        print("The number of patterns found in the matrix is: {0}".format(total))