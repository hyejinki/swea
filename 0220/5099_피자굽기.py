T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = [0]*N
    front = rear = top = -1
    dic = {}                        # key: 피자받침 번호 value그때의 arr의 인덱스
    for i in range(N):
        dic[i] = i + 1
        rear += 1
        top += 1
        queue[rear] = arr[top]
    while True:
        front = (front + 1) % N
        rear = (rear + 1) % N
        queue[rear] = queue[front] // 2
        if queue[front] == 0:
            if top < M-1:            # arr 끝까지 갔으면 no push
                top += 1
                queue[rear] = arr[top]
                dic[rear] = top
        if queue.count(0) == N - 1:     # 하나만 남으면 끝
            break

    for x in range(N):
        if queue[x] != 0:
            print(f'#{test_case}',dic[x]+1)