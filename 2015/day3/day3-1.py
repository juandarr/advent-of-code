from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    data = file.read()
    dirs = data.rstrip()
    return dirs


def totalPresents(dirs):
    x = 0
    y = 0
    visited = {(0,0):1}
    for dir in dirs:
        if dir=='>':
            x += 1
        elif dir=='<':
            x-=1
        elif dir=='^':
            y +=1
        elif dir=='v':
            y -= 1
        if (x,y) not in visited:
            visited[(x,y)] = 1
    return len(visited)

def main(filename):
    dirs = parseInformation(filename)
    presents = totalPresents(dirs)
    return presents


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2015, 3, [2,4,2], main)
    else:
        presents = getAnswer(2015, 3, main)
        print("The total presents given during visits is {0}".format(presents))