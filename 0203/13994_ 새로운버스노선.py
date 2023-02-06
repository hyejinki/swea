T = int(input())
 
for test_case in range(1, T+1):
    total_arr = [0]*1001
    N = int(input())
    for _ in range(N):
        arr = list(map(int, input().split()))
        start = arr[1]          # 처음 정류장
        end = arr[2]            # 마지막 정류장
        if arr[0] == 1:         # 구간 사이 모든 정류장
            for i in range(start, end + 1):
                total_arr[i] += 1
         
        elif arr[0] == 2:       # 홀이면 홀 짝이면 짝
            for i in range(start, end + 1, 2):
                total_arr[i] += 1
            if end not in total_arr:
                total_arr[end] += 1
                 
        elif arr[0] == 3:
            if start % 2 == 0:
                for i in range(start, end + 1):
                    if i % 4 == 0 and i % 10 != 0:
                        total_arr[i] += 1
                    elif i == start or i == end:    # 처음, 마지막 정류장 포함
                        total_arr[i] += 1
            else:
                for i in range(start, end + 1):
                    if i % 3 == 0 and i % 10 != 0:
                        total_arr[i] += 1
                    elif i == start or i == end:    # 처음, 마지막 정류장 포함
                        total_arr[i] += 1
 
    maxV = 0
    for i in total_arr:
        if i > maxV:
            maxV = i
 
    print(f'#{test_case}', maxV)