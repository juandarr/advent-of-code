from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    tmp = file.read()
    tmp = tmp.rstrip().split("\n")
    locations = []
    for row in tmp:
        locations.append(row)
    return locations


def mapFromSensorAndBeacons(locations):
    sensorAndBeacon = []
    keys = ["sensor", "beacon", "d"]
    for location in locations:
        tmp = {}
        location = location.strip().split("x=")
        location = location[1:]
        location[0] = location[0].split(": closest")
        location[0] = location[0][0]
        for idx, i in enumerate(location):
            i = i.split(", y=")
            tmp[keys[idx]] = (int(i[0]), int(i[1]))
        tmp[keys[-1]] = abs(tmp["sensor"][0] - tmp["beacon"][0]) + abs(
            tmp["sensor"][1] - tmp["beacon"][1]
        )
        sensorAndBeacon.append(tmp)
    return sensorAndBeacon


def positionsWithoutBeacons(locations, rowLimit) -> tuple[int, int]:
    sensorAndBeaconSignals = mapFromSensorAndBeacons(locations)
    endRow = 0
    tmp = [[0, 0]]
    for row in range(rowLimit, -1, -1):
        intervals = []
        beacon = {}
        # print(row)
        for signal in sensorAndBeaconSignals:
            # print(signal)
            a = abs(row - signal["sensor"][1])
            b = signal["sensor"][0]
            d = signal["d"]
            high = d - a + b
            low = a + b - d
            if low < high:
                intervals.append((low, high))
            if signal["beacon"][1] == row:
                beacon[signal["beacon"][0]] = 1
        tmp = []
        for begin, end in sorted(intervals):
            if tmp and tmp[-1][1] >= begin - 1:
                tmp[-1][1] = max(tmp[-1][1], end)
            else:
                tmp.append([begin, end])
        if len(tmp) > 1:
            endRow = row
            break
    return (tmp[0][1] + 1, endRow)


def main(filename, rowLimit):
    locations = parseInformation(filename)
    singlePosition: tuple[int, int] = positionsWithoutBeacons(locations, rowLimit)
    tf = 4000000 * singlePosition[0] + singlePosition[1]
    return tf


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        rowLimit = 20
        performTests(2022, 15, [56000011], main, rowLimit)
    else:
        rowLimit = 4 * 10**6
        tf = getAnswer(2022, 15, main, rowLimit)
        print(
            "The tuning frequency for the only possible position for the distress beacon is {0}".format(
                tf
            )
        )
