from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    dataLines = open(filename, "r")
    dataLines = dataLines.readlines()
    return dataLines


def s2d(value):
    digits = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
    e = len(value) - 1
    v = 0
    for idx in range(len(value) - 1, -1, -1):
        v += digits[value[idx]] * (5 ** (e - idx))
    return v


def d2s(value, maxDigits):
    val = 0
    digits2s = {"0": "=", "1": "-", "2": "0", "3": "1", "4": "2"}

    for e in range(maxDigits):
        val += 4 * (5**e)
    e = maxDigits
    while val // 2 < value:
        val += 4 * (5**e)
        e += 1
    value = value + val // 2
    s = ""
    for idx in range(e - 1, -1, -1):
        tmp = value // (5**idx)
        s = s + str(tmp)
        value = value % (5**idx)
    s = "".join([digits2s[i] for i in list(s)])
    return s


def findSnafuValue(data):
    total = 0
    maxDigits = 0
    for d in data:
        d = d.strip()
        if len(d) > maxDigits:
            maxDigits = len(d)
        total += s2d(d)
    return d2s(total, maxDigits)


def main(filename):
    data = parseInformation(filename)
    value = findSnafuValue(data)
    return value


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2022, 25, ["2=-1=0"], main)
    else:
        ans = getAnswer(2022, 25, main)
        print("The snafu number to be supplied to the machine is {0}".format(ans))
