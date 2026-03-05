from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402

def parseInformation(filename):
    file = open(filename, "r")
    str = file.read()
    rows = str.split('\n')
    machines = [[]]
    for row in rows:
        if row=='':
            machines.append([])
            continue
        tmp = row.split(': ')
        data = tmp[1]
        xy = []
        if tmp[0] in ['Button A', 'Button B']:
            data = data.split(', ')
            for d in data:
                d = d.split('+')
                xy.append(int(d[1]))
            machines[-1].append(xy)
        else:
            data = data.split(', ')
            for d in data:
                d = d.split('=')
                xy.append(int(d[1]))
            machines[-1].append(xy)
    return machines

def calculateCost(machines):
    cost = 0
    for m in machines:
        a = (m[1][1]*m[2][0]-m[1][0]*m[2][1])/(m[1][1]*m[0][0]-m[1][0]*m[0][1])
        if a==int(a):
            b = (m[2][0]-m[0][0]*int(a))/m[1][0]
            if b==int(b):
                cost += 3*a+b
    return int(cost)

def main(filename):
    machines = parseInformation(filename)
    price = calculateCost(machines)
    return price 

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')
    if test:
        performTests(2024, 13, [480],main)
    else:
        cost = getAnswer(2024, 13, main)
        print("The total token cost of positioning machines at the target location is: {0}".format(cost))