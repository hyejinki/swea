# 최솟값 인덱스 찾기
def min_value(arr):
    min_i = 0
    for i in range(len(arr)):
        if arr[min_i] > arr[i]:
            min_i = i
    return min_i

# 최댓값 인덱스 찾기
def max_value(arr):
    max_i = 0
    for i in range(len(arr)):
        if arr[max_i] < arr[i]:
            max_i = i
    return max_i


for test_case in range(1, 2):
    D = int(input())
    arr = list(map(int, input().split()))
    i = 0
    while(i < D):
        highest = arr[max_value(arr)]
        lowest = arr[min_value(arr)]
        # 평탄화 완료되면 브레이크
        if highest - lowest == 0 or highest - lowest == 1:

            break
        # 덤프
        else:
            arr[max_value(arr)] -= 1
            arr[min_value(arr)] += 1



