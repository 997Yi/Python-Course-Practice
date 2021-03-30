
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8')

# 获取输入
a_len = int(input())
a = list(map(int, input().split(" ")))
a.sort()
b_len = int(input())
b = list(map(int, input().split(" ")))
b.sort()

# 两个数据集是否相同
same = 1

if not a_len == b_len:
    same = 0
else:
    for i in range(a_len):
        if not a[i] == b[i]:
            same = 0

print(same)           

i = 0
j = 1
while i < a_len:
    if j == a_len or not a[i] == a[j]:
        print(a[i], j-i)
        i = j
    j += 1
