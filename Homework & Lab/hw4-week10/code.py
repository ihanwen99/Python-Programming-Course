def findPrim(n):
    l = []
    for i in range(2, n + 1):
        l.append(i)

    while l:
        if len(l) == 1: break
        print l[0],
        for i in range(l[0], n, l[0]):
            if i in l:
                l.remove(i)


if __name__ == '__main__':
    n = int(raw_input("Please input the upper bound you want to check: "))
    findPrim(n)
