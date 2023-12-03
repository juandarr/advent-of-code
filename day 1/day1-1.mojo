from python import Python


fn read_file(filename: String) raises -> PythonObject:
    let bn = Python.import_module("builtins")
    let myfile = bn.open(filename, "r")
    return myfile.readlines()


fn main() raises:
    let bn = Python.import_module("builtins")
    try:
        var lines = read_file("day1-1-input.txt")
        for line in lines:
            for s in line:
                if s.
    except:
        print("There was an error reading the file")
