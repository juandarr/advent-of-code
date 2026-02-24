from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    str = file.read()
    rows = str.split('\n')
    return [list(row) for row in  rows]

def traverseMap(pos, rows, dirs, inc):
    score = 0 
    for d in dirs:
        i = pos[0]+d[0]
        j = pos[1]+d[1]
        if (i<0 or i>=len(rows) or j<0 or j>=len(rows[0])): 
            continue
        if rows[i][j]==rows[pos[0]][pos[1]]+1:
            if rows[i][j]==9:
                score += 1
            else:
                score += traverseMap((i,j), rows, dirs)

def checkScoreSum(rows):
    startSet = []
    for i,row in enumerate(rows):
        for j,d in enumerate(row):
            rows[i][j] = int(rows[i][j])
            if d=='0':
                startSet.append((i,j))
    totalScore = 0
    for start in startSet:
        totalScore += traverseMap(start, rows, dirs)
    return totalScore

def main(filename):
    rows = parseInformation(filename)
    totalScore= checkScoreSum(rows)
    return totalScore

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2024, 10, [36],main)
    else:
        total = getAnswer(2024, 10, main)
        print("The total score for the map is: {0}".format(total))