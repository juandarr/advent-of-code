from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    values = file.read()
    rows = values.rstrip().split("\n")
    idx = 0
    for row in rows:
        rows[idx] = row.split(" ")
        idx+=1
    return rows

def checkValidity(a,b):
    tmp = abs(a-b)
    if tmp<1 or tmp>3:
        return "",False
    if (a-b>0):
        d = "-"
    elif (a-b<0):
        d = "+"
    else:
        return "",False
    return d,True

def reportChecker(report):
    a = int(report[0])
    b = int(report[1])
    prevD, valid = checkValidity(a,b)
    if not(valid):
        return False    
    a = b
    for val in report[2:]:
        b = int(val)
        d, valid = checkValidity(a,b)
        if not(valid):
            return False
        if (prevD!=d):
            return False
        a = b
        prevD = d
        
    return True


def main(filename):
    reports = parseInformation(filename)
    validReports = 0
    for report in reports:
        if (reportChecker(report)):
            validReports += 1
    return validReports


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2024, 2, [2], main)
    else:
        validReports = getAnswer(2024, 2, main)
        print("The number of valid reports is: {0}".format(validReports))