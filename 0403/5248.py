def findset(i):
    while i != rep[i]:
        i = rep[i]

    return i

def union(x, y):
    rep[findset(y)] = findset(x)


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    rep = [i for i in range(N + 1)]
    arr = list(map(int, input().split()))
    for i in range(0, len(arr), 2):
        union(arr[i], arr[i + 1])

    cnt = 0
    for i in range(1, N + 1):
        if i == rep[i]:
            cnt += 1
    print(f'#{test_case}', cnt)



