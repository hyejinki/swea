def bfs(s):
    q = []
    visited = [0] * 101
    q.append(s)             # 초기 설정
    visited[s] = 1
    ans = 0
    while len(q):
        v = q.pop(0)        #  v :현재
        # 조건 제일 늦게 나타난 노드 , 그 중 가장 큰 숫자
        if visited[v] > visited[ans] or (visited[ans] == visited[v] and\
            ans < v):
            ans = v

        for n in adj[v]:
            if visited[n] == 0:
                q.append(n)
                visited[n] = visited[v] + 1         # 누적 합

    return ans
T = 10
for test_case in range(1, T+1):
    L, start = map(int, input().split())
    arr = list(map(int, input().split()))
    adj = [[] for _ in range(101)]
    for i in range(0, L, 2):             # 두 개씩 잘라서
        p, c = arr[i], arr[i+1]
        adj[p].append(c)
    print(f'#{test_case}', bfs(start))