#2072_홀수만 더하기
n = int(input())
for i in range(n):
    v = list(map(int,input().split()))
    sum = 0
    for j in v:
        if j%2==1:
            sum += j
    print(f"#{i+1} {sum}")
