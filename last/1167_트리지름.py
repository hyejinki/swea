from collections import deque
def bfs(start, V):
    dq = deque([start])
    visited = [0]*(V+1)
    visited[start] = 1

    while dq:
        x, d = dq.popleft(), info[x][1]

        for i in info[x]:
            if visited[i[0]] == 0:
                dq.append(i[1])
                visited[i[0]] = d + 1

    return max(visited)


V = int(input())
info = [[] for _ in range(V + 1)]
for _ in range(V):
    temp = list(map(int, input().split()))
    v = temp[0]
    for i in range(1, len(temp), 2):
        if temp[i] == -1:
            break
        else:
            info[v].append((temp[i], temp[i+1]))

print(bfs(1, V))