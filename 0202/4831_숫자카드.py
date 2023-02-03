T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    maxIdx = 0
    for i in range(len(arr)):
        if arr[maxIdx] <= arr[i]:
            maxIdx = i           # 가장 큰 값을 가진 인덱스 찾음

    counts = [0] * (arr[maxIdx] + 1)
    temp = [0] * N
    # 개수 찾기
    for i in range(len(arr)):
        counts[arr[i]] += 1
    # counts의 맥스 값 찾기
    most_i = 0

    for i in range(len(counts)):
        if counts[most_i] <= counts[i]:
            most_i = i            # 해당 인덱스가 곧 최빈값


    print(f'#{test_case}', most_i, counts[most_i])


