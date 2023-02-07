
for test_case in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(100)]
    # 양 옆에 0으로 채워줌
    new_arr = [[0]*102 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            new_arr[i][j+1] = arr[i][j]
    