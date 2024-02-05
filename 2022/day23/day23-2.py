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
        locations[locationsToUpdate[location]] = 1
    return locations


def moveInField(locations):
    directions = {
        "north": [{(-1, 1): 0, (-1, 0): 0, (-1, -1): 0}, (-1, 0), 0],
        "south": [{(1, 1): 0, (1, 0): 0, (1, -1): 0}, (1, 0), 0],
        "west": [{(1, -1): 0, (0, -1): 0, (-1, -1): 0}, (0, -1), 0],
        "east": [{(1, 1): 0, (0, 1): 0, (-1, 1): 0}, (0, 1), 0],
    }
    adjacents = [(-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1)]
    checker = ["north", "south", "west", "east"]
    rounds = 10**6
    roundComplete = 0
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
        if len(locationsToUpdate) == 0:
            roundComplete = r + 1
            break
        locations = updateField(locations, locationsToUpdate)
        checker = [*checker[1:], checker[0]]
    return roundComplete


def main(filename):
    field, locations = parseInformation(filename)
    emptyGround = moveInField(locations)
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
        performTests(2022, 23, [20], main)
    else:
        ans = getAnswer(2022, 23, main)
        print(
            "The number of rounds before the elves are completely distributed is {0}".format(
                ans
            )
        )
