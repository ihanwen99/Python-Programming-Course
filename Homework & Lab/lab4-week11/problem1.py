from Tkinter import *
from time import sleep


def main():
    r = Tk()
    c = Canvas(r, width=80, height=420, bg='white')
    c.pack()

    c.create_rectangle(0, 410, 79, 419, fill='brown')
    #   c.create_line(0,10,79,10)
    ball = c.create_oval(20, 10, 59, 49, fill='red')

    h0 = 380
    v0 = 0.0
    dt = 0.05

    while True:
        h1 = h0 - v0 * dt
        v1 = v0 + 9.8 * dt

        if h1 < 20:
            h1 = 20
            v1 = -1.0 * v1

        if h1 > 380:
            h1 = 380
            v1 = 0.0

        c.move(ball, 0, h0 - h1)
        c.update()

        h0 = h1
        v0 = v1

        sleep(0.02)


if __name__ == '__main__':
    main()
