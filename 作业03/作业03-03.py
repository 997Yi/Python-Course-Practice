inpu = []

while True:
    inpu.append(int(input()))
    if inpu[-1] == 0:
        break
    
n = inpu[0]
result = 0
bag = []
bag.append(inpu[1])
for i in range(2, len(inpu) - 1):
    if inpu[i] > bag[-1]:
        bag[-1] = inpu[i]
    elif len(bag) < n:
        bag.append(inpu[i])

print(sum(bag))
