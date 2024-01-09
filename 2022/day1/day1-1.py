def parseInformation(filename):
    file = open(filename, "r")
    calories = file.readlines()
    return list(map(lambda c: c.strip(), calories))

def maxCalories(calories):
    biggest = 0
    current = 0
    for calorie in calories:
        if calorie == '':
            if (biggest < current):
                biggest = current
            current = 0
        else:
            current += int(calorie)
    if (biggest < current):
        biggest = current
    return biggest

if __name__=='__main__': 
    test = False
    if test:
        filename = "day1-test-input.txt"
    else:
        filename = "day1-input.txt"
    calories = parseInformation(filename)
    biggest = maxCalories(calories)
    print("Biggest calorie amount is: {0}".format(biggest))
