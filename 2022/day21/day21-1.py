from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    dataLines = open(filename, "r")
    dataLines = dataLines.readlines()
    values = {}
    formulas = {}
    for line in dataLines:
        line = line.strip().split(": ")
        if " " in line[1]:
            tmp = line[1].split(" ")
            formulas[line[0]] = {"operands": [tmp[0], tmp[2]], "operator": tmp[1]}
        else:
            values[line[0]] = int(line[1])
    return [values, formulas]


def monkeyMath(values, formulas):
    root = "root"
    while root not in values:
        toCalculate = []
        for formula in formulas:
            readyToCalculate = True
            for operand in formulas[formula]["operands"]:
                if operand not in values:
                    readyToCalculate = False
                    break
            if readyToCalculate:
                toCalculate.append(formula)
        for f in toCalculate:
            operands = formulas[f]["operands"]
            operator = formulas[f]["operator"]
            values[f] = eval(
                str(values[operands[0]]) + operator + str(values[operands[-1]])
            )
            del formulas[f]
    return int(values[root])


def main(filename):
    values, formulas = parseInformation(filename)
    result = monkeyMath(values, formulas)
    return result


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2022, 21, [152], main)
    else:
        ans = getAnswer(2022, 21, main)
        print("The number yelled by root monkey is {0}".format(ans))
