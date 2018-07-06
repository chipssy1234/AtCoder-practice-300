import numpy as np
N = int(input())
A = list(map(int,input().split()))

npA = np.sort(A)

ans = 0
while len(npA) > 0 and N >= npA[0]:
    i = np.min(npA)
    tmp = np.sum(npA == i)
    if tmp > i:
        ans += tmp - i
    elif tmp < i:
        ans += tmp
    npA = np.delete(npA, range(tmp))


print(ans + len(npA))
