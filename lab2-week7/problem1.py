n = input("Please input a number: ")
mat = []
for i in range(n):
    mat.append([0] * n)
for i in range(n):
    mat[0][i] = i + 1
for i in range(1, n):
    mat[i][n - 1] = mat[i - 1][n - 1] + 1
    if i == 1:
        mat[1][0] = 4 * (n - 1)
    else:
        mat[i][0] = mat[i - 1][0] - 1


for i in range(1, n - 1):
    mat[n - 1][i] = mat[n - 1][i - 1] - 1

for i in range(n):
    for j in range(n):
        print'%4d' % mat[i][j],
    print
