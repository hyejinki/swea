T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    adjM = [[0] *(V+1) for _ in range(V+1)]