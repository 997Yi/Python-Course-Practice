a = ""
with open('in.txt', 'r') as f1:
    a = f1.readlines()
    a = "".join(a)
a = list(a)
for i in range(len(a)):
    if not (ord(a[i]) >= 65 and ord(a[i]) <= 90):
        if not (ord(a[i]) >= 97 and ord(a[i]) <= 122):
            a[i] = " "
a = "".join(a)
l = a.split()

print(len(l), len(a))
