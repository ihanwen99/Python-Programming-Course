# Author: David Stark
# Version: 1.0


def calculate():
    function = raw_input()
    a = input()
    b = input()

    if function == "A":
        print(a + b)
    elif function == "S":
        print(a - b)
    elif function == "M":
        print(a * b)
    elif function == "D":
        print(float(a / b))


if __name__ == '__main__':
    calculate()
