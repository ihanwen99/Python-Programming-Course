def reportOddNumber():
    l = []
    m = input()
    n = input()
    for i in range(m + 1, n):
        if i % 2 == 1:
            l.append(i)
    print(sum(l))


if __name__ == '__main__':
    for i in range(20):
        reportOddNumber()
