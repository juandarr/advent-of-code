from utils.static_tuple import StaticTuple
from builtin.string import atol


fn read_file(filename: String) raises -> String:
    let myfile = open(filename, "r")
    return myfile.read()


fn main() raises:
    try:
        let lines = read_file("day1-1-input.txt")
        var c: Int = 0
        var l: Int = 1
        let digits: StaticTuple[9, StringLiteral] = StaticTuple[
            9, StringLiteral
        ].__init__("1", "2", "3", "4", "5", "6", "7", "8", "9")
        var net: Int = 0
        var start: String = "-1"
        var end: String = "-1"
        while c < lines.__len__():
            if lines[c] != "\n":
                var d: Int = 0
                while d < digits.__len__():
                    if lines[c] == digits.__getitem__(d):
                        if start == "-1":
                            start = lines[c]
                        end = lines[c]
                    d += 1
            else:
                net += atol(start) * 10 + atol(end)
                l += 1
                start = "-1"
                end = "-1"
            c += 1
        net += atol(start) * 10 + atol(end)
        print("This is the end result: ", net)
    except:
        print("There was an error reading the file")
