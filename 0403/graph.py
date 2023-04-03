'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

#재귀
def dfs1(v, k):     # 중복 없이 , 빠짐 없이
    visited[v] = 1  # 중복방지용
    print(v)
    # for w in adjL[v]:
    #     if visited[w] == 0:
    #         dfs1(w, k)
    for w in range(1, k + 1):
        if adjM[v][w] == 1 and visited[w] == 0:
            dfs1(w, k)

def dfs2(s, k):
    stack = []
    visited = [0] * (k + 1)
    v = s
    while True:
        if visited[v] == 0:
            print(v)
            visited[v] = 1

        for w in range(1, k + 1):
            if adjM[v][w] and visited[w] == 0:
                stack.append(v)
                v = w
                break
        else:       # 더이상 인접 정점이 없으면
            if stack:       # 스택이 비어있지 않으면
                v = stack.pop()
            else:           # 스택이 비어있으면
                break

def dfs3(v, k, g):          # v에서 g까지 가능한 모든 경로 탐색
    global cnt
    if v == g:
        cnt += 1            # 목적지 도착 횟수
    else:
        visited[v] = 1  # 중복방지용
        for w in range(1, k + 1):
            if adjM[v][w] == 1 and visited[w] == 0:
                dfs3(w, k, g)
        visited[v] = 0

def dfs4(v, k):
    sp = -1
    stack = [0] * k         #스택 생성, 스택포인터 초기화
    visited = [0] * (k + 1)
    # 시작점 push(stack을 탐색할 정점 목록으로 활용)
    sp += 1             # push와 방문표시(목록에 이미 올라가 있음)
    stack[sp] = v
    visited[v] = 1
    while sp > -1:
        v = stack[sp]       # pop()
        sp -= 1
        print(v)
        for w in range(1, k + 1):
            if adjM[v][w] and visited[w] == 0:
                sp += 1  # push와 방문표시(목록에 올림)
                stack[sp] = w
                visited[w] = 1
    return


V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjM = [[0]*(V + 1) for _ in range(V + 1)]
adjL = [[]for _ in range(V + 1)]
cnt = 0
for i in range(E):
    n1, n2 = arr[i * 2], arr[i * 2 + 1]
    adjM[n1][n2] = 1
    adjM[n2][n1] = 1        # 방향이 없는 경우
    adjL[n1].append(n2)
    adjL[n2].append(n1)
visited = [0] * (V + 1)

# dfs1(1, V)
# dfs2(1, V)
# dfs3(1, V, 7)
# print(cnt)

dfs4(1, V)
print(*bfs(V, E))