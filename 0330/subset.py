def f(i, k, s, key, rs):
    global cnt
    global c
    c += 1

    if s == key:
        cnt += 1
    elif i == k or s > key:
        return

    # if i == k:
    #     if s == key:
    #         cnt += 1

    else:
        bit[i] = 0
        f(i+1, k, s, key, rs - A[i])
        bit[i] = 1
        f(i+1, k, s+A[i], key, rs - A[i])
        return

A = [i for i in range(1, 11)]
N = 10
bit = [0]*N
key = 10
cnt = 0
c = 0
f(0, N, 0, key, sum(A))
print(cnt, c)
