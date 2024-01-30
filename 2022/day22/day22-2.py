import re
from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    dataLines = open(filename, "r")
    dataLines = dataLines.readlines()
    map = {"row": {}, "col": {}}
    landmarks = {}
    for idxRow, row in enumerate(dataLines[:-2]):
        prev = " "
        row = row.rstrip()
        for idxCol, col in enumerate(row):
            # Store minimum index in row
            if col == "#":
                landmarks[(idxRow + 1, idxCol + 1)] = 1
            if col in [".", "#"]:
                # Store minimum row index of column
                if str(idxCol + 1) not in map["col"]:
                    map["col"][str(idxCol + 1)] = [idxRow + 1]
                # Store maximum row index of column
                elif len(map["col"][str(idxCol + 1)]) == 1:
                    map["col"][str(idxCol + 1)].append(idxRow + 1)
                else:
                    if map["col"][str(idxCol + 1)][-1] < (idxRow + 1):
                        map["col"][str(idxCol + 1)][-1] = idxRow + 1
            # Store minimum column index of row
            if prev == " " and col in [".", "#"]:
                map["row"][str(idxRow + 1)] = [idxCol + 1]
            # Store maximum column index of row
            elif (prev in [".", "#"] and col == "") or (
                col in [".", "#"] and idxCol + 1 == len(row)
            ):
                map["row"][str(idxRow + 1)].append(idxCol + 1)
            prev = col
    instructions = dataLines[-1].strip()
    steps = re.findall("[0-9]+", instructions)
    directions = re.findall("[A-Z]", instructions)
    instructions = []
    for idx, d in enumerate(directions):
        instructions.append(int(steps[idx]))
        instructions.append(d)
    instructions.append(int(steps[len(steps) - 1]))
    return map, landmarks, instructions


def copySide(warped, size, position, side):
    tmp = []
    dir = ""
    # Side meaning:
    # lud: left up down
    # ldu: left down up
    # rud: right up down
    # rdu: right down up
    # tlr: top left right
    # trl: top right left
    # blr: bottom left right
    # brl: bottom right left
    if side == "lud":
        for i in range(position[0] * size + 1, (position[0] + 1) * size + 1):
            tmp.append(warped[i][position[1] * size + 1])
            dir = "r"
    elif side == "ldu":
        for i in range((position[0] + 1) * size, position[0] * size, -1):
            tmp.append(warped[i][position[1] * size + 1])
            dir = "r"
    elif side == "rud":
        for i in range(position[0] * size + 1, (position[0] + 1) * size + 1):
            tmp.append(warped[i][(position[1] + 1) * size])
            dir = "l"
    elif side == "rdu":
        for i in range((position[0] + 1) * size, position[0] * size, -1):
            tmp.append(warped[i][(position[1] + 1) * size])
            dir = "l"
    elif side == "tlr":
        for j in range(position[1] * size + 1, (position[1] + 1) * size + 1):
            tmp.append(warped[position[0] * size + 1][j])
            dir = "d"
    elif side == "trl":
        for j in range((position[1] + 1) * size, position[1] * size, -1):
            tmp.append(warped[position[0] * size + 1][j])
            dir = "d"
    elif side == "blr":
        for j in range(position[1] * size + 1, (position[1] + 1) * size + 1):
            tmp.append(warped[(position[0] + 1) * size][j])
            dir = "u"
    elif side == "brl":
        for j in range((position[1] + 1) * size, position[1] * size, -1):
            tmp.append(warped[(position[0] + 1) * size][j])
            dir = "u"
    return [tmp, dir]


