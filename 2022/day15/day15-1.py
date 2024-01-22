from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(abspath(__file__))))
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


def positionsWithoutBeaconsInRow(locations, row):
    sensorAndBeaconSignals = mapFromSensorAndBeacons(locations)
    intervals = []
    beacon = {}
    for signal in sensorAndBeaconSignals:
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
    noBeacon = -len(beacon.keys())
    for pair in tmp:
        noBeacon += abs(pair[1] - pair[0]) + 1
    return noBeacon


def main(filename, row):
    locations = parseInformation(filename)
    positionsWithoutBeacon = positionsWithoutBeaconsInRow(locations, row)
    return positionsWithoutBeacon


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        row = 10
        performTests(15, [26], main, row)
    else:
        row = 2 * 10**6
        ans = getAnswer(15, main, row)
        print(
            "The number of positions without beacons in row {0} is {1}".format(row, ans)
        )
