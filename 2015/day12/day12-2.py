from os.path import dirname, abspath
import sys
import re

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from utils import performTests, getAnswer  # noqa E402


def parseInformation(filename):
    file = open(filename, "r")
    data = file.read()
    return data.rstrip() 

def union_of_ranges(ranges):
    if not ranges:
        return []

    # Sort ranges by start point, then by end point
    sorted_ranges = sorted(ranges, key=lambda x: (x[0], x[1]))

    merged_ranges = []
    current_merged_range = list(sorted_ranges[0])  # Start with the first range

    for i in range(1, len(sorted_ranges)):
        next_range = sorted_ranges[i]
        
        # Check for overlap or adjacency
        if next_range[0] <= current_merged_range[1] + 1:
            # Merge: update the end of the current merged range
            current_merged_range[1] = max(current_merged_range[1], next_range[1])
        else:
            # No overlap/adjacency, add the current merged range and start a new one
            merged_ranges.append(tuple(current_merged_range))
            current_merged_range = list(next_range)
    
    # Add the last merged range
    merged_ranges.append(tuple(current_merged_range))
    
    return merged_ranges

def findExclusionZones(s):
    pattern = "red"    
    indices = []
    idx = 0
    while True:
        idx = s.find(pattern,idx)
        if (idx != -1):
            indices.append(idx)
            idx +=1
        else:
            break
    bannedRanges = []
    for idx in indices:
        val = 0
        tmp = idx
        while val<=0:
            if (s[tmp] in [']','}']):
                val -= 1
            elif (s[tmp] in ['[','{']):
                val += 1
            tmp -= 1
        if s[tmp+1]=='[':
            continue
        start = tmp+1
        val = 0
        tmp = idx
        while val>=0:
            if (s[tmp] in [']','}']):
                val -= 1
            elif (s[tmp] in ['[','{']):
                val += 1
            tmp += 1
        end = tmp - 1
        bannedRanges.append([start,end])
    bannedRangesUnion = union_of_ranges(bannedRanges)
    return bannedRangesUnion

def addNumbers(s):
    bannedRanges = findExclusionZones(s)
    tmp = ''
    total = 0
    idx = 0
    exc = 0
    while idx<len(s):
        while s[idx].isdigit() or s[idx]=='-':
            tmp += s[idx]
            idx+=1
        if tmp !='':
            total += int(tmp)  
            tmp = ''
        idx +=1
        if exc < len(bannedRanges) and idx>= bannedRanges[exc][0]:
            idx = bannedRanges[exc][1]+1
            exc += 1
    return total

def main(filename):
    s = parseInformation(filename)
    net = addNumbers(s)
    return net

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "test":
        test = True
    elif args[0] == "main":
        test = False
    else:
        raise Exception('Wrong argument, expected "test" or "main"')

    if test:
        performTests(2015, 12, [4,0,6], main, test=["5","6","7"])
    else:
        iterations = getAnswer(2015, 12, main)
        print("The total sum of numbers in the JSON string excluding objects having property \"red\" is {0}".format(iterations))