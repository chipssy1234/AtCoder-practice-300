N,K = map(int, input().split())
D = input().split()

for ans in range(N,N*10+1):
    ch_n = str(ans)
    cnt = 0
    for c in ch_n:
        cnt += 1
        if c in D:
            break
        if cnt == len(ch_n):
            print(ans)
            exit()

# https://www.pythonweb.jp/tutorial/list/index10.html
# オブジェクト in リストオブジェクト
# オブジェクト not in リストオブジェクト
# True or False
