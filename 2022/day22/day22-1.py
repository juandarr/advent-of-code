import re
from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    dataLines = open(filename, "r")
    dataLines = dataLines.readlines()
    # Goals
    # 1) Codify map in hashmap data structure
    #     - Include start of row, end of row, start of column, end of column and landmarks
    # 2) Store instructions start from steps followed by change in direction
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
    # print(map,instructions)
    return map, landmarks, instructions


def moveInMap(map, landmarks, instructions):
    # Goals:
    # Create key of change of direction
    # Create movement mechanism per direction
    directionChange = {
        "R": {(0): (1), (1): (2), (2): (3), (3): (0)},
        "L": {(0): (3), (1): (0), (2): (1), (3): (2)},
    }
    motion = {(0): (0, 1), (1): (1, 0), (2): (0, -1), (3): (-1, 0)}
    position = [1, map["row"]["1"][0]]
    while tuple(position) in landmarks:
        position[1] += 1
    direction = 0
    # print(position)
    for instruction in instructions:
        # print('start',position,direction)
        if isinstance(instruction, int):
            for _ in range(instruction):
                i = position[0] + motion[direction][0]
                j = position[1] + motion[direction][1]
                # print('i,j',i,j)
                if direction in [(1), (3)] and i < map["col"][str(j)][0]:
                    i = max(map["col"][str(j)])
                    # print('i',i)
                elif direction in [(1), (3)] and i > map["col"][str(j)][1]:
                    i = min(map["col"][str(j)])
                    # print('i',i)
                elif direction in [(0), (2)] and j < map["row"][str(i)][0]:
                    j = max(map["row"][str(i)])
                    # print('j',j)
                elif direction in [(0), (2)] and j > map["row"][str(i)][1]:
                    j = min(map["row"][str(i)])
                    # print('j',j)
                if (i, j) not in landmarks:
                    position = [i, j]
                else:
                    break
        else:
            direction = directionChange[instruction][direction]
        # print('end',position,direction)
    return 1000 * position[0] + 4 * position[1] + direction


def main(filename):
    map, landmarks, instructions = parseInformation(filename)
    result = moveInMap(map, landmarks, instructions)
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
        performTests(2022, 22, [6032], main)
    else:
        ans = getAnswer(2022, 22, main)
        print("The final password is {0}".format(ans))
