a = input()
b = []
for i in a.lower():
    b.append(i)

b[0] = chr(ord(b[0]) - 32)

for i in range(len(b)-2):   
    if b[i] == ".":
        b[i+2] = chr(ord(b[i+2]) - 32)
    if b[i] == "i" and (b[i-1] == " " or b[i-1] == ",") and (b[i+1] == " " or b[i+1] == ","):
        b[i] = chr(ord(b[i]) - 32)

print("".join(b))
    
