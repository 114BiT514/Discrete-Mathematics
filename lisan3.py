def sum(a, b):
    if a == 1 or b == 1:
        return 1
    return 0

def mul(a, b):
    if a == 1 and b == 1:
        return 1
    return 0

mat = []
line = raw_input()
num = int((len(line) + 1)/2)
line = line.split(" ")
mat.append(line)
for i in range(num):
    line[i] = int(line[i])
for i in range(num - 1):
    line = raw_input()
    line = line.split(" ")
    for i in range(num):
        line[i] = int(line[i])
    mat.append(line)
for k in range(1,num + 1):
    for i in range(num):
        for j in range(num):
            mat[i][j] = sum(mat[i][j], mul(mat[i][k - 1], mat[k - 1][j]))
for i in range(num):
    for j in range(num - 1):
        print mat[i][j],
    print mat[i][num - 1]

"""debug日志
1.print格式不对，直接打印列表会有[]和，
"""
