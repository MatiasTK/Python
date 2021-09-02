v1 = [1,2,3]
v2 = [-1,0,2]

pe = 0

for i in range(len(v1)):
    pe += v1[i] * v2[i]

print(pe)
