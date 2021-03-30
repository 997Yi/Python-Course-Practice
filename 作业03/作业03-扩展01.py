result = []
for i in range(8):
    result.append([0,0])  
  

inpu = input()
j = 0
index = 0
for i in inpu:
    result[j][0] = j + 1
    if i == '*':
        index = j
    else:
        result[j][1] = int(i)
    j += 1


a = [1, 2, 3, 4, 5, 6, 7, 8]
for i in inpu:
    if i == '*':
        pass
    else:
        a.remove(int(i))

result[index][1] = a[0]
def queen():
    j = 0
    for i in range(8):
        if i == index:
            continue
        elif result[i][0] - result[index][0] == result[i][1] - result[index][1]:
            return False
    return True        
            
if queen():
    print(result[index][1])
else:
    print("No Answer")
