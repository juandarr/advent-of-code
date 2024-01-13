def parseInformation(filename):
    file = open(filename, "r")
    tmp= file.read()
    tmp= tmp.rstrip().split('\n')
    return list(tmp[0])

def checkMarkerLocation(nCharacters,stream):
    distinctCharacters = nCharacters 
    idx = 0
    currentStarter = {}
    # Store fist nCharacters in hash map
    while (idx<distinctCharacters):
        k = stream[idx]
        if k in currentStarter:
            currentStarter[k] += 1 
        else:
            currentStarter[k] = 1
        idx +=1
    # While unique consecutive characters is different from distinctCharacters
    while (len(currentStarter)<distinctCharacters):
        # Remove last character in sequence to count the next one
        k = stream[idx-distinctCharacters]
        if (currentStarter[k]>1):
            currentStarter[k] -= 1
        else:
            currentStarter.pop(k)
        # Count next character
        k = stream[idx]
        if k in currentStarter:
            currentStarter[k]+=1
        else:
            currentStarter[k]=1
        idx +=1
    return idx

def getLocation(filename, positions):
    s = parseInformation(filename)
    location = checkMarkerLocation(positions,s)
    return location

if __name__=='__main__': 
    test = False
    positions = 14
    if test:
        answers = [19,23,23,29,26]
        passed= 0
        for idx,ans in enumerate(answers):
            filename = "day6-test{0}-input.txt".format(idx+1)
            res =getLocation(filename,positions) 
            if res==ans:
                passed += 1
            else:
                print('Wrong: Answer to test {0} Should be {1}, got {2} instead'.format(idx+1,ans, res))
        print('{0} of {1} tests PASSED'.format(passed, len(answers)))
    else:
        filename = "day6-input.txt"
        ans = getLocation(filename, positions)
        print("The character location at which the first {0}-character long starter marker is detected is {1}".format(positions,ans))