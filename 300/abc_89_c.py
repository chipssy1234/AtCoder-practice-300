import numpy as np
N = int(input())
S = [input()[0] for _ in range(N)]

npS = np.array(S)
march = np.zeros(5,dtype = int)
tmp = 'MARCH'

for i in range(5):
    march[i] = np.sum(npS == tmp[i])

ans = 0
for i in range(3):
    for j in range(i+1,4):
        for k in range(j+1,5):
            tmp = march[i] * march[j] * march[k]
            ans += tmp


print(ans)
