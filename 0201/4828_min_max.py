# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    maxV = 1        # 들어올 수 있는 가장 작은 값
    minV = 1000000  # 들어올 수 있는 가장 큰 값

    for i in range(1, N):
        if maxV < arr[i]:
            maxV = arr[i]
        if minV > arr[i]:
            minV = arr[i]

    print(f'#{test_case} {maxV-minV}')