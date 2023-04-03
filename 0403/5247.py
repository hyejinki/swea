from collections import deque

def bfs(s, e):
    q = [s]
    visited = [0] * 10000001
    visited[s] = 1
    while q:
        v = q.pop(0)
        if v == e:
            return visited[v]
        else:
            c1 = (v + 1)
            c2 = (v - 1)
            c3 = (v * 2)
            c4 = (v - 10)
            for x in [c1, c2, c3, c4]:
                if 0 < x <= 1000000 and visited[x] == 0:
                    q.append(x)
                    visited[x] = visited[v] + 1



T = int(input())
for test_case in range(1, T + 1):
    s, e = map(int, input().split())

    print(f'#{test_case}', bfs(s, e) - 1)