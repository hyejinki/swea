import sys
N = int(sys.stdin.readline())        # 가게 수
arr = list(map(int, sys.stdin.readline().strip().split()))
cost = 0
for i in range(len(arr)):
    if arr[i + 1] > arr[i + 2]:                 # 두번째가 세번째보다 크면

        cost += 5 * min(arr[i], (arr[i + 1] - arr[i + 2])) # 만큼 산다
        arr[i + 1] -= min(arr[i], (arr[i + 1] - arr[i + 2]))
        if arr[i] > (arr[i + 1] - arr[i + 2]):
            cost += 3 * (arr[i] - (arr[i + 1] - arr[i + 2]))

    else:
        cost += 7 * min(arr[i], arr[i + 1], arr[i + 2])     # 3개 삼
        if arr[i]:                                          # 남으면 사
            cost += 3 * (arr[i] - min(arr[i], arr[i + 1], arr[i + 2]))