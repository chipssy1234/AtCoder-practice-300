import numpy as np
import collections
N,K = map(int,input().split())
A = list(map(int,input().split()))

col = collections.Counter(A)
most = col.most_common()

ans = 0
for i in range(1,len(most) - K+1):
    ans += most[-i][1]

print(ans)
