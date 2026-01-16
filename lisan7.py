num = int(raw_input())
mat = []

for i in range(num):
    line = raw_input()
    line = line.split()
    for j in range(num):
        line[j] = int(line[j])
    mat.append(line)

node = []
for i in range(num):
    node.append(-1)

yes = True

def dfs(n,id):
    global yes
    if not yes :
        return
    if node[n] != -1:
        return
    node[n] = id
    if mat[n][n] != 0:
        yes = False
        return
    if id == 0:
        for i in range(num):
            if mat[n][i] != 0:
                y = True
                for j in range(num):
                    if mat[i][j] != 0 and node[j] == 1:
                        y = False
                if y:
                    dfs(i,1)
                else:
                    yes = False
    else:
        for i in range(num):
            if mat[n][i] != 0:
                y = True
                for j in range(num):
                    if mat[i][j] != 0 and node[j] == 0:
                        y = False
                if y:
                    dfs(i,0)
                else:
                    yes = False

for i in range(num):
    dfs(i,0)

if yes:
    print "yes"
else:
    print "no"


"""debug日志
  1.本来用的是bfs，但是发现这样做对于不连通的图不好处理
  2.bool类型的变量yes在函数中不能正确修改，需要加上global声明
  3.要及时给node[n]赋值，否则可能出现死循环
"""