n = input("Please input a number : ")

k, a = 0, ord('A')

for i in range(n):
    for j in range(n - i):
        print chr(a + k),
        k = k + 1
        if k == 26: k = 0
    print 