def pasteSide(warped, size, position, side, tmp, dir):
    idx = 0
    if side == "lud":
        for i in range(position[0] * size + 1, (position[0] + 1) * size + 1):
            if warped[i][position[1] * size] == 0:
                warped[i][position[1] * size] = {
                    (i, position[1] * size + 1): [tmp[idx], dir]
                }
            else:
                warped[i][position[1] * size][(i, position[1] * size + 1)] = [
                    tmp[idx],
                    dir,
                ]
            idx += 1
    elif side == "ldu":
        for i in range((position[0] + 1) * size, position[0] * size, -1):
            if warped[i][position[1] * size] == 0:
                warped[i][position[1] * size] = {
                    (i, position[1] * size + 1): [tmp[idx], dir]
                }
            else:
                warped[i][position[1] * size][(i, position[1] * size + 1)] = [
                    tmp[idx],
                    dir,
                ]
            idx += 1
    elif side == "rud":
        for i in range(position[0] * size + 1, (position[0] + 1) * size + 1):
            if warped[i][(position[1] + 1) * size + 1] == 0:
                warped[i][(position[1] + 1) * size + 1] = {
                    (i, (position[1] + 1) * size): [tmp[idx], dir]
                }
            else:
                warped[i][(position[1] + 1) * size + 1][
                    (i, (position[1] + 1) * size)
                ] = [tmp[idx], dir]
            idx += 1
    elif side == "rdu":
        for i in range((position[0] + 1) * size, position[0] * size, -1):
            if warped[i][(position[1] + 1) * size + 1] == 0:
                warped[i][(position[1] + 1) * size + 1] = {
                    (i, (position[1] + 1) * size): [tmp[idx], dir]
                }
            else:
                warped[i][(position[1] + 1) * size + 1][
                    (i, (position[1] + 1) * size)
                ] = [tmp[idx], dir]
            idx += 1
    elif side == "tlr":
        for j in range(position[1] * size + 1, (position[1] + 1) * size + 1):
            if warped[position[0] * size][j] == 0:
                warped[position[0] * size][j] = {
                    (position[0] * size + 1, j): [tmp[idx], dir]
                }
            else:
                warped[position[0] * size][j][(position[0] * size + 1, j)] = [
                    tmp[idx],
                    dir,
                ]
            idx += 1
    elif side == "trl":
        for j in range((position[1] + 1) * size, position[1] * size, -1):
            if warped[position[0] * size][j] == 0:
                warped[position[0] * size][j] = {
                    (position[0] * size + 1, j): [tmp[idx], dir]
                }
            else:
                warped[position[0] * size][j][(position[0] * size + 1, j)] = [
                    tmp[idx],
                    dir,
                ]
            idx += 1
    elif side == "blr":
        for j in range(position[1] * size + 1, (position[1] + 1) * size + 1):
            if warped[(position[0] + 1) * size + 1][j] == 0:
                warped[(position[0] + 1) * size + 1][j] = {
                    ((position[0] + 1) * size, j): [tmp[idx], dir]
                }
            else:
                warped[(position[0] + 1) * size + 1][j][
                    ((position[0] + 1) * size, j)
                ] = [tmp[idx], dir]
            idx += 1
    elif side == "brl":
        for j in range((position[1] + 1) * size, position[1] * size, -1):
            if warped[(position[0] + 1) * size + 1][j] == 0:
                warped[(position[0] + 1) * size + 1][j] = {
                    ((position[0] + 1) * size, j): [tmp[idx], dir]
                }
            else:
                warped[(position[0] + 1) * size + 1][j][
                    ((position[0] + 1) * size, j)
                ] = [tmp[idx], dir]
            idx += 1
    return warped


def warpTest(warped, size):
    # 2/14 - 1,2
    tmp, dir = copySide(warped, size, (2, 3), "tlr")
    warped = pasteSide(warped, size, (1, 2), "rdu", tmp, dir)

    tmp, dir = copySide(warped, size, (1, 2), "rdu")
    warped = pasteSide(warped, size, (2, 3), "tlr", tmp, dir)

    # 4/14 2,3
    tmp, dir = copySide(warped, size, (0, 2), "rdu")
    warped = pasteSide(warped, size, (2, 3), "rud", tmp, dir)

    tmp, dir = copySide(warped, size, (2, 3), "rud")
    warped = pasteSide(warped, size, (0, 2), "rdu", tmp, dir)

    # 6/14 3,6
    tmp, dir = copySide(warped, size, (0, 2), "trl")
    warped = pasteSide(warped, size, (1, 0), "tlr", tmp, dir)

    tmp, dir = copySide(warped, size, (1, 0), "tlr")
    warped = pasteSide(warped, size, (0, 2), "trl", tmp, dir)

    # 8/14 5,6
    tmp, dir = copySide(warped, size, (0, 2), "ldu")
    warped = pasteSide(warped, size, (1, 1), "trl", tmp, dir)

    tmp, dir = copySide(warped, size, (1, 1), "trl")
    warped = pasteSide(warped, size, (0, 2), "ldu", tmp, dir)

    # 10/14 3,8
    tmp, dir = copySide(warped, size, (1, 0), "lud")
    warped = pasteSide(warped, size, (2, 3), "brl", tmp, dir)

    tmp, dir = copySide(warped, size, (2, 3), "brl")
    warped = pasteSide(warped, size, (1, 0), "lud", tmp, dir)

    # 12/14 7,8
    tmp, dir = copySide(warped, size, (2, 2), "blr")
    warped = pasteSide(warped, size, (1, 0), "brl", tmp, dir)

    tmp, dir = copySide(warped, size, (1, 0), "brl")
    warped = pasteSide(warped, size, (2, 2), "blr", tmp, dir)

    # 14/14 4,7
    tmp, dir = copySide(warped, size, (1, 1), "brl")
    warped = pasteSide(warped, size, (2, 2), "lud", tmp, dir)

    tmp, dir = copySide(warped, size, (2, 2), "lud")
    warped = pasteSide(warped, size, (1, 1), "brl", tmp, dir)
    # for i in warped:
    #     print(i)
    return warped


