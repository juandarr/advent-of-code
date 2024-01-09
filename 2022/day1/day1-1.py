def parseInformation(filename):
    file = open(filename, "r")
    calories = file.read()
    calories = calories.rstrip().split('\n\n')
    return list(map(lambda c: map(int,tuple(c.split('\n'))), calories))

def maxCalories(calories):
    biggest = 0
    for group in calories:
        current = 0
        for calorie in group:
            current += calorie
            if (biggest < current):
                biggest = current
    return biggest

if __name__=='__main__': 
    test = True
    if test:
        filename = "day1-test-input.txt"
    else:
        filename = "day1-input.txt"
    calories = parseInformation(filename)
    biggest = maxCalories(calories)
    print("Biggest calorie amount is: {0}".format(biggest))
