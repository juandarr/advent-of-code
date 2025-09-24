from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    values = file.read()
    rows = values.rstrip().split('\n')
    return rows


def totalSurfaceArea(rows):
    total = 0
    for row in rows:
        dim = row.split('x')
        a,b,c = map(lambda d: int(d), dim)
        sides = [a*b,a*c, b*c]
        total += 2*sides[0]+2*sides[1]+2*sides[2]+min(sides)
    return total 

def main(filename):
    rows = parseInformation(filename)
    totalArea = totalSurfaceArea(rows)
    return totalArea


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2015, 2, [101], main)
    else:
        totalArea = getAnswer(2015, 2, main)
        print("The total surface area required of wrapping paper is {0}".format(totalArea))