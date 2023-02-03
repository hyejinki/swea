# 주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라
# N은 5 이상 50 이하

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


    print(f'#{test_case}', *arr)
