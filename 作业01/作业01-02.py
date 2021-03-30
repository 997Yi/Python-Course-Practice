import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8')

num = int(input())

result =0


while not num == 0:
    result += num % 10
    num = num // 10

print(result)

