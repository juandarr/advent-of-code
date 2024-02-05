from heapq import heappop, heappush
from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
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
    # L1 (manhattan) distance
    return (goal[0] - start[0]) + (goal[1] - start[1])


def moveInValley(valley, hStateBlizzards, vStateBlizzards):
    limits = {"i": [0, len(valley) - 3], "j": [0, len(valley[0]) - 3]}
    start = (0, 0)
    goal = (limits["i"][1], limits["j"][1])
    # f-score and (node, (horizontal blizzard cycle, vertical blizzard cycle))
    toExpand: list[tuple[int, tuple[tuple[int, int], int]]] = [(1, (start, 1))]
    gScore: dict[tuple[tuple[int, int], int], int] = {(start, 1): 1}
    fScore: dict[tuple[tuple[int, int], int], int] = {
        (start, 1): gScore[(start, 1)] + heuristicScore(start, goal)
    }
    while toExpand:
        node = heappop(toExpand)
        current = node[1][0]
        cycle = node[1][1]
        if current == goal:
            return gScore[(current, cycle)] + 1
        for dir in [*directions, (0, 0)]:
            neighbor = (current[0] + dir[0], current[1] + dir[1])
            # print(neighbor)
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
            c = tentativeGScore
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
    return None


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
        performTests(2022, 24, [18], main)
    else:
        ans = getAnswer(2022, 24, main)
        print("The minimal time to reach the goal is {0}".format(ans))
