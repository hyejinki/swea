def nCr(n, r, s, A):
    global new_comb
    if r == 0:
        new_comb.append(sorted(comb))

    else:
        for i in range(s, n - r + 1):
            comb[r - 1] = A[i]
            nCr(n, r - 1, i + 1, A)

def f(k):
    new_P[new_comb[i][0]], new_P[new_comb[i][1]] = new_P[new_comb[i][1]], new_P[new_comb[i][0]]


T = int(input())
for test_case in range(1, T + 1):
    p, t = map(str, input().split())
    x = int(p)

    P = list(p)
    N = len(P)
    comb = [0] * 2
    A = [i for i in range(N)]
    new_comb = []
    nCr(N, 2, 0, A)

    print(new_comb)
    maxV = 0
    ans = [[] for _ in range(k + 1)]


    for i in range(len(new_comb)):
        k = int(t)
        new_P = P[:]
        ans = ''
        while k > 0:

            k -= 1
        for x in new_P:
            ans += x
        if int(ans) > maxV:
            maxV = int(ans)
            print(maxV)



    print((maxV))
    # ans = []
    # nCr(N, t, 0, new_comb)
