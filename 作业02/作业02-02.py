import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8')

import numpy as np

tmp = []
# 符号
symbol = ''
# 将输入的数据存入临时数组
while True:
    str = input()
    if (str == ''):
        break
    elif str in  ('+', '-', '*'):
        symbol = str
    else:
        tmp.append([int(i) for i in str.split()])
        if 2 * len(tmp[0]) == len(tmp):
            break

# 矩阵的行数
N = len(tmp) // 2

a = np.mat(tmp[0:N])
b = np.mat(tmp[N:])

# 判断符号并进行运算
if symbol == '+':
    result = (a + b).tolist()
elif symbol == '-':
    result = (a - b).tolist()
elif symbol == '*':
    result = (a * b).tolist()

# 格式化输出
for i in range(N):
    print("".join('{:>5d}'.format(j) for j in result[i]))


