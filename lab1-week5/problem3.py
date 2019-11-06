# -*- coding: UTF-8 -*-

apple = 3.0
pear = 2.5
orange = 4.1
grape = 10.2

times = 4
while times > 0:
    print "[1] 苹果"
    print "[2] 梨"
    print "[3] 橘子"
    print "[4] 葡萄"
    print "[0] 退出"

    ord = input("请输入序号：")
    if ord==0:
        break
    else:
        if ord==1:
            print "苹果单价为%0.2f元/千克\n" % apple
        elif ord == 2:
            print "梨单价为%0.2f元/千克\n" % pear
        elif ord == 3:
            print "橘子单价为%0.2f元/千克\n" % orange
        elif ord == 4:
            print "葡萄单价为%0.2f元/千克\n" % grape
    times-=1
print "Bye!"