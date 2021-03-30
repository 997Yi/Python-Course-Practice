def isPrime(x):
    '''
    判断是否为质数
    '''
    if x <= 1:
        return False
    for i in range(2,x//2+1):
        if x % i == 0:
            return False
    return True


x = int(input())
string = ""

y = x
i = 2

while i <= y:
    if x%i == 0 and isPrime(i):
          string += str(i)+' '
          x=x//i
    else:
        i += 1 
print(string[:-1])

