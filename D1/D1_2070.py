# 2070_큰 놈, 작은 놈, 같은 놈

n = int(input())
for i in range(n):
    v = list(map(int,input().split()))
    if v[0] > v[1]:
        result = ">"
    elif v[0] < v[1]:
         result = "<"
    else:
         result = "="
    print(f"#{i+1} {result}")