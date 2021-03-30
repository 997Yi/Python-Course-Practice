'''
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8')
'''

# 记录行列的列表
row_col = list((map(int, input().split(" "))))
row = row_col[0]
col = row_col[1]

# 输入二维数组
a = []
for i in range(row):
    a.append(list(map(int, input().split(" "))))

def isMin(x, y):
    for i in range(row):
        if a[x][y] > a[i][y]:
            return False
    for j in range(col):
        if a[x][y] > a[x][j]:
            return False
    return True
    
for i in range(row):
    for j in range(col):
        if isMin(i,j):
            print(a[i][j], i+1, j+1)

            

