a = ""
with open('trans.in', 'r') as f1:
    a = f1.readline()
a = list(a)
for i in range(len(a)):
    if not (ord(a[i]) >= 48 and ord(a[i]) <= 57):
        a[i] = " "
a = "".join(a)
l = a.split()

with open('trans.out', 'w') as f1:
    f1.write(str(len(l)))
    f1.write("\n")
    f1.write(" ".join(i for i in l))
    f1.write("\n")
