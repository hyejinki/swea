#2071_평균값 구하기
n = int(input())
for i in range(n):
    v = list(map(int,input().split()))
    ave_v = round(sum(v)/10)
    print(f"#{i+1} {ave_v}")