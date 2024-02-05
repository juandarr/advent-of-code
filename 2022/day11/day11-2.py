from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    tmp = file.read()
    tmp = tmp.rstrip().split("\n")
    monkeys = []
    for row in tmp:
        row = row.strip().split(" ")
        if row[0] == "Monkey":
            monkeys.append({"test": {}, "inspections": 0})
        else:
            if row[0] == "Starting":
                items = []
                for item in row[2:]:
                    item = item.replace(",", "")
                    items.append(int(item))
                monkeys[-1]["items"] = items
            elif row[0] == "Operation:":
                operation = []
                for op in row[4:]:
                    operation.append(op)
                monkeys[-1]["operation"] = operation
            elif row[0] == "Test:":
                divisor = int(row[-1])
                monkeys[-1]["divisor"] = divisor
            elif row[0] == "If":
                monkeys[-1]["test"][row[1].replace(":", "")] = int(row[-1])
    return monkeys


def monkeyRounds(monkeys, rounds):
    div = 1
    for monkey in monkeys:
        div *= monkey["divisor"]
    for _ in range(1, rounds + 1):
        for idx, monkey in enumerate(monkeys):
            items = monkey["items"]
            for item in items:
                monkeys[idx]["inspections"] += 1
                if monkey["operation"][1] == "old":
                    worry = eval(str(item) + monkey["operation"][0] + str(item))
                else:
                    worry = eval(
                        str(item) + monkey["operation"][0] + monkey["operation"][1]
                    )
                worry = worry % div
                if worry % monkey["divisor"] == 0:
                    monkeys[monkey["test"]["true"]]["items"].append(worry)
                else:
                    monkeys[monkey["test"]["false"]]["items"].append(worry)
            monkeys[idx]["items"] = []
    maxInspections = [0, 0]
    for monkey in monkeys:
        if maxInspections[0] < monkey["inspections"]:
            tmp = maxInspections[0]
            maxInspections[0] = monkey["inspections"]
            maxInspections[1] = tmp
        elif maxInspections[1] < monkey["inspections"]:
            maxInspections[1] = monkey["inspections"]
    monkeyBusiness = 1
    for i in maxInspections:
        monkeyBusiness *= i
    return monkeyBusiness


def main(filename):
    monkeys = parseInformation(filename)
    rounds = 10**4
    monkeyBusiness = monkeyRounds(monkeys, rounds)
    return monkeyBusiness


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2022, 11, [52166 * 52013], main)
    else:
        ans = getAnswer(2022, 11, main)
        print("The monkey business is {0}".format(ans))
