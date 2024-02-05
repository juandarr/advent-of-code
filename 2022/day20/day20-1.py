from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    tmp = file.readlines()
    ar = []
    idxAr = []
    for idx, line in enumerate(tmp):
        value = int(line.strip())
        ar.append(value)
        idxAr.append(idx)
    return [ar, idxAr]


def mixData(data, loc):
    n = len(data)
    total = 0
    for idx, i in enumerate(data):
        realIdx = loc.index(idx)
        if i < 0:
            tmpIdx = realIdx + i
            if tmpIdx < 0:
                tmpIdx += (n - 1) * ((abs(tmpIdx) // (n - 1)) + 1)
        else:
            tmpIdx = realIdx + i
            if tmpIdx >= n:
                tmpIdx -= (n - 1) * ((tmpIdx // (n - 1)))
        # Add to the left
        if realIdx > tmpIdx:
            loc = (
                loc[:tmpIdx] + [loc[realIdx]] + loc[tmpIdx:realIdx] + loc[realIdx + 1 :]
            )
        # Add to the right
        else:
            loc = (
                loc[:realIdx]
                + loc[realIdx + 1 : tmpIdx + 1]
                + [loc[realIdx]]
                + loc[tmpIdx + 1 :]
            )
        mix = []
        for idx in loc:
            mix.append(data[idx])
    idxZero = loc.index(data.index(0))
    for i in range(1, 3 + 1):
        idx = (idxZero + 1000 * i) % n
        total += data[loc[idx]]
    return total


def main(filename):
    data, loc = parseInformation(filename)
    sum = mixData(data, loc)
    return sum


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2022, 20, [3], main)
    else:
        ans = getAnswer(2022, 20, main)
        print("The total sum of values at the 1000's is {0}".format(ans))
