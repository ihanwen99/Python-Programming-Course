# -*- coding: cp936 -*-

# 输入x,输出函数
#    f(x) = (sin(x)^2+cos(x)+1)^3 - 3(sin(x)^2+cos(x)), x>0
#           4sin(x)^2+4cos(x)-1                         x<0
#           pi                                          x=0
# 的值.

from math import sin,cos,pi

x = input("请输入x: ")

t = sin(x)**2 + cos(x)    # 这一步使下面的语句简洁!
if x > 0:
    y = (t+1)**3 - 3*t
elif x < 0:
    y = 4*t - 1
else:
    y = pi
    
print "函数值f("+str(x)+") =",y
