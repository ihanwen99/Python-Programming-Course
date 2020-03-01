# -*- coding: cp936 -*-
from Tkinter import *


def prepare(s):
    for ch in ",.":
        s.replace(ch, " ")
    return s


def drawBar(c, k, t, aHi, aLo, bHi, bLo):
    a = aHi + aLo
    b = bHi + bLo
    n = a + b
    x0 = 20 + (k - 1) * 60
    y0 = 200 - aHi * 200 / n
    x1 = x0 + 20
    y1 = 200
    c.create_rectangle(x0, y0, x1, y1, fill='red')
    y2 = y0 - aLo * 200 / n
    y3 = y0
    c.create_rectangle(x0, y2, x1, y3, fill='green')

    u0 = x1
    v0 = 200 - bHi * 200 / n
    u1 = u0 + 20
    v1 = 200
    c.create_rectangle(u0, v0, u1, v1, fill='red')
    v2 = v0 - bLo * 200 / n
    v3 = v0
    c.create_rectangle(u0, v2, u1, v3, fill='green')

    c.create_text(x0 + 4, 204, text=t[0], anchor=NW)
    c.create_text(u0 + 4, 204, text=t[1], anchor=NW)

    pct1 = unicode("%d%%" % (100 * aLo / a), 'gbk')
    c.create_text(x0 + 4, y2, text=pct1, anchor=NW)
    pct2 = unicode("%d%%" % (100 * bLo / b), 'gbk')
    c.create_text(u0 + 4, v2, text=pct2, anchor=NW)


def main():
    f = open("data.txt", "r")
    dHi, dLo, ndHi, ndLo = 0, 0, 0, 0  # degree vs nodegree
    wHi, wLo, cHi, cLo = 0, 0, 0, 0  # white vs colored
    mHi, mLo, fHi, fLo = 0, 0, 0, 0  # male vs female
    s = f.readline()
    while s != "":
        s = prepare(s)
        w = s.split()
        if "Bac" in w[3] or "Mas" in w[3] or "Doc" in w[3]:
            if ">" in w[14]:
                dHi = dHi + 1
            else:
                dLo = dLo + 1
        else:
            if ">" in w[14]:
                ndHi = ndHi + 1
            else:
                ndLo = ndLo + 1

        if "White" in w[8]:
            if ">" in w[14]:
                wHi = wHi + 1
            else:
                wLo = wLo + 1
        else:
            if ">" in w[14]:
                cHi = cHi + 1
            else:
                cLo = cLo + 1

        if "Male" in w[9]:
            if ">" in w[14]:
                mHi = mHi + 1
            else:
                mLo = mLo + 1
        else:
            if ">" in w[14]:
                fHi = fHi + 1
            else:
                fLo = fLo + 1

        s = f.readline()

    r = Tk()
    c = Canvas(r, width=200, height=260, bg="white")
    c.pack()
    td = [unicode("有\n学\n位", "gbk"), unicode("无\n学\n位", "gbk")]
    ts = [unicode("白\n人", "gbk"), unicode("有\n色\n人", "gbk")]
    tg = [unicode("男\n性", "gbk"), unicode("女\n性", "gbk")]
    drawBar(c, 1, td, dHi, dLo, ndHi, ndLo)
    drawBar(c, 2, ts, wHi, wLo, cHi, cLo)
    drawBar(c, 3, tg, mHi, mLo, fHi, fLo)

    r.mainloop()


main()
