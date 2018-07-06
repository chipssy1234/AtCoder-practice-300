import numpy as np
N = int(input())
S = input()

numW = [0]*N
numE = [0]*N
tmpW = 0
tmpE = 0
for i,s in enumerate(S):
    if s == 'W':
        tmpW += 1
    else:
        tmpE += 1

    numW[i] = tmpW
    numE[i] = tmpE

npans = np.zeros(N,dtype = int)
npans[0] = numE[-1] - numE[0]
for i in range(1,N):
    npans[i] = numW[i-1] + numE[-1] - numE[i]
print(np.min(npans))


# npans = np.zeros(N,dtype = int)
# for i,s in enumerate(S):
#     if s == 'W':
#         npans[i+1:] += 1
#     else:
#         npans[:i] += 1
# print(np.min(npans))
