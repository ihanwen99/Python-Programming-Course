def star(n):
    print n * "*"
    print n * "*"


def dollar(n):
    print "%s%s%s" % (4 * "$", (n - 8) * " ", 4 * "$")
    print "%s%s%s" % (4 * "$", (n - 8) * " ", 4 * "$")


def main():
    s = raw_input("Please enter a String you want to show on screen: ")
    n = len(s) + 10
    star(n)
    dollar(n)
    print("%s%s%s" % (4 * "=" + " ", s, " " + 4 * "="))
    dollar(n)
    star(n)


if __name__ == '__main__':
    main()
