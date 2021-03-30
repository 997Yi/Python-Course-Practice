result = []

inp = list(map(int, input().split(" ")))
M = inp[0]
N = inp[1]

def conversion(M, N):
    while not M == 0:
        tmp = M % N
        result.insert(0, tmp if tmp<10 else chr(65+(tmp%10)))
        M = M // N
        
conversion(M, N)
print("".join(str(i) for i in result))
