# -*- coding: cp936 -*-

# 输入自然数n，输出如下形式的n阶方阵（以n=4为例）：
# 1   2   3   4
# 12  0   0   5
# 11  0   0   6
# 10  9   8   7

# 变通思维版本：逐行填充

n = input("输入自然数n：")

# 建立一个全0的n阶方阵
mat = []
for i in range(n):
    mat = mat + [n*[0]]

# 第一行mat[0]的各元素
for i in range(n):
    mat[0][i] = i+1

# 以下各行mat[j]的首尾元素值
for j in range(1,n):
    if j == 1:
        mat[j][0] = 4*(n-1)           # 第二行首元素是4(n-1)
    else:
        mat[j][0] = mat[j-1][0] - 1   # 其他各行首元素是上一行首元素-1
    mat[j][n-1] = mat[j-1][n-1] + 1   # 各行尾元素是上一行尾元素+1

# 最后一行非首尾元素
for k in range(1,n-1):
    mat[n-1][k] = mat[n-1][k-1] - 1

# 显示
for i in range(n):
    for j in range(n):
        print "%4d" % mat[i][j],
    print


