a = []

try:
    while True:
        a.append(input())
except:
    b = sorted(a)
    for i in b:
        print(i)
