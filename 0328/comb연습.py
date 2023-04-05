def nCr(n, r, s):
    if r == 0:
        new_comb = sorted(comb)
        print(new_comb)
    else:
        for i in range(s, n -r+1):
            comb[r-1] = A[i]
            nCr(n, r- 1, i + 1)


A = [1, 2 , 3, 4, 5]
n = 5
r = 3
comb = [0] * r
nCr(n, r, 0)