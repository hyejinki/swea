

V, E = map(int, input().split())
s = int(input())
adjM = [[0] *(V+1) for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w
print(adjM)