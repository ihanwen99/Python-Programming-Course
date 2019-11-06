# -*- coding: cp936 -*-

# 输入自然数n，输出如下形式的n阶方阵（以n=4为例）：
# 1   2   3   4
# 12  0   0   5
# 11  0   0   6
# 10  9   8   7

# 直线思维版本：按题意沿顺时针方向填充

n = input("输入自然数n：")

# 建立一个全0的n阶方阵mat
mat = []
for i in range(n):
    mat = mat + [n*[0]]

# 向mat的合适位置填入自然数
for k in range(4*n-4):                # 总共4n-4个元素
    if k < n:                         # mat顶行自左向右
        i = 0                         # i:行号,j:列号
        j = k
    elif k >= n and k < 2*n-1:        # mat最右列自上向下
        i = k-(n-1)
        j = n-1
    elif k >= 2*n-1 and k < 3*n-2:    # mat底行自右向左
        i = n-1
        j = (3*n-3)-k
    else:                             # mat最左列自下向上
        i = (4*n-4)-k
        j = 0
    mat[i][j] = k+1                   # 填入自然数k+1
        
# 显示
for i in range(n):
    for j in range(n):
        print "%4d" % mat[i][j],
    print
