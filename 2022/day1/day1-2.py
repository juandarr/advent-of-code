def parseInformation(filename):
    file = open(filename, "r")
    calories = file.readlines()
    return list(map(lambda c: c.strip(), calories))

def max3Calories(calories):
    biggest3 = [0, 0, 0]
    current = 0
    for calorie in calories:
        if calorie == '':
            for idx, val in enumerate(biggest3):
                if (val < current):
                    for i in range(2,idx,-1):
                        biggest3[i] = biggest3[i-1]
                    biggest3[idx] = current
                    break
            current = 0
        else:
            current += int(calorie)
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
    print(calories)
    biggest3 = max3Calories(calories)
    print("Top 3 calorie amounts are {0}".format(biggest3))
    print("Total sum is {0}".format(sum(biggest3)))
