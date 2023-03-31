from collections import deque
import copy
d_ij = [[-1, 0], [0, 1], [1, 0], [0, -1]]
def path(N, M):
    dq = deque([(0,0)])
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    while dq:
        r, c = dq.popleft()
        if r == N - 1 and c == M - 1:
            return visited[r][c]
        for k in range(4):
            ni, nj = r + d_ij[k][0], c + d_ij[k][1]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and\
                    (arr_T[ni][nj] == 0 or arr[ni][nj] == 0):
                dq.append((ni, nj))
                visited[ni][nj] = visited[r][c] + 1
    if len(dq) == 0 and (r != N - 1 or c != M - 1):
        return -1
v = [[0, 0] [1, 0] [2, 0] [0, 3]]
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
compare = []

for i in range(N):
    for j in range(M):
        arr_T = copy.deepcopy(arr)
        if arr[i][j] == 1:
            arr_T[i][j] = 0
        compare.append(path(N, M))
compare.append(path(N, M))
ans = []
for x in compare:
    if 0 <= x:
        ans.append(min(compare))

if len(ans) == 0:
    ans = [-1]

print(min(ans))