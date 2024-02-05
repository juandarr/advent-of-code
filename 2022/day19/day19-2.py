import re
import copy
from math import ceil

from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    tmp = file.read()
    tmp = tmp.rstrip().split("\n")
    bps = []
    robots = ["oreRobot", "clayRobot", "obsidianRobot", "geodeRobot"]
    resourcesKeys = {
        "oreRobot": ["ore"],
        "clayRobot": ["ore"],
        "obsidianRobot": ["ore", "clay"],
        "geodeRobot": ["ore", "obsidian"],
    }
    for line in tmp:
        blueprint = re.findall("[0-9]+", line)
        bp = {"id": int(blueprint[0])}
        idx = 1
        for robot in robots:
            bp[robot] = {}
            for resource in resourcesKeys[robot]:
                bp[robot][resource] = int(blueprint[idx])
                idx += 1

        maxSpend = {"ore": 0, "clay": 0, "obsidian": 0}
        for robot in robots:
            for resource in bp[robot]:
                maxSpend[resource] = max(maxSpend[resource], bp[robot][resource])
        bp["maxSpend"] = maxSpend
        bps.append(bp)
    return bps


def simulateMining(blueprints):
    product = 1

    for blueprint in blueprints:
        # blueprintFile = open("bp.txt",'a')
        if blueprint["id"] == 4:
            return product
        c = 0
        # print("\nBlueprint {0}".format(blueprint["id"]))
        # print(blueprint)
        # blueprintFile.write('\nBlueprint {0}\n{1}'.format(blueprint['id'],blueprint))
        t = 0
        limit = 32

        # print(maxSpend)
        maxSpend = blueprint["maxSpend"]

        # Used to calculate the minimal time needed to reach the necessary resources to acquire a robot
        bots = ["oreRobot", "clayRobot", "obsidianRobot", "geodeRobot"]
        resources = ["ore", "clay", "obsidian", "geode"]

        toExpand = [[[[0], [], [], []], 0]]
        botRange = len(toExpand[-1][0])

        geodeCounter = 0
        bestState = []

        idx = 0
        toExpandLength = 1
        visited = {}

        while toExpandLength > idx:
            # Start expansion of last node with next time step
            t = toExpand[idx][1]
            tmpVal = float("inf")
            didChange = False
            for s in toExpand[idx][0]:
                if s != []:
                    if tmpVal > s[-1] and s[-1] > t:
                        tmpVal = s[-1]
                        didChange = True
            if didChange:
                t = tmpVal
                # Do nothing at current time step t
                toExpand.append([copy.deepcopy(toExpand[idx][0]), t])
                toExpandLength += 1
                c += 1
            # If time step reaches maximum move to the next node
            if t >= limit:
                idx += 1
                continue

            initialState = []
            # Used to avoid repeating element in state (Only one robot can be created for each time step)
            initialSet = set()
            for state in toExpand[idx][0]:
                tmp = []
                for e in state:
                    if e <= t:
                        tmp.append(e)
                        initialSet.add(e)
                initialState.append(tmp)

            key = str(initialState) + str(t)
            if key not in visited:
                visited[key] = 1
            else:
                idx += 1
                continue

            resAmt = [0, 0, 0]
            for m, botGroup in enumerate(initialState):
                if m == 3:
                    break
                for bot in botGroup:
                    if bot < t:
                        resAmt[m] += t - bot
                for n in range(len(bots)):
                    if resources[m] not in blueprint[bots[n]]:
                        continue
                    for bot in initialState[n]:
                        if n == 0 and bot == 0:
                            continue
                        if bot <= t:
                            resAmt[m] -= blueprint[bots[n]][resources[m]]

            for i in range(botRange):
                newState = copy.deepcopy(initialState)
                newSet = initialSet.copy()

                nextLoop = False
                breakLoop = False

                for j in range(i, botRange):
                    # Exit loop when the previous state for resource i-1 has not bots
                    # (bots for resource i are impossible to create)
                    if j > 0 and newState[j - 1] == []:
                        breakLoop = True
                        break
                    # When the slot i doesn't corresponde to the geode one
                    if j != 3:
                        # Skip creation of bot for resource i when the max required number
                        # of bots for resource i is already present
                        if (len(newState[j]) + 1 > maxSpend[resources[j]]) or maxSpend[
                            resources[j]
                        ] * (limit - t) <= (resAmt[j] + len(newState[j]) * (limit - t)):
                            nextLoop = True
                            break
                    # Minimal time step t required to get enough resources to obtain a robot for resource i
                    minT = []
                    for resource in blueprint[bots[j]]:
                        tmp = blueprint[bots[j]][resource]
                        for node in newState[resources.index(resource)]:
                            tmp += node
                        for jTmp in range(botRange):
                            if resource in blueprint[bots[jTmp]]:
                                cost = blueprint[bots[jTmp]][resource]
                                if jTmp == 0:
                                    tmp += (len(newState[jTmp]) - 1) * cost
                                else:
                                    tmp += (len(newState[jTmp])) * cost
                        tmp = ceil(tmp / len(newState[resources.index(resource)]))
                        minT.append(tmp + 1)
                    maxi = max(minT)
                    # Store maxi when not robot of type i has been created, or new spot available and not robot created at time maxi
                    if (
                        newState[j] == [] or maxi > (newState[j][-1])
                    ) and maxi not in newSet:
                        newState[j].append(maxi)
                        newSet.add(maxi)
                if breakLoop:
                    break
                if nextLoop:
                    continue
                tmpMin = 0
                for node in newState[-1]:
                    tmpMin += limit - node
                if tmpMin > geodeCounter:
                    geodeCounter = tmpMin
                    bestState = copy.deepcopy(newState)
                    # print(
                    #     "Best state: {0} with {1} geodes".format(
                    #         bestState, geodeCounter
                    #     )
                    # )
                # Consider whether the current state can be saved for expansion
                toExpand.append([copy.deepcopy(newState), t])
                toExpandLength += 1
                c += 1
            idx += 1
        if geodeCounter > 0:
            product *= geodeCounter
        # print(
        #     "Here was the best state: {0}, with product {1}".format(bestState, product)
        # )
    return product


def main(filename):
    blueprints = parseInformation(filename)
    totalQualityLevel = simulateMining(blueprints)
    return totalQualityLevel


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2022, 19, [56 * 62], main)
    else:
        ans = getAnswer(2022, 19, main)
        print(
            "The total product of all the blueprints largest geode numbers is {0}".format(
                ans
            )
        )
