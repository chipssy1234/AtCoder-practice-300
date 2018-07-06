N,A = map(int, input().split())
X = list(map(int,input().split()))

max_x = max(X)
Y = []
for x in X:
    Y.append(x - A)

dp=[[0 for t in range(60*60*2)] for j in range(60)]
#dp[j番目までの変数から0枚以上選んでy_iの合計を][t-NXにする] = 総数

#dp[0][N*max_x] = 1
for j in range(N+1):
    for t in range(2*N*max_x+1):
        if j == 0 and t == N*max_x:
            dp[j][t] = 1
        else:
            if j>=1 and (t-Y[j-1] < 0 or t - Y[j-1] > 2*N*max_x):
                dp[j][t] = dp[j-1][t]
            elif j>=1 and 0<= t-Y[j-1] <=2*N*max_x:
                dp[j][t] = dp[j-1][t] + dp[j-1][t-Y[j-1]]
            else:
                dp[j][t] = 0
print(dp[N][N*max_x]-1)



# dp=[[[0 for s in range(60*60)] for k in range(60)] for j in range(60)]
# for s in range(60*60):
#     dp[0][0][s]=0
# #dp[j番目までの変数から][k個選んで][合計がs] = になる総数
# for j in range(N+1):
#     for k in range(N+1):
#         for s in range(N*k+1):
#             if j == 0 and k == 0 and s == 0:
#                 dp[j][k][s] = 1
#             else:
#                 if j >= 1 and s < X[j-1]:
#                     dp[j][k][s] = dp[j-1][k][s]
#                 elif j >= 1 and  k >= 1 and s>=X[j-1]:
#                     dp[j][k][s] = dp[j-1][k][s] + dp[j-1][k-1][s-X[j-1]]
#                 else:
#                     dp[j][k][s] = 0

# print(dp[0][0][6])
# ans = 0
# for k in range(N+1):
#     ans += dp[N][k][k*A]
# print('ans = ',ans)

# import itertools
# N,A = map(int, input().split())
# X = map(int,input().split())

# ans = 0
# X = sorted(X)
# for n in range(1,N+1):
#     tmp = []
#     tmp = list(itertools.combinations(X,n))
#     tmp_sum = []

#     for i in range(len(tmp)):
#         tmp_sum.append(sum(tmp[i]))
#     ans += tmp_sum.count(A*n)
#     if tmp_sum[0] > A*n:
#         break

# print(ans)
