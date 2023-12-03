
def read_file(filename):
    return open(filename, "r")

if __name__=='__main__': 
    lines = read_file("day1-1-input.txt")
    #linesTest = ['two1nine','eightwothree','abcone2threexyz', 'xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen']
    digits = '123456789'
    digitsWords = {'one':'1','two':'2', 'three':'3','four':'4','five':'5', 'six':'6','seven':'7','eight':'8', 'nine':'9'}
    for dw in digitsWords:
        print(dw[::-1])
    net = 0
    c = 0
    for line in lines:
        start = [float("inf"), None]
        for d in digits:
            tmp = line.find(d) 
            if tmp>=0 and tmp < start[0]:
                start = [tmp, d]
        for dw in digitsWords:
            tmp = line.find(dw) 
            if tmp>=0 and tmp < start[0]:
                start = [tmp, digitsWords[dw]]
        end = [float("inf"), None]
        lineReversed = line[::-1]
        for d in digits:
            tmp = lineReversed.find(d) 
            if tmp>=0 and tmp < end[0]:
                end = [tmp, d]
        for dw in digitsWords:
            tmp = lineReversed.find(dw[::-1]) 
            if tmp>=0 and tmp+len(dw)-1 < end[0]:
                end = [tmp+len(dw)-1, digitsWords[dw]]
        val = int('{0}{1}'.format(start[1], end[1]))
        net  += val 
    print(net)