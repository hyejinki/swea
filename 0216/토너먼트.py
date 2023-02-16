def win(i, j):
    global s
    a, b = s[i], s[j]
    if (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
        return j
    return i


def f(arr, i, j):
    if i == j:
        return i
    mid = (i + j) // 2
    r1 = f(arr, i, mid)
    r2 = f(arr, mid+1, j)
    return win(r1, r2)

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    s = list(map(int, input().split()))
    print(f(s, 0, N-1)+1)