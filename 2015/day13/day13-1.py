from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    data = file.read()
    people = set()
    rows = [row.split(' ') for row in data.rstrip().split('\n')]
    relations = {}
    for row in rows:
        people.add(row[0])
        if row[0] in relations:
            relations[row[0]][row[-1][:-1]] = (1 if row[2]=='gain' else -1)*int(row[3])
        else:
            relations[row[0]] = {row[-1][:-1]: (1 if row[2]=='gain' else -1)*int(row[3])}
    print(people, relations)
    return  people, relations

def seatPeople(s):
    return 0

def main(filename):
    s = parseInformation(filename)
    happyness = seatPeople(s)
    return happyness

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2015, 13, [330], main)
    else:
        optHappyness = getAnswer(2015, 13, main)
        print("The optimal happyness for the people seated on the round table is {0}".format(optHappyness))