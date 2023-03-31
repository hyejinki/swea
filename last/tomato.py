from collections import deque

d_ij = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def bfs(N, M):

    q = deque([])
    for x in coor:
        q.append((x[0], x[1], 1))       # 3번째 요소는 싸이클 돌 때마다 누적 합(출력 값)
        visited[x[0]][x[1]] = 1
    while q:
        r, c, v = q.popleft()
        for k in range(4):
            ni, nj = r + d_ij[k][0], c + d_ij[k][1]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                q.append((ni, nj, v + 1))
                visited[ni][nj] = v + 1
    ans = v - 1

    for i in range(N):              # 0이 남아있으면!
        if 0 in visited[i]:
            ans = -1

    return ans


M, N = map(int, input().split())
tmt = [list(map(int, input().split())) for _ in range(N)]
coor = []
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if tmt[i][j] == 1:          # 1이면 좌표 append
            coor.append((i, j))
        if tmt[i][j] == -1:         # -1이면 -1이라고 체크해줘야됨
            visited[i][j] = -1

if len(coor) == 0:
    print(-1)
else:
    print(bfs(N, M))