from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    dataLines = open(filename, "r")
    dataLines = dataLines.readlines()
    values = {}
    formulas = {}
    nodeHuman = "humn"
    for line in dataLines:
        line = line.strip().split(": ")
        if line[0] == nodeHuman:
            continue
        if " " in line[1]:
            left, op, right = line[1].split(" ")
            formulas[line[0]] = {"operands": [left, right], "operator": op}
        else:
            values[line[0]] = int(line[1])
    return [values, formulas]


def monkeyMath(values, formulas):
    node = "root"
    nodeHuman = "humn"
    toCalculate = ["dummy"]

    operations = {
        "+": lambda x, y: int(x + y),
        "-": lambda x, y: int(x - y),
        "*": lambda x, y: int(x * y),
        "/": lambda x, y: int(x / y),
    }

    while toCalculate != []:
        toCalculate = []
        for formula in formulas:
            readyToCalculate = True
            for idx, operand in enumerate(formulas[formula]["operands"]):
                if isinstance(operand, int):
                    continue
                if operand in values:
                    formulas[formula]["operands"][idx] = values[operand]
                else:
                    readyToCalculate = False
            if readyToCalculate:
                toCalculate.append(formula)
        for f in toCalculate:
            left, right = formulas[f]["operands"]
            operator = formulas[f]["operator"]
            # values[f]= int(eval(str(operands[0])+operator+str(operands[1])))
            values[f] = operations[operator](left, right)
            del formulas[f]
    # Now calculate the rest of the formulas
    currentNode = node  # Use root as the first node
    tmpInt = 0
    tmpStr = ""
    for operand in formulas[currentNode]["operands"]:
        if isinstance(operand, int):
            tmpInt = operand
        else:
            tmpStr = operand
    # Root node gets the value of its operands
    values[currentNode] = tmpInt
    # Also define value of previously unknown variable
    values[tmpStr] = tmpInt
    # While 'humn' value hasn't been reached yet
    while nodeHuman not in values:
        currentValue = tmpInt
        currentNode = tmpStr
        for idx, operand in enumerate(formulas[currentNode]["operands"]):
            if isinstance(operand, int):
                tmpInt = operand
            else:
                pastStr = tmpStr
                tmpStr = operand
                i = idx
        if formulas[currentNode]["operator"] == "*":
            tmpInt = currentValue / tmpInt
        elif formulas[currentNode]["operator"] == "+":
            tmpInt = currentValue - tmpInt
        elif formulas[currentNode]["operator"] == "-":
            if i == 0:
                tmpInt = currentValue + tmpInt
            else:
                tmpInt = tmpInt - currentValue
        elif formulas[currentNode]["operator"] == "/":
            if i == 0:
                tmpInt = currentValue * tmpInt
            else:
                tmpInt = tmpInt / currentValue
        # del formulas[pastStr]
        values[tmpStr] = tmpInt
    return int(values[nodeHuman])


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
        performTests(2022, 21, [301], main)
    else:
        ans = getAnswer(2022, 21, main)
        print("The number yelled by root monkey is {0}".format(ans))
