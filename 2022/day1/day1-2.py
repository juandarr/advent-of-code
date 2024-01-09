def parseInformation(filename):
    file = open(filename, "r")
    calories = file.read()
    calories = calories.rstrip().split('\n\n')
    return list(map(lambda c: map(int,tuple(c.split('\n'))), calories))

def max3Calories(calories):
    biggest3 = [0, 0, 0]
    current = 0
    for group in calories:
        current = 0
        for calorie in group:
            current += calorie
        for idx, val in enumerate(biggest3):
            if (val < current):
                for i in range(2,idx,-1):
                    biggest3[i] = biggest3[i-1]
                biggest3[idx] = current
                break
    return biggest3

if __name__=='__main__': 
    test = False
    if test:
        filename = "day1-test-input.txt"
    else:
        filename = "day1-input.txt"
    calories = parseInformation(filename)
    biggest3 = max3Calories(calories)
    print("Top 3 calorie amounts are {0}".format(biggest3))
    print("Total sum is {0}".format(sum(biggest3)))
