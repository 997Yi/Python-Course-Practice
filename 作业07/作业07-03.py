a = ""
with open('correct.in', 'r') as f1:
    a = f1.readline()
l = []
result = True
for i in a:
    if i == '(' or i == '[' or i == '{' :
        l.append(i)
    if i == ')':
        if not l:
            result = False
            break
        elif ord(l[-1]) == ord(i)-1:
            l.pop(-1)
        else:
            result = False
            break
    elif i == ']' or i == '}':
        if not l:
            result = False
            break
        elif ord(l[-1]) == ord(i)-2:
            l.pop(-1)
        else:
            result = False
            break
    
with open('correct.out', 'w') as f1:
    if result:
        f1.write('True')
    else:
        f1.write('False')
