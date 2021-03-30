
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8')

N = int(input())
a = []

for i in range(N):
    a.append([0] * N)


x = 0
y = N - 1
num = 1
while num < N * N:
    # 向右
    for i in range(x, y):
        a[x][i] = num
        num += 1

    # 向下
    for i in range(x, y):
        a[i][y] = num
        num += 1
    # 向左
    for i in range(y, x, -1):
        a[y][i] = num
        num += 1
    # 向上
    for i in range(y, x, -1):
        a[i][x] = num
        num += 1
    x += 1
    y -= 1

a[x][y] = N*N

for i in range(N):
    print("".join('{:>5d}'.format(j) for j in a[i]))