def warpProblem2(warped, size):
    # 2/14 - 1,2
    tmp, dir = copySide(warped, size, (0, 2), "blr")
    warped = pasteSide(warped, size, (1, 1), "rud", tmp, dir)

    tmp, dir = copySide(warped, size, (1, 1), "rud")
    warped = pasteSide(warped, size, (0, 2), "blr", tmp, dir)

    # 4/14 2,3
    tmp, dir = copySide(warped, size, (0, 2), "rdu")
    warped = pasteSide(warped, size, (2, 1), "rud", tmp, dir)

    tmp, dir = copySide(warped, size, (2, 1), "rud")
    warped = pasteSide(warped, size, (0, 2), "rdu", tmp, dir)

    # 6/14 3,4
    tmp, dir = copySide(warped, size, (2, 1), "brl")
    warped = pasteSide(warped, size, (3, 0), "rdu", tmp, dir)

    tmp, dir = copySide(warped, size, (3, 0), "rdu")
    warped = pasteSide(warped, size, (2, 1), "brl", tmp, dir)

    # 8/14 3,7
    tmp, dir = copySide(warped, size, (0, 2), "trl")
    warped = pasteSide(warped, size, (3, 0), "brl", tmp, dir)

    tmp, dir = copySide(warped, size, (3, 0), "brl")
    warped = pasteSide(warped, size, (0, 2), "trl", tmp, dir)

    # 10/14 7,8
    tmp, dir = copySide(warped, size, (0, 1), "trl")
    warped = pasteSide(warped, size, (3, 0), "ldu", tmp, dir)

    tmp, dir = copySide(warped, size, (3, 0), "ldu")
    warped = pasteSide(warped, size, (0, 1), "trl", tmp, dir)

    # 12/14 6,8
    tmp, dir = copySide(warped, size, (0, 1), "ldu")
    warped = pasteSide(warped, size, (2, 0), "lud", tmp, dir)

    tmp, dir = copySide(warped, size, (2, 0), "lud")
    warped = pasteSide(warped, size, (0, 1), "ldu", tmp, dir)

    # 14/14 5,6
    tmp, dir = copySide(warped, size, (1, 1), "ldu")
    warped = pasteSide(warped, size, (2, 0), "trl", tmp, dir)

    tmp, dir = copySide(warped, size, (2, 0), "trl")
    warped = pasteSide(warped, size, (1, 1), "ldu", tmp, dir)
    return warped


def warp(map, test):
    warped = []
    size = 10**12
    for i in map["row"]:
        tmp = map["row"][i][1] - map["row"][i][0] + 1
        if size > tmp:
            size = tmp
    warped.append([0] * (4 * size + 2))
    for i in map["row"]:
        # print(map['row'][i])
        tmp = [0]
        for idx in range(4 * size):
            if idx + 1 <= map["row"][i][1] and idx + 1 >= map["row"][i][0]:
                tmp.append((int(i), idx + 1))
            else:
                tmp.append(0)
        tmp.append(0)
        warped.append(tmp)
    warped.append([0] * (4 * size + 2))
    if test:
        warped = warpTest(warped, size)
    else:
        warped = warpProblem2(warped, size)
    return warped


def moveInMap(map, landmarks, instructions, test=False):
    warped = warp(map, test)
    directionChange = {
        "R": {(0): (1), (1): (2), (2): (3), (3): (0)},
        "L": {(0): (3), (1): (0), (2): (1), (3): (2)},
    }
    motion = {(0): (0, 1), (1): (1, 0), (2): (0, -1), (3): (-1, 0)}
    position = [1, map["row"]["1"][0]]
    while tuple(position) in landmarks:
        position[1] += 1
    direction = 0
    directionMap = {"l": (2), "r": (0), "u": (3), "d": (1)}
    idx = 0
    for instruction in instructions:
        if isinstance(instruction, int):
            for _ in range(instruction):
                idx += 1
                i = position[0] + motion[direction][0]
                j = position[1] + motion[direction][1]
                # The goal here is to fand the mapping to get access to each new face location and direction
                # Once the limit has been reached
                key = (position[0], position[1])
                tmpDir = direction
                if direction in [(1), (3)] and i < map["col"][str(j)][0]:
                    tmpDir = directionMap[warped[i][j][key][1]]
                    i, j = warped[i][j][key][0]
                elif direction in [(1), (3)] and i > map["col"][str(j)][1]:
                    tmpDir = directionMap[warped[i][j][key][1]]
                    i, j = warped[i][j][key][0]
                elif direction in [(0), (2)] and j < map["row"][str(i)][0]:
                    tmpDir = directionMap[warped[i][j][key][1]]
                    i, j = warped[i][j][key][0]
                elif direction in [(0), (2)] and j > map["row"][str(i)][1]:
                    tmpDir = directionMap[warped[i][j][key][1]]
                    i, j = warped[i][j][key][0]

                if (i, j) not in landmarks:
                    direction = tmpDir
                    position = [i, j]
                else:
                    break
        else:
            direction = directionChange[instruction][direction]
    return 1000 * position[0] + 4 * position[1] + direction


def main(filename, test):
    map, landmarks, instructions = parseInformation(filename)
    result = moveInMap(map, landmarks, instructions, test)
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
        performTests(22, [5031], main, True)
    else:
        ans = getAnswer(22, main, False)
        print("The final password is {0}".format(ans))
