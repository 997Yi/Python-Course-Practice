from operator import itemgetter

n = int(input())
a = []

for i in range(n):
    a.append(input().split())

x = sorted(a, key=lambda x: x[1],reverse=True)

for i in range(n):
    print("{:>15s}{:>5d}".format(x[i][0], int(x[i][1])))
        
