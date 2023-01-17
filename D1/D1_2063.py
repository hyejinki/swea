#2063_중간값 찾기

n = int(input())
v = list(map(int,input().split()))
v.sort()
i = int((n-1) / 2)
print(v[i])