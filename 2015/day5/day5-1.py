from os.path import dirname, abspath
import sys
import hashlib

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    data = file.read()
    strs = data.rstrip().split('\n')
    return strs


def getNiceStrs(strs):
    vowels = {'a':1, 'e':1, 'i':1, 'o':1, 'u':1}
    niceNumber = 0
    for str in strs:
        vowelList = [i for i in str if i in vowels]
        if len(vowelList)>=3:
            pass
        else:
            continue
        prev = str[0]
        hasRepetition = False
        for s in str[1:]:
            if s==prev:
                hasRepetition = True
            prev = s
        if hasRepetition:
            pass
        else:
            continue
        filters = ['ab', 'cd', 'pq', 'xy']
        hasFilter = False
        for f in filters:
            if f in str:
                hasFilter = True
        if hasFilter:
            continue
        else:
            niceNumber +=1
    return niceNumber

def main(filename):
    strs = parseInformation(filename)
    niceNumber = getNiceStrs(strs)
    return niceNumber

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2015, 5, [2], main, test=["1"])
    else:
        code = getAnswer(2015, 5, main)
        print("The number of nice strings is {0}".format(code))

