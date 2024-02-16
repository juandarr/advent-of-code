from copy import deepcopy
from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    lines = file.readlines()
    # Read lines and expand by rows
    ops = {}
    for line in lines:
        tmp = line.strip().split("->")
        input = tmp[0].strip()
        if input[0] == "b":
            node = input
        else:
            node = input[1:]
        type = input[0]
        output = tmp[1].strip().split(", ")
        ops[node] = {"type": type, "output": output}

    # Calculate state
    state = {}
    for operation in ops:
        t = ops[operation]["type"]
        node = operation
        if t == "%":
            state[node] = {"type": "%", "state": False}
        elif t == "&":
            state[node] = {"type": "&", "state": True, "input": []}
        elif t == "b":
            state[node] = {
                "type": "b",
                "state": False,
                "output": ops[operation]["output"],
            }
    for node in state:
        if state[node]["type"] == "&":
            for node2 in ops:
                if node in ops[node2]["output"]:
                    state[node]["input"].append(node2)
    return ops, state


def primeDecomposition(number):
    primes = {}
    tmp = number
    c = 0
    while tmp % 2 == 0:
        tmp /= 2
        c += 1
    if c > 0:
        primes[2] = c
    div = 3
    while tmp > 1:
        c = 0
        while tmp % div == 0:
            tmp /= div
            c += 1
        if c > 0:
            primes[div] = c
        div += 2
    return primes


def operations(ops, state):
    pushes = 20000
    startState = deepcopy(state)
    neg = 0
    pos = 0
    repeated = [0, 0, 0, 0]
    end = [False, False, False, False]
    for i in range(pushes):
        # print('Pulse: ',i+1)
        neg += 1
        cur = "broadcaster"
        queue = []
        for e in ops[cur]["output"]:
            queue.append([False, e])
        while queue != []:
            addToQueue = []
            for q in queue:
                if q[0]:
                    pos += 1
                else:
                    neg += 1
                curSignal = q[0]
                node = q[1]
                t = ops[node]["type"]
                if t == "%":
                    if curSignal is False:
                        state[node]["state"] = not (state[node]["state"])
                        for n in ops[node]["output"]:
                            addToQueue.append([state[node]["state"], n])
                elif t == "&":
                    tmp = False
                    for n in state[node]["input"]:
                        if state[n]["state"] is False:
                            tmp = True
                            break
                    state[node]["state"] = tmp
                    for n in ops[node]["output"]:
                        if n in state:
                            addToQueue.append([tmp, n])
                        else:
                            if tmp:
                                pos += 1
                            else:
                                neg += 1
                if state["lk"]["state"] is True and i + 1 > 1 and not (end[0]):
                    # print('Pulse: ',i+1, 'lk: High!')
                    if repeated[0] == 0:
                        repeated[0] = i + 1
                    else:
                        if i + 1 == 2 * repeated[0]:
                            end[0] = True
                if state["zv"]["state"] is True and i + 1 > 1 and not (end[1]):
                    # print('Pulse: ',i+1, 'zv: High!')
                    if repeated[1] == 0:
                        repeated[1] = i + 1
                    else:
                        if i + 1 == 2 * repeated[1]:
                            end[1] = True
                if state["sp"]["state"] is True and i + 1 > 1 and not (end[2]):
                    # print('Pulse: ',i+1, 'sp: High!')
                    if repeated[2] == 0:
                        repeated[2] = i + 1
                    else:
                        if i + 1 == 2 * repeated[2]:
                            end[2] = True
                if state["xt"]["state"] is True and i + 1 > 1 and not (end[3]):
                    # print('Pulse: ',i+1, 'xt: High!')
                    if repeated[3] == 0:
                        repeated[3] = i + 1
                    else:
                        if i + 1 == 2 * repeated[3]:
                            end[3] = True
            queue = []
            for op in addToQueue:
                queue.append(op)
        completed = True
        for node in state:
            if startState[node]["state"] != state[node]["state"]:
                completed = False
                break
        endF = True
        for b in end:
            if b is False:
                endF = False
        if completed or endF:
            break
    return repeated


def fewestPresses(ops, state):
    repeated = operations(ops, state)
    print(repeated)
    for index, value in enumerate(repeated):
        repeated[index] = primeDecomposition(value)
    commonMultiple = {}
    for stepDict in repeated:
        for key in stepDict:
            if key in commonMultiple:
                if commonMultiple[key] < stepDict[key]:
                    commonMultiple[key] = stepDict[key]
            else:
                commonMultiple[key] = stepDict[key]
    net = 1
    for key in commonMultiple:
        net *= key ** commonMultiple[key]
    return net


def main(filename):
    ops, state = parseInformation(filename)
    ans = fewestPresses(ops, state)
    return ans


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')
    if test:
        performTests(2023, 20, [], main)
    else:
        ans = getAnswer(2023, 20, main)
        print("The fewests number of presses is: {0}".format(ans))
