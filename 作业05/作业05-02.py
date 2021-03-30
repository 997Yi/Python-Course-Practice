def insert(string, c):
    string += c
    return "".join(i for i in sorted(string))

string = input()
c = input()
print(insert(string, c))
