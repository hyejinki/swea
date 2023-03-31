K = int(input())
for tc in range(K):
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V + 1)]
    for _ in range(E):
        v, w = map(int, input().split())
        adjL[v].append(w)
    print(adjL)