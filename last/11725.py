N = int(input())
adjL = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    v, w = map(int, input().split())
    adjL[v].append(w)

print(adjL)
