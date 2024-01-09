def parseInformation(filename):
    file = open(filename, "r")
    calories = file.readlines()
    return calories

def maxCalories(calories):
    biggest = 0
    current = 0
    for calorie in calories:
        if calorie == '\n':
            if (biggest < current):
                biggest = current
            current = 0
        else:
            current += int(calorie)
    return biggest

if __name__=='__main__': 
    calories = parseInformation("day1-input.txt")
    biggest = maxCalories(calories)
    print("Biggest calorie amount is: {0}".format(biggest))
