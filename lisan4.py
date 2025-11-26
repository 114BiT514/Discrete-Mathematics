dic = {
 'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18,
 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25
}

def sum(a, b):
    if a == 1 or b == 1:
        return 1
    return 0

def mul(a, b):
    if a == 1 and b == 1:
        return 1
    return 0

class Relation:
    def __init__(self, num, set):
        self.mat = []
        self.num = num
        self.set = set
        for i in range(num):
            line = []
            for j in range(num):
                line.append(0)
            self.mat.append(line)

    def add(self, str):
        m = dic[str[1]]
        n = dic[str[3]]
        self.mat[m][n] = 1

    def t(self):
        self.t_mat = self.mat[:]
        for k in range(1, self.num + 1):
            for i in range(self.num):
                for j in range(self.num):
                    self.t_mat[i][j] = sum(self.t_mat[i][j], mul(self.t_mat[i][k - 1], self.t_mat[k - 1][j]))

    def find_min(self):
        self.min = []
        for c in self.set:
            n = dic[c]
            yes = True
            for i in range(self.num):
                if self.t_mat[i][n] == 1:
                    yes = False
                    break
            if yes:
                self.min.append(c)

    def find_max(self):
        self.max = []
        for c in self.set:
            n = dic[c]
            yes = True
            for i in range(self.num):
                if self.t_mat[n][i] == 1:
                    yes = False
                    break
            if yes:
                self.max.append(c)

set = raw_input()
set = set.split(",")
num = len(set)
relation = Relation(num, set)
rela = raw_input()
rel = []
i = 0
while i < len(rela):
    rel.append(rela[i:i + 5])
    i += 6
for r in rel:
    relation.add(r)
relation.t()
relation.find_min()
relation.find_max()
min = ",".join(relation.min)
max = ",".join(relation.max)
print min
print max

"""debug日志
    add的索引写错了，两个字母应该是在1和3
    python3取字典的键返回的不是列表，无法切片，要先转成列表
    python2和python3的input函数不一样，忘记改了
    python2列表没有copy()，得用切片
    python2的字典居然是无序的，逆天
    
"""

