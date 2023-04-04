'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
def prim(V):
    MST = []   # MST에 포함된 정점인지 표시
    MST.append(0)          # 0번 정점부터
    s = 0                   # MST를 구성한 간선 가중치의 합
    for _ in range(V):  # 0번을 제외한 나머지 모든 정점에 대해
        minV = 100      # 문제에 주어진 가중치 최대값 이상으로 초기화
        t = 0
        for u in MST:    # MST에 포함된 정점에 대해
            for v in range(V+1):
                if adjM[u][v]!=0 and v not in MST:  # 인접이고 아직 MST에 속하지 않은v
                    if minV>adjM[u][v]:
                        minV = adjM[u][v]
                        t = v
        MST.append(t)   # MST에 속한 정점과 인접한 정점 중 가중치가 최소인 정점
        s += minV
    return s

V, E = map(int, input().split())
s = int(input())
adjM = [[0] *(V+1) for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w
    adjM[v][u] = w  # 방향이 없으므로
print(prim(V))