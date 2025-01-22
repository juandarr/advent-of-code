from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    str = file.read()
    rows = str.split('\n')
    data = [[],[],[]]
    idx = 0
    for row in rows:
        if row=='':
            idx+=1
            continue
        if idx==0:
            data[idx].append(list(map(int,row.split('|'))))
        else:
            data[idx].append(list(map(int, row.split(','))))
            data[idx+1].append({value:index for index,value in enumerate(data[idx][-1])})
    return data

def checkUpdates(rules, updates, updatesDict):
    validTotal = 0
    for idx,update in enumerate(updatesDict):
        valid = True
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                if update[rule[0]]>update[rule[1]]:
                    valid = False
                    break
        if not(valid):
            for i in range(10):
                for rule in rules:
                    if rule[0] in update and rule[1] in update:
                        if update[rule[0]]>update[rule[1]]:
                            tmp = update[rule[0]]
                            update[rule[0]]= update[rule[1]]
                            update[rule[1]]=tmp
            tmpSorted = sorted(update.items(), key=lambda item: item[1])
            print(tmpSorted)
            validTotal += tmpSorted[len(tmpSorted)//2][0]
    return validTotal


def main(filename):
    rules, updates, updatesDict = parseInformation(filename)
    total = checkUpdates(rules,updates, updatesDict)
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
        performTests(2024, 5, [123], main)
    else:
        total = getAnswer(2024, 5, main)
        print("The sum of middle values of correctly-ordered updates is: {0}".format(total))