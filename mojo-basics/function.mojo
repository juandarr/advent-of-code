# This example shows how to create functions, function arguments, default values
fn add(x: Int, y: Int = 80) -> Int:
    return x + y


# Argument mutability and ownership
"""
- borrowed == default definition
- inout = mutable values inside are reflected outside
- owned = creates unique copy of arguments
- ^ = transfer ownership to argument, thus destroys external variable
"""


fn power(owned base: Int, power: Int = 3) -> Int:
    base *= 2
    return base**power


# Structures
struct MyPair:
    var first: Int
    var second: Int

    fn __init__(inout self, first: Int, second: Int):
        self.first = first
        self.second = second

    fn dump(self):
        print(self.first, self.second)


fn main():
    let s: Int = 10
    print("Hello, world!")
    print(add(5))
    print(power(s ^))
    let pair = MyPair(1, 3)
    pair.dump()
