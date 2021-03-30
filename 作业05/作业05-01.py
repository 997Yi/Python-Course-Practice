def expand(s1, s2):
    '''
    用以将字符串s1中的缩记符号在字符串s2中扩展为等价的完整字符
    '''
    
    for i in range(len(s1)-2):
        if s1[i] == ' ':
            s2 += s1[i]
        elif s1[i] == '-':
            continue
        else:
            if not s1[i+1] == '-':
                s2 += s1[i]
            else:
                if s1[i] >= s1[i+2]:
                    s2 += s1[i] + s1[i+1]
                else:
                    for j in range(ord(s1[i]), ord(s1[i+2])):
                        s2 += chr(j)
    if not s1[-2] == '-':
        s2 += s1[-2]
    s2 += s1[-1]
    return s2

s1 = input()
s2 = ""
s2 = expand(s1, s2)
print(s2)
