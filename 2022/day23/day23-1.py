from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    dataLines = open(filename, "r")
    dataLines = dataLines.readlines()
    field = [list(row.strip()) for row in dataLines]
    locations = {}
    for i, row in enumerate(field):
        for j, spot in enumerate(row):
            if spot == "#":
                locations[(i, j)] = 1
    return field, locations


def updateField(locations, locationsToUpdate):
    for location in locationsToUpdate:
        del locations[location]
        dest = locationsToUpdate[location]
        locations[dest] = 1
    return locations


def moveInField(field, locations):
    limits = {"i": [0, len(field) - 1], "j": [0, len(field[0]) - 1]}
    directions = {
        "north": [[(-1, 1), (-1, 0), (-1, -1)], (-1, 0)],
        "south": [[(1, 1), (1, 0), (1, -1)], (1, 0)],
        "west": [[(1, -1), (0, -1), (-1, -1)], (0, -1)],
        "east": [[(1, 1), (0, 1), (-1, 1)], (0, 1)],
    }
    adjacents = [(-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1)]
    checker = ["north", "south", "west", "east"]
    rounds = 10
    for r in range(rounds):
        newLocations = {}
        for location in locations:
            free = {}
            freeCounter = 0
            for adj in adjacents:
                tmp = (location[0] + adj[0], location[1] + adj[1])
                free[adj] = 1 if tmp not in locations else 0
                freeCounter += free[adj]
            if freeCounter < 8:
                for direction in checker:
                    if sum([free[i] for i in directions[direction][0]]) == 3:
                        inc = directions[direction][1]
                        tmp = (location[0] + inc[0], location[1] + inc[1])
                        if tmp in newLocations:
                            newLocations[tmp].append(location)
                        else:
                            newLocations[tmp] = [location]
                        break
        locationsToUpdate = {}
        for newLocation in newLocations:
            if len(newLocations[newLocation]) == 1:
                locationsToUpdate[newLocations[newLocation][0]] = newLocation
        locations = updateField(locations, locationsToUpdate)
        checker = [*checker[1:], checker[0]]
    limits: dict[str, list[float | int]] = {
        "i": [float("inf"), -float("inf")],
        "j": [float("inf"), -float("inf")],
    }
    for i, j in locations:
        if i < limits["i"][0]:
            limits["i"][0] = i
        if i > limits["i"][1]:
            limits["i"][1] = i
        if j < limits["j"][0]:
            limits["j"][0] = j
        if j > limits["j"][1]:
            limits["j"][1] = j
    emptyCounter = 0
    for i in range(int(limits["i"][0]), int(limits["i"][1] + 1)):
        for j in range(int(limits["j"][0]), int(limits["j"][1] + 1)):
            if (i, j) not in locations:
                emptyCounter += 1
    return emptyCounter


def main(filename):
    field, locations = parseInformation(filename)
    emptyGround = moveInField(field, locations)
    return emptyGround


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2022, 23, [110], main)
    else:
        ans = getAnswer(2022, 23, main)
        print("The number of empty ground tiles is {0}".format(ans))
