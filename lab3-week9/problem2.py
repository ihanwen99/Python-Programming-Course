from Tkinter import *


def getInput():
    a = input("Please input principal: ")
    i = input("Please input interest: ")
    n = input("Please input year: ")
    return a, i, n


def calculation(a, i, n):
    l = []
    for y in range(n):
        l.append(a * (1 + i) ** y)
    return l


def drawBar(tk, year, money, limit):
    x1 = 20 + year * 50
    y1 = 430 - money * 400 / limit
    x2 = x1 + 30
    y2 = 430
    tk.create_rectangle(x1, y1, x2, y2, fill='green')
    m = "%-0.2f" % money
    tk.create_text(x1, y1 - 20, text=m, anchor=NW)


def initCanvas(n):
    tk = Tk()
    w1 = (n + 1) * (20 + 30)
    w = 10 + w1 + 10
    h = 10 + 20 + 400 + 10
    c = Canvas(tk, width=w, height=h, bg='white')
    c.pack()
    c.create_line(10, 10, w1 + 10, 10)
    c.create_line(10, 430, w1 + 10, 430)
    return tk, c


def main():
    a, i, n = getInput()
    # a, i, n = 1000, 0.2, 15
    limit = a * (1 + i) ** n
    l = calculation(a, i, n)
    tk, c = initCanvas(n)
    for k, v in enumerate(l):
        print(k, v)
        drawBar(c, k, v, limit)

    tk.mainloop()


if __name__ == '__main__':
    main()
