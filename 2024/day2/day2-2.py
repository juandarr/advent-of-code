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

def checkValidity(a,b, prevD):
    tmp = abs(a-b)
    if tmp<1 or tmp>3:
        return "ii",False
    if (a-b>0):
        d = "-"
    elif (a-b<0):
        d = "+"
    else:
        return "id",False
    if prevD!=None:
        if prevD!=d:
            return "id", False
    return d,True

def reportChecker(report):
    tolerance = 1

    a = int(report[0])
    b = int(report[1])
    fut = int(report[2])
    fut2 = int(report[3])

    prevD = None
    startIdx = 2
    prevD, valid = checkValidity(a,b, prevD)
    if not(valid):
        if abs(fut-a)<=0 or abs(fut-a)>=4:
            a = b
        prevD = None
        b = fut
        tolerance = 0
        startIdx = 3
        prevD, valid = checkValidity(a,b,prevD)
        if not(valid):
            return False
    a = b
    idx = startIdx
    while (idx<len(report)):
        b = int(report[idx])
        if idx+1==len(report):
            fut = None
        else:
            fut = int(report[idx+1])
        d, valid = checkValidity(a,b, prevD)
        if not(valid):
            if tolerance>0:
                if idx+1==len(report):
                    break
                tolerance -=1
                idx+=1
                continue
            else:
                return False
        a = b
        prevD = d 
        idx+=1
    return True


def main(filename):
    reports = parseInformation(filename)
    validReports = 0
    for report in reports:
        valid = reportChecker(report)
        valid2 = reportChecker(report[::-1])
        # Count when succession is valid in any of the two directions
        if valid != valid2 or valid:        
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
        # Test1:4 test2:10
        performTests(2024, 2, [4,10,4], main)
    else:
        validReports = getAnswer(2024, 2, main)
        print("The number of valid reports is: {0}".format(validReports))