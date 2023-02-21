for test_case in range(1, 11):
    tc = int(input())
    num = list(map(int, input().split()))
    queue = [0] * 100000
    front = rear = -1
    for i in range(8):
        rear += 1                   # 마지막 삽입 인덱스
        queue[i] = num[i]
    while True:
        for i in range(1,6):
            front += 1
            rear += 1
            queue[rear] = queue[front] - i
            if queue[rear] <= 0:
                break
        if queue[rear] <= 0:            # 0보다 작아도 0
            queue[rear] = 0
            break

    print(f'#{test_case}', *queue[front+1:rear+1])