from os.path import dirname, abspath
import sys
import re

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    data = file.read()
    rows = [row.split(' ') for row in data.rstrip().split('\n')]
    return rows[0] 


def iterateCalls(row):
    start, it = row
    cur = start
    for i in range(int(it)):
        tmp = ''
        prev = ''
        counter = 0
        for c in cur:
            if prev==c:
                counter += 1
            else:
                if prev!='':
                    tmp += str(counter)+prev
                counter = 1
            prev = c
        tmp += str(counter)+prev
        ratio = len(tmp)/len(cur)
        cur = tmp

    return len(cur) 

def main(filename):
    rows = parseInformation(filename)
    sequence = iterateCalls(rows)
    return sequence 

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2015, 10, [6], main, test=["1"])
    else:
        iterations = getAnswer(2015, 10, main)
        print("The length of the final sequence after the defined iterations is {0}".format(iterations))