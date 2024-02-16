from time import sleep, time
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


def operations(ops, state):
    pushes = 1000
    startState = deepcopy(state)
    neg = 0
    pos = 0
    i = 0
    for i in range(pushes):
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
            queue = []
            for op in addToQueue:
                queue.append(op)
        completed = True
        for node in state:
            if startState[node]["state"] != state[node]["state"]:
                completed = False
                break
        if completed:
            break
    m = 1000 // (i + 1)
    return (m * pos) * (m * neg)


def main(filename):
    ops, state = parseInformation(filename)
    result = operations(ops, state)
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
        performTests(2023, 20, [11687500, 32000000], main)
    else:
        ans = getAnswer(2023, 20, main)
        print("The total of rating numbers of all parts is: {0}".format(ans))
