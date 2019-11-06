from math import *


def getZeroBit(n):
    return n % 10


def getTenBit(n):
    return (n / 10) % 10


def getHundredBit(n):
    return n / 100


def twoEqual(n):
    return getZeroBit(n) == getTenBit(n) or getZeroBit(n) == getHundredBit(n) or getTenBit(n) == getHundredBit(n)


def isSquare(n):
    a = int(sqrt(n))
    return a * a == n


def main():
    n = input("Please input a 3-bit number: ")
    l = []
    for i in range(100, n + 1):
        if isSquare(i) and twoEqual(i):
            l.append(i)

    print("There is {} numbers from 100 to {} suits the conditions.".format(len(l), n))
    for i in l:
        print i,


if __name__ == '__main__':
    main()
