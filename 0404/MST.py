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

def findset(i):
    while rep[i] != i:
        i = rep[i]
    return i        # rep[i] == i 자기 자신을 가리키면 대표 원소

def union(x, y):
    rep[findset(y)] = findset(x)

V, E = map(int, input().split())
#makeset()
rep = [i for i in range(V + 1)]
graph = []
for _ in range(E):
    v1, v2, w = map(int, input().split())
    graph.append([v1, v2, w])
    # graph.append([w, v1, v1)]
# (1) 가중치 기준 오름차순 정렬
graph.sort(key=lambda x:x[2])
# graph.sort()

# (2) N개 정점(v+1), N - 1개의 간선 선택
N = V + 1
s = 0               # MST에 포함된 간선의 가중치 합
cnt = 0
MST = []
for v, u, w in graph:       # 가중치가 작은 것부터...
    if findset(u) != findset(v):        # 사이클이 생기지 않으면
        cnt += 1
        s += w          # 가중치 합
        MST.append([u, v, w])
        union(u, v)
        if cnt == N - 1:        # MST 구성 완료
            break
print(s)
print(MST)
