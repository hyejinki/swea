
def bfs(v, G, N):
    visited = [0]*(N+1)
    queue = [v]
    visited[v] = 1
    while queue:
        t = queue.pop(0)
        for i in adjL[t]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[t] + 1
    if visited[G] == 0:         # 노드 S와 G가 서로 연결되어 있지 않다면, 0을 출력한다
        return 0
    else:
        return visited[G] - 1


T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V + 1)]
    for _ in range(E):
        v, w = map(int, input().split())
        adjL[v].append(w)
        adjL[w].append(v)
    S, G = map(int, input().split())

    print(f'#{test_case}', (bfs(S, G, V)))