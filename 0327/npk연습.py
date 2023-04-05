def perm(i, k):
    if i == k:
        print(*p)
    else:
        for j in range(k):
            if used[j] == 0:
                p[i] = arr[j]
                used[j] = 1
                perm(i+ 1, k)
                used[j] = 0


arr = [1, 2, 3]
p = [0] * 3
used = [0] * 3
perm(0, 3)