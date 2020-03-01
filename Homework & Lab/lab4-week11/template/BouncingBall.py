# -*- coding: cp936 -*-

# 动画:皮球从高处落地弹起.
# 假设速度矢量向下为正,向上为负
# 球的新高度 = 球的旧高度 - 球速* 时间间隔
# 球的新速度 = 球的旧速度 + 9.8 * 时间间隔
# 落地反弹:if 高度 < 皮球半径:                                    
#            速度取反

from Tkinter import *
from time import sleep

def main():
    r = Tk()
    c = Canvas(r,width=80,height=420,bg='white')
    c.pack()

    c.create_rectangle(0,410,79,419,fill='brown')   # 地面
#   c.create_line(0,10,79,10)                       # 下落起点
    ball = c.create_oval(20,10,59,49,fill='red')

    h0 = 380                      # 初始高度 = 410 - 10 - 20
    v0 = 0.0                      # 初始速度
    dt = 0.05                     # 时间离散化的间隔，越小运动越精确但计算量越大

    while True:
        h1 = h0 - v0 * dt         # dt后的新高度
        v1 = v0 + 9.8 * dt        # dt后的新速度

        if h1 < 20:               # 球的高度小于其半径
            h1 = 20               # 则触地
            v1 = -1.0 * v1        # 速度变向

        if h1 > 380:              # 球的高度大于初始高度
            h1 = 380              # 则触顶
            v1 = 0.0              # 速度也恢复为初始值0

        c.move(ball,0,h0-h1)      # 运动到新高度
        c.update()                # 刷新画面
        
        h0 = h1
        v0 = v1

        sleep(0.02)

main()
