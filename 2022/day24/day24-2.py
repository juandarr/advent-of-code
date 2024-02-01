from heapq import heappop, heappush
from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from utils import performTests, getAnswer  # noqa E402


# Generally useful data
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, down, left, right


def parseInformation(filename):
    dataLines = open(filename, "r")
    dataLines = dataLines.readlines()
    valley = [list(row.strip()) for row in dataLines]
    limits = {"i": [0, len(valley) - 3], "j": [0, len(valley[0]) - 3]}
    hStateBlizzards = [{}]
    vStateBlizzards = [{}]
    blizzardMotion = {"^": 0, "v": 1, "<": 2, ">": 3}
    for i, row in enumerate(valley):
        for j, spot in enumerate(row):
            if spot in ["v", "^"]:
                vStateBlizzards[-1][(i - 1, j - 1)] = [blizzardMotion[spot]]
            elif spot in ["<", ">"]:
                hStateBlizzards[-1][(i - 1, j - 1)] = [blizzardMotion[spot]]
    h = len(valley[0][2:-1])
    v = len(valley[2:-1])
    for _ in range(h):
        hStateBlizzards.append({})
        updateBlizzards(hStateBlizzards, directions, limits)
    for _ in range(v):
        vStateBlizzards.append({})
        updateBlizzards(vStateBlizzards, directions, limits)
    return valley, hStateBlizzards, vStateBlizzards


def updateBlizzards(blizzards, directions, limits):
    for location in blizzards[-2]:
        for dirBlizzard in blizzards[-2][location]:
            dir = directions[dirBlizzard]
            newLoc = (
                (location[0] + dir[0]) % (limits["i"][1] + 1),
                (location[1] + dir[1]) % (limits["j"][1] + 1),
            )
            if newLoc in blizzards[-1]:
                blizzards[-1][newLoc].append(dirBlizzard)
            else:
                blizzards[-1][newLoc] = [dirBlizzard]


def heuristicScore(start, goal):
    # L1 distance
    return abs(goal[0] - start[0]) + abs(goal[1] - start[1])


def moveInValley(valley, hStateBlizzards, vStateBlizzards):
    limits = {"i": [0, len(valley) - 3], "j": [0, len(valley[0]) - 3]}
    pastTime = 0
    s = (-1, 0)
    g = (limits["i"][1] + 1, limits["j"][1])
    for journeys in ((s, g), (g, s), (s, g)):
        # f-score and (node, (horizontal blizzard cycle, vertical blizzard cycle))
        start, goal = journeys
        h = pastTime % len(hStateBlizzards)
        v = pastTime % len(vStateBlizzards)
        toExpand = [(pastTime, (start, (h, v)))]
        gScore = {(start, (h, v)): pastTime}
        fScore = {
            (start, (h, v)): gScore[(start, (h, v))] + heuristicScore(start, goal)
        }
        while toExpand:
            node = heappop(toExpand)
            current = node[1][0]
            cycle = node[1][1]
            if current == goal:
                pastTime = gScore[(goal, cycle)]
                break
            if current == s:
                dirs = [(1, 0), (0, 0)]
            elif current == g:
                dirs = [(-1, 0), (0, 0)]
            else:
                dirs = [*directions, (0, 0)]
            for dir in dirs:
                neighbor = (current[0] + dir[0], current[1] + dir[1])
                if neighbor not in [s, g]:
                    if (
                        neighbor[0] < limits["i"][0]
                        or neighbor[0] > limits["i"][1]
                        or neighbor[1] < limits["j"][0]
                        or neighbor[1] > limits["j"][1]
                    ):
                        continue
                tentativeGScore = gScore[(current, cycle)] + 1
                h = tentativeGScore % len(hStateBlizzards)
                v = tentativeGScore % len(vStateBlizzards)
                c = (h, v)
                if (
                    neighbor not in hStateBlizzards[h]
                    and neighbor not in vStateBlizzards[v]
                ):
                    if (neighbor, c) not in gScore or tentativeGScore < gScore[
                        (neighbor, c)
                    ]:
                        gScore[(neighbor, c)] = tentativeGScore
                        fScore[(neighbor, c)] = gScore[(neighbor, c)] + heuristicScore(
                            neighbor, goal
                        )
                        heappush(toExpand, (fScore[(neighbor, c)], (neighbor, c)))
    return pastTime


def main(filename):
    valley, hStateBlizzards, vStateBlizzards = parseInformation(filename)
    time = moveInValley(valley, hStateBlizzards, vStateBlizzards)
    return time


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(24, [18 + 23 + 13], main)
    else:
        ans = getAnswer(24, main)
        print("The minimal time to reach the goal is {0}".format(ans))
