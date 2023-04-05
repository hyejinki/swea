def prim(V):
    MST = []   
    MST.append(1)         
    s = 0                  
    for _ in range(V):  
        minV = 100     
        t = 0
        for u in MST:    
            for v in range(V+1):
                if adjM[u][v]!=0 and v not in MST:  
                    if minV > adjM[u][v]:
                        minV = adjM[u][v]
                        t = v
        MST.append(t)  
        
        s += minV
        print(s)
    # return s
    

V, E = map(int, input().split())
s = int(input())
adjM = [[0] *(V+1) for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w
prim(V)    
print(adjM)