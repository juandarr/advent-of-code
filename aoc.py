import sys
from subprocess import Popen

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) > 2:
        print(
            'This script requires two arguments: the year (y in format YYYY),  day (d) and challenge (c) in format "y.d.c" and whether to call "test" or "main" input files'
        )
    else:
        tmp = args[0].split(".")
        if len(tmp) != 3:
            print(
                'This script requires format: "y.d.c", where y is the year, d is the day and c the challenge'
            )
        else:
            year = tmp[0]
            day = int(tmp[1])
            challenge = int(tmp[2])
            proc = Popen(
                [
                    sys.executable,
                    "{0}/day{1}/day{1}-{2}.py".format(year, day, challenge),
                    args[1],
                ]
            )
            return_value = (
                proc.wait()
            )  # this call blocks until the program has been finished
