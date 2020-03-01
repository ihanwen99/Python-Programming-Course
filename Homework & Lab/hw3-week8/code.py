from Tkinter import *

root = Tk()

c = Canvas(root, width=350, height=200, bg='white')

c.create_rectangle(68, 160, 52, 200, fill='brown')
points1 = [60, 120, 15, 160, 105, 160]
points2 = [60, 108, 25, 135, 95, 135]
c.create_polygon(points1, fill='green')
c.create_polygon(points2, fill='gray')

c.create_rectangle(160, 160, 180, 200, fill='brown')
points3 = [170, 120, 120, 160, 220, 160]
points4 = [170, 108, 132, 135, 208, 135]
points5 = [170, 100, 155, 122, 185, 122]
c.create_polygon(points3, fill='green')
c.create_polygon(points4, fill='green')
c.create_polygon(points5, fill='gray')

x0, y0, r0 = 280, 185, 15
c.create_oval(x0 - r0, y0 - r0, x0 + r0, y0 + r0)
x1, y1, r1 = 280, 161, 9
c.create_oval(x1 - r1, y1 - r1, x1 + r1, y1 + r1)
x2, y2, r2 = 280, 141, 11
c.create_oval(x2 - r2, y2 - r2, x2 + r2, y2 + r2)

x3, y3, r3 = 275, 141, 2
x4, y4, r4 = 285, 141, 2
x5, y5, x6, y6 = 276, 145, 284, 148
c.create_oval(x3 - r3, y3 - r3, x3 + r3, y3 + r3, fill='blue')
c.create_oval(x4 - r4, y4 - r4, x4 + r4, y4 + r4, fill='blue')
c.create_oval(x5, y5, x6, y6, fill='red')

x6, y6, x7, y7 = 271, 161, 259, 131
c.create_line(x6, y6, x7, y7)
x8, y8, x9, y9 = 289, 161, 301, 131
c.create_line(x8, y8, x9, y9)

x5, y5, r5 = 280, 70, 25
c.create_oval(x5 - r5, y5 - r5, x5 + r5, y5 + r5, fill='red')

c.pack()

# using Pycharm you need the following code
root.mainloop()
