# -*- coding: cp936 -*-

# 输入正整数n，输出n行由大写字母（从A-Z循环使用）组成的三角形阵列。
# 例如：输入3，输出
# A B C 
# D E
# F
# 又如：输入7，输出
# A B C D E F G
# H I J K L M
# N O P Q R
# S T U V
# W X Y
# Z A
# B

n = input("请输入一个自然数：")
a = ord('A')                        # 首个被打印字母
k = 0                               # k表示当前打印的字母与A的距离(编码差)
for i in range(1,n+1):              # i取值1~n表示行号
    for j in range(n-i+1):          # j是第i行上的循环控制变量:0 ~ n-i
        print chr(a+k),             # 打印当前字母
        k = k + 1                   # 下次打印的字母
        if k == 26:                 # 如果刚才打印的是Z
            k = 0                   # 那么下次回到A
    print

