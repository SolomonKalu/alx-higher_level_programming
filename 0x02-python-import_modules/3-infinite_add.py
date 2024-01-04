#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    r = 0
    for x in range(1, len(sys.argv)):
        r += int(sys.argv[x])
    print("{}".format(r))
