def f(N):
    visited = [0] * (100)
    stack = [0] * N
    top = -1
    v = 0
    while True:
        if v == 99:
            return 1
        visited[v] = 1
        for w in adjL[v]:                  # 갈 곳이 있으면
            if visited[w] == 0:               # 방문 안했어? 해
                top += 1
                stack[top] = v                  # push
                v = w
                break
        else:                           # 더 이상 갈 곳이 없으면
            if top > -1:                # pop
                v = stack[top]
                top -= 1
            else:
                break
    return 0

for _ in range(10):
    test_case, N = map(int, input().split())
    arr = list(map(int, input().split()))
    adjL = [[] for _ in range(N+1)]

    for i in range(len(arr)//2):
        v1, v2 = arr[i*2], arr[i*2+1]           # 두개씩 잘라서
        adjL[v1].append(v2)

    print(f'#{test_case}', f(N))