import itertools
class Matrix:
    def __init__(self):
        '''
        建立一个4x4的零矩阵
        '''
        self.n = 4
        self.content = []
        for i in range(self.n):
            self.content.append([0] * self.n)
        pass

    def get_pos(self, x, y):
        '''
        获取矩阵第x行第y列的元素，作为返回值
        '''
        return self.content[x-1][y-1]
        pass

    def set_pos(self, x, y, value):
        '''
        将矩阵第x行第y列的元素值改为value
        '''
        self.content[x-1][y-1] = value
        pass

    def initialize(self, matlist):
        '''
        matlist，为一个列表，保证该列表包含四个子列表，每个子列表包含四个整型数值
        '''
        for i in range(self.n):
            for j in range(self.n):
                self.set_pos(i+1, j+1, matlist[i][j])
        pass

    def output(self):
        '''
        将矩阵以某种格式输出至标准输出流（屏幕）
        '''
        for i in range(self.n):
            s = "|"
            for j in range(self.n):
                s += "{:>5d}".format(self.get_pos(i+1, j+1))
            s += "    |"
            print(s)
        pass

    def trans(self):
        '''
        计算矩阵的转置矩阵，作为返回值
        '''
        m = Matrix()
        for i in range(self.n):
            for j in range(self.n):
                m.set_pos(i+1, j+1, self.get_pos(j+1, i+1))
        return m
        pass

    def plus(self, m2):
        '''
        计算本矩阵与m2矩阵的和，作为返回值
        '''
        m = Matrix()
        for i in range(self.n):
            for j in range(self.n):
                m.set_pos(i+1, j+1, m2.get_pos(i+1,j+1) + self.get_pos(i+1,j+1))
        return m
        pass

    def multiply(self, m2):
        '''
        计算本矩阵与m2矩阵的乘积，作为返回值
        '''
        m = Matrix()
        for i in range(self.n):
            for j in range(self.n):
                a, b = [], []
                for x in range(self.n):
                    a.append(self.get_pos(i+1, x+1))
                for x in range(self.n):
                    b.append(m2.get_pos(x+1, j+1))
                value = sum(list(itertools.starmap(lambda x,y:x*y , zip(a,b))))
                m.set_pos(i+1, j+1, value)
        return m
        pass
        
m1 = Matrix()
m2 = Matrix()

print("x before initialization:")
m1.output()


a, b = [], []
for i in range(4):
    a.append(list(map(int, input().split())))
for i in range(4):
    b.append(list(map(int, input().split())))

print("x after initialization:")
m1.initialize(a)
m1.output()
print("y after initialization:")
m2.initialize(b)
m2.output()
print("Transpose x is:")
m1.trans().output()
print("Transpose y is:")
m2.trans().output()
print("Transpose x+y is:")
m1.plus(m2).trans().output()
print("x*y is:")
m1.multiply(m2).output()


