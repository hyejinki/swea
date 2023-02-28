

arr = list(map(int, input()))
N = len(arr)
num = 0
for i in range(N):
    j = i % 7
    num += arr[i] * (2**(6-j))
    if j == 6:          # 7개 끊기
        print(num, end=' ')
        num = 0