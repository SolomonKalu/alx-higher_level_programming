#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    alpha = dir()
    for x in range(0, len(alpha)):
        if alpha[x][0:2] != "__":
            print("{}".format(alpha[x]))
