'''
aList = [['a', 0], ['b', 0], ['c', 0], ['d', 0], ['e', 0], ['f', 0],
         ['g', 0], ['h', 0], ['i', 0], ['j', 0], ['k', 0], ['l', 0],
         ['m', 0], ['n', 0], ['o', 0], ['p', 0], ['q', 0], ['r', 0],
         ['s', 0], ['t', 0], ['u', 0], ['v', 0], ['w', 0], ['x', 0],
         ['y', 0], ['z', 0]]
'''

aList = [[chr(97+i), 0] for i in range(26)]

inpu = ""
try:
    while True:
        inpu += input()
except:
    for i in inpu:
        tmp = ord(i)
        if tmp >= 97 and tmp <= 122:
            aList[tmp-97][1] += 1
        else:
            continue

    max = 0
    for i in aList:
        if i[1] > max:
            max = i[1]

    for i in range(max):
        a = ""
        for j in aList:
            if max - j[1] - i <= 0:
                a += "*"
            else:
                a += " "
        print(a)

    print("".join(str(i[0]) for i in aList))
