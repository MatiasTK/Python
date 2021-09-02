m1 = [[1,2,3],[4,5,6]]
m2 = [[-1,0],[0,1],[1,1]]

res = [[0,0],[0,0]]

f = 0
c = 0

for i in range(len(m1)):
    for j in range(len(m2[0])):
        for k in range(len(m2)):
            res[i][j] += m1[i][k] * m2[k][j]

for z in res:
    print(res)