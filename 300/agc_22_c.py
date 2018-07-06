S = input()
abc = 'abcdefghijklmnopqrstuvwxyz'
non = []

if len(S) < 26:
    for a in abc:
        if not a in S:
            print(S + a)
            break
elif S == 'zyxwvutsrqponmlkjihgfedcba':
    print(-1)
else:
    Zind = S.index('z')
    tmpind = abc.index(S[Zind-1])
    print(S[:Zind-1] + abc[tmpind + 1])
