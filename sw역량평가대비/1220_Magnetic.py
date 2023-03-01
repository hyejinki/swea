# 1 다음 2가 나오면 counts++
for test_case in range(1, 11):
    N = int(input())
    board = [list(map(int, input().split()))for _ in range(N)]
    counts = 0
    for j in range(N):
        flag = 0            # 1을 만나면 1 아니면 0
        i = 0 
        while 0 <= i < N:
            if board[i][j] == 1:
                flag = 1
            if flag == 1 and board[i][j] == 2:  # 전에 1을 만난 상태에서 2가 나오면
                counts += 1
                flag = 0
            i += 1
    print(f'#{test_case}', counts)
    