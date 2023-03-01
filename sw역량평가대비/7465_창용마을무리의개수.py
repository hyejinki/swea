T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    adjL = [[] for _ in range(N+1)]
    for _ in range(M):
        v, w = map(int, input().split())
       
        adjL[v].append(w)
    print(adjL)

    