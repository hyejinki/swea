#2068_최대수 구하기

n = int(input())
for i in range(n):
    v = list(map(int,input().split()))
    max_v = max(v)
    print(f"#{i+1} {max_v}")
