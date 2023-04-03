def findset(i):
    while rep[i] != i:
        i = rep[i]
    return i        # rep[i] == i 자기 자신을 가리키면 대표 원소

def union(x, y):
    rep[findset(y)] = findset(x)


# make -set (1) ~ (6)


rep = [i for i in range(8)]
union(2, 3)
union(4, 5)
union(4, 6)
union(7, 4)


print(rep)