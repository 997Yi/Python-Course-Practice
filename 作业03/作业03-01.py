chess = []

for i in range(19):
    chess.append(list(map(int, input().split(" "))))

def playChess():
    for i in range(19):
        for j in range(19):
            if chess[i][j] == 0:
                continue
            elif chess[i][j] == 1:
                if isWin(1, i, j) == True:
                    print("1:%d,%d"%(i+1, j+1))
                    return
            elif chess[i][j] == 2:
                if isWin(2, i, j) == True:
                    print("2:%d,%d"%(i+1, j+1))
                    return
    return False

def isWin(x, i, j):
    
    if j <= 14:
        # 判断右边
        for n in range(1,5):
            if not chess[i][j + n] == x:
                break
            if n == 4:
                return True
        # 判断右下
        if i <= 14:
            for n in range(1,5):
                if not chess[i + n][j + n] == x:
                    break
                if n == 4:
                    return True
    
    if i <= 14:
        # 判断下边
        for n in range(1,5):
            if not chess[i + n][j] == x:
                break
            if n == 4:
                return True
        # 判断左下
        if j >= 4:
            for n in range(1,5):
                if not chess[i + n][j - n] == x:
                    break
                if n == 4:
                    return True
      
    pass

if playChess() == False:
    print("No")

    
