from operator import itemgetter

n = int(input())
a = []

for i in range(n):
    a.append(input().split())

x = sorted(a, key=lambda x: x[1])
y = sorted(a, key=itemgetter(2,1))

for i in range(n):
    print("{:>3d}{:>6s}{:>3d}".format(int(x[i][0]), x[i][1], int(x[i][2])))
        
print()
for i in range(n):
    print("{:>3d}{:>6s}{:>3d}".format(int(y[i][0]), y[i][1], int(y[i][2])))
