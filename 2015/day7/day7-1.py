from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402

def parseInformation(filename):
    file = open(filename, "r")
    data = file.read()
    wirings = [s.split(' ') for s in data.rstrip().split('\n')]
    return wirings

def computeWirings(wirings):
    print(wirings)
    d = {}
    idx = len(wirings)-1
    while (idx >= 0):
        w = wirings[idx]
        if len(w)==3:
            d[w[2]] = int(w[0])
            wirings.remove(idx)
        idx -=1
    print(d)
    print(wirings)
    return 0


def main(filename):
    wirings = parseInformation(filename)
    signal = computeWirings(wirings)
    return signal

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2015, 7, [0], main)
    else:
        signal = getAnswer(2015, 7, main)
        print("The signal for wire a is {0}".format(signal))

