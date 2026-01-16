num = int(raw_input())
mat = []

for i in range(num):
    line = raw_input()
    line = line.split()
    for j in range(num):
        line[j] = int(line[j])
    mat.append(line)

def matmal(mat1, mat2):
    m = []
    for i in range(num):
        line = []
        for j in range(num):
            n = 0
            for k in range(num):
                n += mat1[i][k] * mat2[k][j]
            line.append(n)
        m.append(line)
    return m

def add(sum, m):
    for i in range(num):
        for j in range(num):
            if m[i][j] > 0:
                sum[i][j] = 1

m = mat
sum = []
for i in range(num):
    line = []
    for j in range(num):
        line.append(0)
    sum.append(line)
    sum[i][i] = 1
add(sum, mat)
for i in range(num - 1):
    m = matmal(m, mat)
    add(sum, m)

yes1 = True
yes2 = True
for i in range(num):
    y1 =  True
    y2 = True
    for j in range(num):
        if sum[i][j] == 0 or sum[j][i] == 0:
            y1 = False
        if sum[i][j] == 0 and sum[j][i] == 0:
            y2 = False
    if not y1:
        yes1 = False
    if not y2:
        yes2 = False
if yes1:
    print "A"
elif yes2:
    print "B"
else:
    print "C"

"""debug日志
1.矩阵乘法下表写反了
2.要求k次幂只需进行k-1次矩阵乘法
3.最后可达矩阵应该是把邻接矩阵各个幂相加
4.规定自身到自身可达，要把可达矩阵的对角线元素人为改成1
"""