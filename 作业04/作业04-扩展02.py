a = []
try:
    while True:
        a.append(input())
except:
    result = r""
    for i in a:
        for j in i:
            if j == "\t":
                result += r"\t"
            else:
                result += j
        result += r"\n"
    print(result)
            
    
