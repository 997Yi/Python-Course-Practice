def gcd(x, y):
    if y<=x and x % y == 0:
        return y
    elif y > x:
        return gcd(y, x)
    else:
        return gcd(y, x % y)

a = list(map(int, input().split()))
print(gcd(int(a[0]), int(a[1])))
