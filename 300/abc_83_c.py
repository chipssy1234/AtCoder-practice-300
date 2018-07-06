X,Y = map(int,input().split())
tmp = X
ans = 0
while tmp <= Y:
    tmp *= 2
    ans += 1

print(ans)
