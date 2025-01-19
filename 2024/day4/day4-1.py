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
    pattern = 'XMAS'
    directions = [[1,0], [1,1], [0,1], [-1,1], [-1,0], [-1,-1], [0,-1],[1,-1]]
    i = 0 
    j = 0
    total = 0
    while (i<len(m)):
        while (j<len(m[0])):
            if (m[i][j]=='X'):
                for d in directions:
                    if i+3*d[0]>=len(m) or i+3*d[0]<0 or j+3*d[1]>=len(m[0]) or j+3*d[1]<0:
                        continue
                    if m[i+d[0]][j+d[1]]=='M' and m[i+2*d[0]][j+2*d[1]]=='A' and m[i+3*d[0]][j+3*d[1]]=='S':
                        total += 1
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
        performTests(2024, 4, [18], main)
    else:
        total = getAnswer(2024, 4, main)
        print("The number of patterns found in the matrix is: {0}".format(total))