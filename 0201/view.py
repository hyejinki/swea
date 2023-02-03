for test_case in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    count = 0

    for i in range(N - 4):
        maxV = 0
        subV = 0
        for j in range(i, i + 5):
            if maxV < arr[j] and i + 2 != j:
                maxV = arr[j]

        if maxV < arr[i + 2]:
            count += (arr[i + 2] - maxV)

    print(f'#{test_case} {count}')

