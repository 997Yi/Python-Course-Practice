import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8')

a = []
while True:
    tmp = input()
    if tmp == "":
        break
    else:
        a.append(int(tmp))

b = sorted(a, reverse=True)
# 最大
print(b[0])
# 最小
print(b[-1])
# 中位数
print(a[(len(a) - 1)//2])
# 降序输出
print(" ".join(str(i) for i in b))
