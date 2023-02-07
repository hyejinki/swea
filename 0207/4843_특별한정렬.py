T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N-1):                    # 선택정렬
        maxidx = i
        for j in range(i+1, N):
            if arr[j] > arr[maxidx]:
                maxidx = j
        arr[i], arr[maxidx] = arr[maxidx], arr[i]
    new_arr = [0]*10                        # 출력할 배열 만들어 놓고
    i = j= 0
    for i in range(0, 10):
        if i % 2 == 0:                      # 인덱스 0, 2, 4, 6, 8
            new_arr[i] = arr[j]             # 정렬한 arr 순차적으로 넣고
            j += 1
        else:                               # 인덱스 홀수일 때
            new_arr[i] = arr[N-j]           # 뒤에서 부터 넣음

    print(f'#{test_case}', *new_arr)