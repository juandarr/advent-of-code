from os.path import dirname, abspath
import sys
import re

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    str = file.read()
    d = ''
    appending = True
    idx = 0
    while (idx< len(str)):
        if str[idx]=='d':
            if str[idx:idx+4]=='do()':
                if not(appending):
                    appending = True
                idx +=3
                continue
            elif str[idx:idx+7]=="don't()":
                if appending:
                    appending = False
                idx += 7
                continue
        if appending:
            d += str[idx]
        idx += 1
    return d

def findOcurrences(s):
    pattern = r"mul\(\d+,\d+\)"
    ocurrences = re.findall(pattern, s, flags=0)
    return ocurrences

def multiplication(s):
    ocurrences = findOcurrences(s)
    total = 0
    for o in ocurrences:
        tmp = o[:-1].split('(')[1].split(',')
        total += int(tmp[0])*int(tmp[1])
    return total

def main(filename):
    str = parseInformation(filename)
    total = multiplication(str)
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
        performTests(2024, 3, [161,48], main)
    else:
        total = getAnswer(2024, 3, main)
        print("The multiplication of valid patterns is: {0}".format(total))