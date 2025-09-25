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
    location = [[0,0], [0,0]]
    visited = [{(0,0):1},{(0,0):1}]
    houses = {(0,0):1}
    idx = 0 
    for dir in dirs:
        if dir=='>':
            location[idx][0] += 1
        elif dir=='<':
            location[idx][0]-= 1
        elif dir=='^':
            location[idx][1] += 1
        elif dir=='v':
            location[idx][1] -= 1
        if (location[idx][0],location[idx][1]) not in visited[idx]:
            visited[idx][(location[idx][0],location[idx][1])] = 1
        if (location[idx][0],location[idx][1]) not in houses:
            houses[(location[idx][0],location[idx][1])]=1
        idx = abs(idx-1)
    return len(houses)

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
        performTests(2015, 3, [3,3,11], main)
    else:
        presents = getAnswer(2015, 3, main)
        print("The total presents given during visits is {0}".format(presents))